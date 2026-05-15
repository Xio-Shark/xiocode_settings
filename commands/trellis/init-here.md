---
description: Initialize Trellis in the current directory (any project)
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



Initialize Trellis workflow in the current project directory.

Run:
```bash
trellis init -u xioshark
```

If `trellis` command is not available, install it first:
```bash
npm install -g @mindfoldhq/trellis@latest
```

After init, verify:
```bash
ls .trellis/
python3 .trellis/scripts/get_context.py
```

Then read `.trellis/workflow.md` to understand the project workflow.
