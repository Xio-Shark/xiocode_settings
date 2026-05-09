"""Standalone MCP server entry point for personal knowledge base."""

from app.mcp.kb_server import mcp

if __name__ == "__main__":
    mcp.run(transport="stdio")
