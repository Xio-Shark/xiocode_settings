---
description: Load Trellis project context (spec, workflow, task status)
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



Load the full Trellis context for the current project.

Run these commands and summarize the output:

```bash
python3 "$TRELLIS_SCRIPTS/"get_context.py
python3 "$TRELLIS_SCRIPTS/"get_context.py --mode packages
```

Then read the relevant spec indices:
- `.trellis/spec/guides/index.md`
- `.trellis/spec/frontend/index.md` (if working on frontend)
- `.trellis/spec/backend/index.md` (if working on backend)

Report back:
1. Current active task (if any)
2. Git status summary
3. Available spec packages
4. Any tasks that need attention
