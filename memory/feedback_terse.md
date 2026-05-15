---
name: feedback_terse
description: User prefers concise responses without trailing summaries or follow-up suggestions.
type: feedback
---

**Rule:** Do not propose follow-up tasks or enhancements at the end of answers. Do not summarize what was just done.

**Why:** User explicitly configured this in CLAUDE.md (`Do not propose follow-up tasks or enhancement at the end of your final answer`) and has confirmed this preference through interaction patterns.

**How to apply:** End responses with the answer itself. No "Next steps", "You could also", "Summary" sections. The diff or output speaks for itself.
