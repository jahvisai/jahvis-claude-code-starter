# JAHVIS Claude Code Starter

Free, ready-to-use files for [Claude Code](https://claude.com/claude-code): CLAUDE.md templates, a safe folder scaffold, session files, slash commands and agents. Built for business owners, not programmers. Part of the JAHVIS AI community: https://www.skool.com/jahvis-ai

## What's inside

| Folder | What it is |
|---|---|
| `claude-md-templates/` | Fill-in-the-blank templates: `freelancer`, `personal-brand`, `small-business`. Each is an `AGENTS.md` (your facts) plus a thin `CLAUDE.md` (line 1 is `@AGENTS.md`). |
| `project-scaffold/` | A clean project or client folder: AGENTS.md, CLAUDE.md, lessons.md, safe `.gitignore`. |
| `non-coder-starter/` | A business process run through Claude: workflows, tools, house rules. |
| `rules-example/` | A rule that loads only for one client's files. |
| `proof/` | `CODE-WORD-TEST.md`: how to prove your CLAUDE.md actually loaded. |
| `settings-and-rules/` | Example global and project settings, rules, and a `.env` example. |
| `session-files/` | The "canary" CLAUDE.md, HANDOFF and RISKS templates, `/clear` vs `/compact` guide. |
| `commands/` | A goal-contract command (install it as a skill) and a bank of prompts to copy. |
| `agents/` | Three starter agents and a model-picking cheat sheet. They go in `.claude/agents/`. |

## Use a template in 4 steps

1. Get this repo onto your computer (once):
   ```bash
   git clone https://github.com/jahvisai/jahvis-claude-code-starter.git ~/jahvis-claude-code-starter
   ```
2. `cd` into ONE real project or client folder (never your home folder).
3. Copy a template in. It never overwrites a file you already have:
   ```bash
   bash ~/jahvis-claude-code-starter/install.sh small-business
   ```
4. Open `AGENTS.md`, replace every `<angle-bracket placeholder>`, delete the `>` lines, start Claude Code in the folder, and run the code-word test in `proof/CODE-WORD-TEST.md`.

## How Claude Code reads these files (the short version)

- **Instruction files STACK.** `~/.claude/CLAUDE.md`, the CLAUDE.md in a folder above you, and the one in your project are all added together. Nothing overrides anything; the closest file is read last. If two files disagree, remove the conflict.
- **Settings have a PECKING ORDER.** For one setting, local beats project beats your global file. Lists such as `permissions.allow` and `deny` add up instead of replacing each other.
- **`CLAUDE.local.md` is yours alone.** If you make it by hand, add `CLAUDE.local.md` to `.gitignore` yourself. The scaffold's `.gitignore` already does.
- **Subagents live in `.claude/agents/`** (this project) or `~/.claude/agents/` (every project). Not in `settings.json`.
- **Your own slash commands are skills now.** Put them in `.claude/skills/<name>/SKILL.md` (this project) or `~/.claude/skills/<name>/SKILL.md` (every project). A `commands/<name>.md` file still works; if both exist, the skill wins.
- **Prove it loaded:** type `/memory` in a fresh session to list every loaded file, and `/context` to see what each one costs.

## Install the goal-contract command as a skill

```bash
mkdir -p ~/.claude/skills/goal-contract
cp ~/jahvis-claude-code-starter/commands/goal-contract.md ~/.claude/skills/goal-contract/SKILL.md
```

Start a fresh Claude Code session and type `/goal-contract` plus a one-line job.

## Get updates without losing your edits

Your folders hold copies. This repo stays untouched, so updating it never touches your files:

```bash
cd ~/jahvis-claude-code-starter && git pull
```

## Safety

Nothing here runs by itself. There is no install script that downloads and executes code from the internet: `install.sh` only copies files, and you can read it first. Never put real keys, passwords or client data in a file you push to GitHub.

## Learn how to use all of this

The lessons live in the JAHVIS AI community: https://www.skool.com/jahvis-ai (course 03, Claude Code).

MIT licensed. Use it, change it, make it yours.
