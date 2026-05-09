---
name: before-dev
description: "Discovers and injects project-specific coding guidelines from .trellis/spec/ before implementation begins. Reads spec indexes, pre-development checklists, and shared thinking guides for the target package. Use when starting a new coding task, before writing any code, switching to a different package, or needing to refresh project conventions and standards."
---

## Setup `[AI]`

Detect trellis location (project-level first, global fallback):

```bash
if [ -d .trellis/scripts ]; then
    export TRELLIS_SCRIPTS=.trellis/scripts
    export TRELLIS_WORKFLOW=.trellis/workflow.md
    export TRELLIS_SPEC=.trellis/spec
else
    export TRELLIS_SCRIPTS=~/.codex/trellis/scripts
    export TRELLIS_WORKFLOW=~/.codex/trellis/workflow.md
    export TRELLIS_SPEC=~/.codex/trellis/spec
fi
```

---



Read the relevant development guidelines before starting your task.

Execute these steps:

1. **Discover packages and their spec layers**:
   ```bash
   python3 "$TRELLIS_SCRIPTS/"get_context.py --mode packages
   ```

2. **Identify which specs apply** to your task based on:
   - Which package you're modifying (e.g., `cli/`, `docs-site/`)
   - What type of work (backend, frontend, unit-test, docs, etc.)

3. **Read the spec index** for each relevant module:
   ```bash
   cat "$TRELLIS_SPEC/"<package>/<layer>/index.md
   ```
   Follow the **"Pre-Development Checklist"** section in the index.

4. **Read the specific guideline files** listed in the Pre-Development Checklist that are relevant to your task. The index is NOT the goal — it points you to the actual guideline files (e.g., `error-handling.md`, `conventions.md`, `mock-strategies.md`). Read those files to understand the coding standards and patterns.

5. **Always read shared guides**:
   ```bash
   cat "$TRELLIS_SPEC/"guides/index.md
   ```

6. Understand the coding standards and patterns you need to follow, then proceed with your development plan.

This step is **mandatory** before writing any code.
