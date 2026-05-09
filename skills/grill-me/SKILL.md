---
name: grill-me
description: |
  Relentlessly interview the user about a plan, design, or proposal until reaching shared understanding.
  Walk down every branch of the decision tree, resolving dependencies between decisions one-by-one.
  Use when user wants to: stress-test a plan, get grilled on their design, validate assumptions,
  find blind spots, harden an architecture, review a proposal, "grill me", "拷问我的方案",
  "压力测试", "find holes in my plan", "poke holes", "devil's advocate", or mentions
  reviewing / validating / critiquing a plan, design doc, RFC, or technical decision.
---

# Grill Me — Plan Stress-Test Protocol

## Purpose

Transform vague or under-specified plans into robust, fully-explored designs by systematically interrogating every assumption, branch, and dependency.

## Trigger Conditions

Auto-activate when user signals intent to validate a plan:
- Explicit: "grill me", "stress-test", "拷问", "压力测试", "find holes"
- Implicit: presenting a plan/design/RFC without explicit validation request
- Contextual: user is about to start implementation on an unvalidated plan

## Protocol

### Phase 1: Scope Clarification (1-2 questions)

1. What is the **goal** of this plan? (Success criteria)
2. What are the **constraints**? (Time, budget, tech, organizational)

### Phase 2: Systematic Interrogation

Walk down each branch of the design tree. For every decision:

1. **Ask** the question (one at a time)
2. **Provide your recommended answer** based on context
3. **Resolve** the user's choice before moving deeper

Question categories to cover:

| Category | Example Questions |
|----------|-------------------|
| Assumptions | What assumptions are we making? What if they're wrong? |
| Dependencies | What does this depend on? Are those dependencies reliable? |
| Edge Cases | What happens in the failure path? What about scale limits? |
| Trade-offs | What alternatives did you reject? Why? |
| Ownership | Who maintains this? Who's on-call? |
| Rollback | How do we undo this if it goes wrong? |
| Metrics | How do we know this succeeded? What do we monitor? |

### Phase 3: Synthesis

After exhausting all branches, summarize:
1. **Open questions** still unresolved
2. **Risks** ranked by severity × likelihood
3. **Recommended next steps**

## Rules

- Ask **one question at a time**. Wait for answer before next.
- If a question can be answered by **exploring the codebase**, explore first.
- Be **relentless but respectful** — the goal is shared understanding, not winning.
- **Flag contradictions** between earlier and later answers immediately.
- If the plan changes mid-interrogation, **backtrack** to affected branches.

## Anti-Patterns to Flag

- Hand-waving over "later" or "TBD" without explicit acceptance
- Unvalidated assumptions presented as facts
- Missing failure paths or error handling
- No rollback / no metrics / no owner
- Premature optimization without identified bottleneck
