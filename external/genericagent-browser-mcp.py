#!/usr/bin/env python3
"""
GenericAgent Browser MCP Bridge
把 TMWebDriver + simphtml 封装为 MCP Server。
支持: Claude Code / Claude Desktop / Codex / Kimi Code CLI 等。

用法:
    python mcp_bridge.py
    # 然后在 MCP 客户端中配置 stdio 方式调用本脚本。
"""

import sys
import os
import json
import asyncio

# 确保能找到同目录下的 GenericAgent 核心模块
GA_DIR = os.path.dirname(os.path.abspath(__file__))
if GA_DIR not in sys.path:
    sys.path.insert(0, GA_DIR)

# GenericAgent 模块在 import 时可能会修改 stdout/stderr，先保留
_original_stdout = sys.stdout
_original_stderr = sys.stderr

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from TMWebDriver import TMWebDriver
import simphtml

# ---------- 初始化浏览器驱动 ----------
# 启动本地 WebSocket + HTTP 网关，等待浏览器扩展连接
driver = TMWebDriver(host="127.0.0.1", port=18765)
print(
    "[GenericAgent MCP] TMWebDriver 已启动，等待浏览器扩展连接 ws://127.0.0.1:18765 ...",
    file=_original_stderr,
    flush=True,
)

# ---------- Tool 定义 ----------
TOOLS = [
    Tool(
        name="browser_navigate",
        description="让浏览器跳转到指定 URL。若当前无活动标签页，会自动等待扩展连接。",
        inputSchema={
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "目标网址，例如 https://github.com"},
                "session_id": {"type": "string", "description": "可选，指定要操作的标签页 session_id"},
            },
            "required": ["url"],
        },
    ),
    Tool(
        name="browser_scan",
        description="获取当前页面的简化 HTML（自动过滤广告、边栏、浮动层）和标签页列表。"
                    "用于观察页面当前状态，是 browser_execute_js 的辅助观察工具。",
        inputSchema={
            "type": "object",
            "properties": {
                "tabs_only": {
                    "type": "boolean",
                    "description": "仅返回标签页列表，不获取页面内容（节省 Token）",
                },
                "switch_tab_id": {
                    "type": "string",
                    "description": "扫描前先切换到指定标签页",
                },
                "text_only": {
                    "type": "boolean",
                    "description": "返回纯文本模式，不含 HTML 标签",
                },
                "instruction": {
                    "type": "string",
                    "description": "可选指令，用于列表裁剪时的命中保留",
                },
            },
        },
    ),
    Tool(
        name="browser_execute_js",
        description="在浏览器页面上下文中执行任意 JavaScript，实现对页面的完全控制"
                    "（点击、输入、滚动、提取数据、修改 DOM 等）。"
                    "这是操控浏览器的核心工具，优先使用它来完成交互操作。",
        inputSchema={
            "type": "object",
            "properties": {
                "script": {
                    "type": "string",
                    "description": "要执行的 JS 代码。可直接写多行代码，最后一行表达式会自动作为返回值。"
                                   "如需点击: document.querySelector('#btn').click();"
                                   "如需提取: return Array.from(document.querySelectorAll('a')).map(a=>a.href);",
                },
                "switch_tab_id": {"type": "string", "description": "切换到指定标签页后执行"},
                "no_monitor": {
                    "type": "boolean",
                    "description": "是否禁用页面变化监控（默认 false，启用 diff 监控）",
                },
                "save_to_file": {
                    "type": "string",
                    "description": "可选，将 JS 返回的完整结果保存到本地文件路径",
                },
            },
            "required": ["script"],
        },
    ),
    Tool(
        name="browser_click",
        description="通过 CSS 选择器点击页面元素。底层封装为 browser_execute_js。",
        inputSchema={
            "type": "object",
            "properties": {
                "selector": {"type": "string", "description": "CSS 选择器，例如 '#submit' 或 '.btn-primary'"},
                "switch_tab_id": {"type": "string"},
            },
            "required": ["selector"],
        },
    ),
    Tool(
        name="browser_type",
        description="在输入框中填入文本，并触发 input / change 事件。底层封装为 browser_execute_js。",
        inputSchema={
            "type": "object",
            "properties": {
                "selector": {"type": "string", "description": "输入框的 CSS 选择器"},
                "text": {"type": "string", "description": "要输入的文本内容"},
                "switch_tab_id": {"type": "string"},
            },
            "required": ["selector", "text"],
        },
    ),
    Tool(
        name="browser_get_tabs",
        description="获取当前所有已连接的浏览器标签页列表（包含 id、url、title）。",
        inputSchema={"type": "object", "properties": {}},
    ),
    Tool(
        name="browser_new_tab",
        description="新建一个浏览器标签页并打开指定 URL。",
        inputSchema={
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "要打开的网址，默认 http://www.baidu.com/robots.txt"},
            },
        },
    ),
]


