---
inclusion: always
---

# Shell Execution Rules

## Multi-line Python / Script Execution

**NEVER** use `python3 -c "` (or `python -c "`, `node -e "`, `ruby -e "`) to execute multi-line code in the terminal. An unclosed quote string causes the shell to enter a continuation prompt (`dquote>`, `∙`, etc.) and the agent session hangs indefinitely.

### Correct Patterns

**Pattern A: Temporary file (preferred for >1 line)**
```bash
cat > /tmp/fix_yaml.py << 'PYEOF'
import yaml
from pathlib import Path

for p in Path('.').glob('private/tasks/*.yaml'):
    try:
        yaml.safe_load(p.read_text())
    except Exception as e:
        print(f"Broken: {p} — {e}")
PYEOF
python3 /tmp/fix_yaml.py
```

**Pattern B: Heredoc without temp file**
```bash
python3 << 'PYEOF'
import os
print(os.getcwd())
PYEOF
```

**Pattern C: Single-line only (for trivial one-liners)**
```bash
python3 -c "import os; print(os.getcwd())"
```

### Forbidden Patterns

```bash
# ❌ NEVER — unclosed double quote
python3 -c "
import os
print(os.getcwd())
"

# ❌ NEVER — unclosed single quote
python3 -c '
import os
print(os.getcwd())
'

# ❌ NEVER — mixing quotes across lines
node -e "
console.log('hello')
"
```

## General Terminal Safety

1. **Always close quotes** before pressing Enter. If a command starts with `"`, `'`, or `` ` ``, ensure the matching closing character is on the same line or properly escaped.
2. **Prefer `&&` over `;`** when chaining commands that depend on each other.
3. **Quote paths**: `cd "/path with spaces"` not `cd /path with spaces`.
4. **Use `rtk` prefix** for build/test/git commands (see RTK section) to reduce token usage.
5. **If a command hangs** (no output for >30s), press `Ctrl+C` to cancel, then rewrite using Pattern A or Pattern B.
