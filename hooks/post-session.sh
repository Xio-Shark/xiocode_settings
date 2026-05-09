#!/bin/bash
# code-agent-insights: Auto-index on session end
# Installed by: cai hooks install

LOG_FILE=~/.code-agent-insights/hooks.log

{
  echo "========================================="
  echo "[$(date)] Session ended - starting hook"

  # Wait a moment for session file to be written
  echo "Waiting 2s for session file..."
  sleep 2

  # Index the recent session (using 6h to avoid timezone edge cases)
  echo "Running: cai index --since 6h"
  if cai index --since 6h; then
    echo "✓ Index completed successfully"
  else
    echo "✗ Index failed with exit code $?"
  fi

  # Generate summary if API key available
  if [ -n "$ANTHROPIC_API_KEY" ]; then
    echo "Running: cai summarize --last-session"
    if cai summarize --last-session 2>&1; then
      echo "✓ Summarize completed"
    else
      echo "⚠ Summarize failed or skipped (check API key and credits)"
    fi
  else
    echo "ℹ Skipping summarization (ANTHROPIC_API_KEY not set)"
    echo "  To enable: export ANTHROPIC_API_KEY=sk-ant-..."
  fi

  # Check if auto-sync is enabled
  if grep -q "autoSync: true" ~/.code-agent-insights/config.yaml 2>/dev/null; then
    echo "Running: cai sync"
    if cai sync 2>&1; then
      echo "✓ Sync completed"
    else
      echo "⚠ Sync failed or skipped"
    fi
  fi

  echo "[$(date)] Hook completed"
  echo "========================================="
} >> "$LOG_FILE" 2>&1
