---
name: "openai-docs"
description: "Use when the user needs current official OpenAI documentation with citations."
---


# OpenAI Docs

## Rules

- 先用 OpenAI 官方文档 MCP，再考虑任何网页兜底。
- 兜底检索只允许官方 OpenAI 域名，并且必须带引用。
- 文档没有覆盖的内容要明确说明，不要猜测。

Provide authoritative, current guidance from OpenAI developer docs using the developers.openai.com MCP server. Always prioritize the developer docs MCP tools over web.run for OpenAI-related questions. Only if the MCP server is installed and returns no meaningful results should you fall back to web search.

## Quick start

- Use `mcp__openaiDeveloperDocs__search_openai_docs` to find the most relevant doc pages.
- Use `mcp__openaiDeveloperDocs__fetch_openai_doc` to pull exact sections and quote/paraphrase accurately.
- Use `mcp__openaiDeveloperDocs__list_openai_docs` only when you need to browse or discover pages without a clear query.

## If MCP server is missing

If MCP tools fail or no OpenAI docs resources are available:

1. Run the install command yourself: `codex mcp add openaiDeveloperDocs --url https://developers.openai.com/mcp`
2. If it fails due to permissions/sandboxing, immediately retry the same command with escalated permissions and include a 1-sentence justification for approval. Do not ask the user to run it yet.
3. Only if the escalated attempt fails, ask the user to run the install command.
4. Ask the user to restart Codex.
5. Re-run the doc search/fetch after restart.

## Workflow

1. Clarify the product scope (Codex, OpenAI API, or ChatGPT Apps SDK) and the task.
2. Search docs with a precise query.
3. Fetch the best page and the specific section needed (use `anchor` when possible).
4. Answer with concise guidance and cite the doc source.
5. Provide code snippets only when the docs support them.

## Quality rules

- Treat OpenAI docs as the source of truth; avoid speculation.
- Keep quotes short and within policy limits; prefer paraphrase with citations.
- If multiple pages differ, call out the difference and cite both.
- If docs do not cover the user’s need, say so and offer next steps.

## Tooling notes

- Always use MCP doc tools before any web search for OpenAI-related questions.
- If the MCP server is installed but returns no meaningful results, then use web search as a fallback.
- When falling back to web search, restrict to official OpenAI domains (developers.openai.com, platform.openai.com) and cite sources.
