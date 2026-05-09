---
name: rust-pro
description: "Rust programming expertise. Use for Cargo, tokio, ownership, lifetimes, traits. Triggers: Rust, Cargo, tokio, Rust开发, lifetime."
---

# Rust Pro

## Overview

Use this skill for serious Rust work: services, libraries, systems code, async design, unsafe boundaries, and performance tuning.

## Rules

- Prefer idiomatic, safe Rust before reaching for unsafe code.
- Make ownership, lifetime, and concurrency constraints explicit.
- Choose the runtime, framework, and crate stack based on the actual workload.
- Keep tests, linting, and profiling in scope for non-trivial Rust changes.

## When to use

- Building or refactoring Rust services, libraries, or systems tooling
- Solving ownership, lifetime, trait, or async design issues
- Optimizing Rust performance, memory layout, or concurrency behavior
- Designing FFI or unsafe boundaries that need careful invariants

## Do not use when

- The task is a trivial script where Rust expertise is irrelevant
- The user only needs basic syntax help
- Rust is not part of the actual stack or decision space

## Workflow

1. Clarify runtime, safety, and performance constraints.
2. Inspect existing crate, workspace, and framework patterns before designing.
3. Choose the simplest sound architecture for ownership, async execution, and error handling.
4. Implement with explicit types, predictable error paths, and targeted tests.
5. For hot paths, profile before optimizing and document any unsafe invariants.

## Focus areas

- Ownership, borrowing, lifetimes, and trait design
- Tokio, axum, async orchestration, and backpressure
- Error handling with `Result`, `thiserror`, `anyhow`, and context propagation
- Systems concerns such as memory layout, atomics, lock-free patterns, and FFI
- Cargo workspaces, feature flags, clippy, rustfmt, and release hygiene

## Output expectations

- Explain architectural choices concretely, not abstractly
- Call out tradeoffs when choosing crates or runtime patterns
- Show the smallest correct path first, then optimize if needed
