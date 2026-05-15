---
description: Create a new Trellis task
argument-hint: <task title>
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



Create a new Trellis task with title: $ARGUMENTS

Run:
```bash
python3 "$TRELLIS_SCRIPTS/"task.py create "$ARGUMENTS"
```

Then confirm the task was created and show its directory.
