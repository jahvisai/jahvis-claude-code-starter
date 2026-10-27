# <PROJECT NAME>

Updated: <YYYY-MM-DD>

> Template for every new project, the same file in the workspace kit and the CLAUDE.md kit. The
> jah-new-project-lite skill fills it for you; by hand: replace every angle-bracket placeholder,
> keep exactly ONE stack profile block (content-ops if there is no code), delete this header.
> Facts only in this file. Claude-only notes live in the CLAUDE.md beside it, whose line 1 is
> `@AGENTS.md`. Keep the finished file under 100 lines.

## Scope

- **What this project IS:** <one sentence>
- **What this project is NOT:** <explicit exclusions, prevents scope bleed>
- **Owner:** <who this project is for (your business, or one client), or "not set yet">.
- **North Star:** <the singular outcome that means this project won>
- **Stage:** <idea | sandbox | active | shipped | paused | sunset>, as of <YYYY-MM-DD>.

## Data shape

<!-- Filled by the discovery gate for nextjs-saas and python-pipeline. Delete this section for content-ops and experiment. -->
- **Input:** <shape and source of truth>
- **Payload (output):** <shape and the destination where it lands; the project is complete only when the payload lands there>
- **Integrations:** <external services this depends on, with credential status by key NAME only>

## Structure

- `tools/` : deterministic scripts (API calls, transforms, file ops, DB queries). Look for an existing tool before writing a new one.
- `.claude/skills/` : repeatable procedures (the SOP layer). `.claude/rules/` : rules for this project only. `.claude/agents/` : project subagents, add your own as you need them.
- `.claude/settings.json` : settings for sessions started in this folder (deny rules for `.env`, read-only allow list). Settings do not flow down from parent folders.
- **Naming:** pick one prefix for every new skill, command, agent, or tool you build in this project, and use it every time. Consistency is what makes things easy to find later.
- **Nesting:** a subfolder that needs its own facts gets its own AGENTS.md plus a CLAUDE.md whose first line is `@AGENTS.md`. Files stack, they never override: a deeper file narrows a rule, never cancels one.

## Hard rules

- Start Claude Code inside this folder for work on this project, never in a parent that also holds another client's files.
- Never read, print or copy a real key. Ask before sending, publishing or deleting anything.

## Decisions

<!-- Settled calls, dated one-liners, newest first, cap 10: `YYYY-MM-DD - chose X over Y because Z`.
     Scan before re-opening a decided question. Deep rationale goes wherever you keep long-term notes. -->
- <YYYY-MM-DD> - <seeded at scaffold with the stack-profile choice>

## Stack profile

<!-- Keep exactly ONE profile block. Delete the other three, marker comments included. -->

<!-- PROFILE:nextjs-saas -->
### Profile: Next.js / SaaS (default for anything web)

- **Stack facts come from `package.json` and the code, never from this template.** After the app scaffold lands, record here: framework and version, styling, DB and auth, deploy target.
- **Gate:** `npx tsc --noEmit` plus your test runner's run command plus `npm run build`. If NO test framework is configured, the gate is just `npx tsc --noEmit && npm run build`; never assume vitest or jest exist. Pin the exact full command under Commands once `package.json` exists.
- Testing tier 1 (production SaaS): new API routes and lib logic get coverage proportionate to risk; every bug fix and remediated review finding gets a pinning test.
- Deploy: pick one host and stick with it. Validate all external input at the boundary; handle errors explicitly, never swallow them.
<!-- /PROFILE -->

<!-- PROFILE:python-pipeline -->
### Profile: Python pipeline

Separates probabilistic reasoning from deterministic execution:

- **`workflows/`**: markdown SOPs (objective, required inputs, which tools to call, expected outputs, edge cases). Update them as you learn; never create or overwrite one without asking.
- **`tools/*.py`**: deterministic scripts do the actual work. On failure: read the full error, fix, retest (ask before re-running paid API calls), record the lesson in the workflow.
- **`.tmp/`**: disposable intermediates only, regenerated as needed, never committed.
- **Link handshake (before any logic):** probe every integration listed under Data shape with a minimal script in `tools/`, record pass/fail per service in the workflow. A broken link halts the build until green.
- Deliverables land wherever your source of truth is (a database, a doc, a sheet); local files are working state only.
- **Gate:** run the pipeline against real input and read the logs and output. Check idempotency and the failure path by hand (what happens on empty input, missing env, non-zero exit).
<!-- /PROFILE -->

<!-- PROFILE:content-ops -->
### Profile: Content / ops (no application code)

- For content systems, docs, playbooks, configs. No code gate.
- **Verify mechanically:** `python3 -m json.tool` for JSON, `plutil -lint` for plists, `bash -n` for shell, render the markdown.
- Deliverables live wherever your source of truth is; this repo holds sources, prompts, and working state.
- `tools/` still holds any deterministic helper scripts; verify them by running against real state.
<!-- /PROFILE -->

<!-- PROFILE:experiment -->
### Profile: Experiment (throwaway spike)

- Same-day disposable work. No gate, no ceremony, minimal scaffold (this file, the CLAUDE.md wrapper, .gitignore).
- The moment it stops being throwaway, promote it: rerun the jah-new-project-lite skill against this folder with a real profile.
<!-- /PROFILE -->

## Commands

TODO: fill in dev / test / deploy commands, including the pinned gate, once the stack is scaffolded.

## Secrets (facts)

- Real keys for this project live only in `.env` in this folder. It is gitignored, and this folder's `.claude/settings.json` makes Claude Code refuse to read it with its own tools and common shell commands (not a wall around every script).
- `.env.example` lists the key NAMES only and is committed. Refer to keys by name in chat, docs and screenshots.
- Never copy this `.env` into another client's folder.

## Brand

- If this project has a brand, style guide, or voice doc, note where it lives here once you know.
  Skip this whole section if it does not apply to this project.

## Memory

- `lessons.md` : one line per correction. Append after any correction; read it at the start of a new job.
- `HANDOFF.md` : session state, newest block first. In a jah-workspace-blueprint workspace it is the one at the workspace root; in a standalone folder, create it here the first time you stop mid-job.

## Pointers

- The workspace map is the root AGENTS.md of the workspace this project lives in.
- If you keep engineering standards or reference docs, note where they live here.
- If you keep plans and playbooks, note where they live here.
- If you keep a notes vault or second brain, note where it lives here.
- This project's repo: `git remote -v`. Live/dashboard URLs are private: keep them out of this file.
