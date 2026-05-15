---
name: project_claude_config
description: Claude Code configuration optimization project status.
type: project
---

**Active project:** xiocode_settings — version-controlled Claude Code configuration.

**Repo:** https://github.com/Xio-Shark/xiocode_settings

**What was done (2026-05-09):**
- CLAUDE.md: 685 → 297 lines (-57%), extracted RTK/skills refs
- AGENTS.md: deduplicated, now 31-line pure index
- MCP security: removed hardcoded API key, stabilized script paths
- Memory system: booted with user + feedback + project + reference types
- Permissions: expanded from 5 → 28 entries

**Decision log:**
- Rejected agentmemory integration — too heavy (~21K LOC service) for current scale. Manual markdown memory is sufficient and aligns with Glue Coding philosophy.

**Next when touching this:**
- Update README if config changes
- Keep memory files under 20 total to avoid context bloat
