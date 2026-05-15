---
name: reference_resources
description: Pointers to external systems and resources relevant to this workspace.
type: reference
---

**Config repo:** https://github.com/Xio-Shark/xiocode_settings
- Personal Claude Code configuration (CLAUDE.md, agents, hooks, MCP, memory)
- Push changes here after modifying ~/.claude/ config

**Trellis workflow:**
- Global spec: `~/.claude/TRELLIS-WORKFLOW.md`
- Init: `trellis init -u xioshark`

**Key tools:**
- RTK (token optimizer): `rtk --version` → 0.37.1
- ccline (status line): `~/.claude/ccline/ccline`
- Context7 MCP docs: requires `CONTEXT7_API_KEY` env var

**Skills registry:**
- Local: `~/.claude/skills/` (90 skills)
- Full routing table: `~/.claude/skills/.system/SKILLS-REFERENCE.md`
