---
name: feedback_glue_coding
description: User follows Glue Coding philosophy — prefer composing existing tools over writing custom business logic.
type: feedback
---

**Rule:** When creating new functionality, always check if a skill, plugin, library, or sub-agent already covers it. Custom code should only be glue/composition.

**Why:** User's core engineering philosophy. Violations have led to unnecessary code generation in past sessions.

**How to apply:** Before implementing, scan skills directory and ask "can an existing component do this?" Prefer `services/` for orchestration, `libs/` only for truly missing utilities.
