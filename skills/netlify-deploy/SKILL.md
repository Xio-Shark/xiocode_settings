---
name: netlify-deploy
description: "Use when the user wants to deploy or link a web project on Netlify."
---

# Netlify Deployment Skill

## Rules
- 只处理 Netlify 部署，不与其他托管平台混用。
- 先确认 `npx netlify status`，再做 link、init、deploy。
- 默认先做 preview deploy，只有用户明确要求或场景明确时才上 production。

Deploy web projects to Netlify using the Netlify CLI with intelligent detection of project configuration and deployment context.

## Prerequisites

- **Netlify CLI**: Installed via npx (no global install required)
- **Authentication**: Netlify account with active login session
- **Project**: Valid web project in current directory

## Workflow

1. Run `npx netlify status` to verify authentication and whether the repo is already linked.
2. If unauthenticated, guide the user through `npx netlify login` or token setup.
3. If unlinked, try `npx netlify link --git-remote-url <REMOTE_URL>`; if no site exists, use `npx netlify init`.
4. Install dependencies and ensure the project can build locally.
5. Deploy with `npx netlify deploy` first; use `--prod` only when the user explicitly wants production.
6. Return the deploy URL, production URL if relevant, and any next action.

## Handling netlify.toml

If a `netlify.toml` file exists, the CLI uses it automatically. If not, the CLI will prompt for:
- **Build command**: e.g., `npm run build`, `next build`
- **Publish directory**: e.g., `dist`, `build`, `.next`

Common framework defaults:
- **Next.js**: build command `npm run build`, publish `.next`
- **React (Vite)**: build command `npm run build`, publish `dist`
- **Static HTML**: no build command, publish current directory

## Error Handling
- Not logged in: run `npx netlify login`
- No site linked: run `npx netlify link` or `npx netlify init`
- Build failed: verify build command, publish directory, and local dependency install
- Publish directory not found: confirm the local build actually created it

## Bundled references
- `references/cli-commands.md`
- `references/deployment-patterns.md`
- `references/netlify-toml.md`
