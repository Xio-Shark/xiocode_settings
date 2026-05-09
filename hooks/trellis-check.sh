#!/bin/bash
# Trellis Auto-Detection for Claude Code
# This hook runs before every Bash tool use to check if Trellis context is loaded

# Only check once per session
TRELLIS_CHECKED_FILE="/tmp/claude-trellis-checked-$$"
if [ -f "$TRELLIS_CHECKED_FILE" ]; then
    exit 0
fi

# Check if current directory has .trellis or global trellis exists
if [ -d ".trellis" ]; then
    echo "📋 Trellis project detected"
    
    # Check active task
    if [ -f ".trellis/.current-task" ]; then
        TASK=$(cat .trellis/.current-task | tr -d '\n')
        if [ -n "$TASK" ]; then
            echo "⚠️  Active task: $TASK"
            echo "   Run '/trellis:context' to load full context"
        fi
    else
        echo "   No active task. Run '/trellis:context' to see project state."
    fi
    
    touch "$TRELLIS_CHECKED_FILE"
elif [ -d "$HOME/.codex/trellis" ]; then
    echo "📋 Trellis global context available (run '/trellis:context' to load)"
    touch "$TRELLIS_CHECKED_FILE"
fi

exit 0
