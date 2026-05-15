---
scope: shell-execution
priority: P0
applies_when: ["写脚本", "终端", "shell", "bash", "heredoc", "多行 python"]
must_run_before: [Bash]
preferred_alternative: WriteFile-tool
---

# AGENTS.shell-safety.md — 终端安全补充规则

> 通用终端安全（闭合引号、优先 `&&`、rtk 前缀、卡死处理）见全局 `~/.claude/CLAUDE.md` §Shell Execution Rules。
> 本文件为项目特有的**更严格**约束。

## 禁止 heredoc（`cat <<'EOF'`）

heredoc 的 `EOF` 结束标记对前导空白极度敏感，极易导致终端卡死。

**正确替代方案（按优先级）：**
1. **首选：WriteFile 工具**（零终端风险）
2. **次选：`printf '%s\n'`**
   ```bash
   printf '%s\n' 'line 1' 'line 2' > /path/to/file
   ```
3. **三选：`echo -e` 配合 `\n`**（仅限简单内容）
4. **批量多行：Python 临时文件**（不用 `python3 -c`）

## 禁止 `python3 -c "` 执行多行代码

多行 `python3 -c "`、`node -e "` 会让 shell 进入 `dquote>` 继续提示，终端直接卡死。

**正确模式：临时文件**
```bash
cat > /tmp/script.py << 'PYEOF'
import os
print(os.getcwd())
PYEOF
python3 /tmp/script.py
```

**单行可用**（必须在同一行闭合引号）：
```bash
python3 -c "import os; print(os.getcwd())"
```

## 写入前必须确认目录存在

```bash
mkdir -p "$(dirname /path/to/file)" && printf '%s\n' 'content' > /path/to/file
```
