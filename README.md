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
| `commands/` | A goal-contract slash command and a bank of commands to copy. |
| `agents/` | Three starter agents and a model-picking cheat sheet. |

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
