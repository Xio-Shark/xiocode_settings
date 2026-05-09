---
description: Start working on a Trellis task
argument-hint: <task-slug>
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



Start the Trellis task: $ARGUMENTS

Run:
```bash
python3 "$TRELLIS_SCRIPTS/"task.py start "$ARGUMENTS"
```

Confirm the task is now active.