# ---------- 辅助函数 ----------
def _ensure_sessions():
    sessions = driver.get_all_sessions()
    if not sessions:
        raise RuntimeError(
            "没有可用的浏览器标签页。请确认:\n"
            "1) Chrome 扩展 'TMWD CDP Bridge' 已安装并启用;\n"
            "2) 至少打开了一个普通网页标签页 (不能是 chrome:// 页面);\n"
            "3) 扩展图标显示已连接 ws://127.0.0.1:18765。"
        )
    return sessions


def _dispatch(name: str, arguments: dict):
    if name == "browser_navigate":
        url = arguments["url"]
        sid = arguments.get("session_id")
        driver.execute_js(f"window.location.href='{url}'", timeout=15, session_id=sid)
        return {"status": "success", "msg": f"已导航到 {url}"}

    if name == "browser_scan":
        _ensure_sessions()
        switch_tab_id = arguments.get("switch_tab_id")
        if switch_tab_id:
            driver.default_session_id = switch_tab_id

        tabs = []
        for sess in driver.get_all_sessions():
            sess.pop("connected_at", None)
            sess.pop("type", None)
            tabs.append(sess)

        result = {
            "status": "success",
            "metadata": {
                "tabs_count": len(tabs),
                "tabs": tabs,
                "active_tab": driver.default_session_id,
            },
        }

        if not arguments.get("tabs_only"):
            html = simphtml.get_html(
                driver,
                cutlist=True,
                maxchars=35000,
                instruction=arguments.get("instruction", ""),
                text_only=arguments.get("text_only", False),
            )
            result["content"] = html
        return result

    if name == "browser_execute_js":
        _ensure_sessions()
        script = arguments["script"]
        switch_tab_id = arguments.get("switch_tab_id")
        if switch_tab_id:
            driver.default_session_id = switch_tab_id

        result = simphtml.execute_js_rich(
            script, driver, no_monitor=arguments.get("no_monitor", False)
        )

        save_path = arguments.get("save_to_file")
        if save_path and "js_return" in result:
            try:
                with open(save_path, "w", encoding="utf-8") as f:
                    f.write(str(result["js_return"] or ""))
                result["saved_to"] = save_path
            except Exception as e:
                result["save_error"] = str(e)
        return result

    if name == "browser_click":
        selector = arguments["selector"]
        switch_tab_id = arguments.get("switch_tab_id")
        script = f"document.querySelector({json.dumps(selector)})?.click(); 'clicked';"
        return _dispatch("browser_execute_js", {
            "script": script,
            "switch_tab_id": switch_tab_id,
            "no_monitor": False,
        })

    if name == "browser_type":
        selector = arguments["selector"]
        text = arguments["text"]
        switch_tab_id = arguments.get("switch_tab_id")
        script = f"""
        const el = document.querySelector({json.dumps(selector)});
        if (!el) throw new Error('Element not found: {selector}');
        el.focus();
        el.value = {json.dumps(text)};
        el.dispatchEvent(new Event('input', {{bubbles: true}}));
        el.dispatchEvent(new Event('change', {{bubbles: true}}));
        'typed';
        """
        return _dispatch("browser_execute_js", {
            "script": script,
            "switch_tab_id": switch_tab_id,
            "no_monitor": False,
        })

    if name == "browser_get_tabs":
        sessions = _ensure_sessions()
        return {"status": "success", "tabs": sessions}

    if name == "browser_new_tab":
        url = arguments.get("url")
        result = driver.newtab(url)
        return {"status": "success", "result": result}

    raise ValueError(f"未知工具: {name}")


# ---------- MCP Server ----------
app = Server("genericagent-browser")


@app.list_tools()
async def list_tools() -> list[Tool]:
    return TOOLS


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    try:
        result = _dispatch(name, arguments)
        return [TextContent(type="text", text=json.dumps(result, ensure_ascii=False, indent=2))]
    except Exception as e:
        return [TextContent(type="text", text=json.dumps({"status": "error", "msg": str(e)}, ensure_ascii=False, indent=2))]


async def main():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options(),
        )


if __name__ == "__main__":
    asyncio.run(main())
