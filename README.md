# JAHVIS Claude Code Starter

Free, ready-to-use files for [Claude Code](https://claude.com/claude-code): CLAUDE.md templates, a safe folder scaffold, session files, slash commands and agents. Built for business owners, not programmers. Part of the JAHVIS AI community: https://www.skool.com/jahvis-ai

## What's inside

| Folder | What it is |
|---|---|
| `claude-md-templates/` | Fill-in-the-blank templates: `freelancer`, `personal-brand`, `small-business`. Each is an `AGENTS.md` (your facts) plus a thin `CLAUDE.md` (line 1 is `@AGENTS.md`). |
| `claude-md-examples/` | Three finished examples, one per template, each an invented business with every blank filled, plus one annotated `AGENTS.md` that labels each section and says why it is there. Read these, copy a template. |
| `.claude/skills/jah-setup-interview/` | The setup interview. Run `bash ~/jahvis-claude-code-starter/install.sh skill`, open a new session in your work folder and type `/jah-setup-interview`: at most seven questions, each answer saved before the next, then your workspace `AGENTS.md`, `context/` and `connections.md` are filled for you. |
| `workspace-root/` | The top of your workspace: a root map, a shared `context/` folder (overview, offers and pricing, customer personas, brand voice), one folder per department (marketing, sales, operations, finance, clients), `connections.md` (the tool each business area uses and how Claude reaches it), `decisions/log.md` (dated decisions, added to and never edited) and the `/jah-grill` skill (Claude interviews you about a plan and saves every answer). Install with `bash install.sh workspace`. |
| `project-scaffold/` | A clean project or client folder: AGENTS.md, CLAUDE.md, lessons.md, safe `.gitignore`. |
| `non-coder-starter/` | A business process run through Claude: workflows, tools, house rules. |
| `rules-example/` | A rule that loads only for one client's files. |
| `proof/` | `CODE-WORD-TEST.md`: how to prove your CLAUDE.md actually loaded. |
| `settings-and-rules/` | Example global and project settings, rules, and a `.env` example. |
| `session-files/` | The "canary" CLAUDE.md, HANDOFF and RISKS templates, `/clear` vs `/compact` guide. |
| `commands/` | A goal-contract command (install it as a skill) and a bank of prompts to copy. |
| `agents/` | Three starter agents and a model-picking cheat sheet. They go in `.claude/agents/`. |

## Set up a whole workspace by interview (works with no work folder, or one you already have)

1. Get this repo onto your computer (once):
   ```bash
   git clone https://github.com/jahvisai/jahvis-claude-code-starter.git ~/jahvis-claude-code-starter
   ```
   Always clone into your home folder with that exact command. Do not clone into a folder that already has files: git refuses, and a clone placed inside your work folder hides the skill.
2. Install the interview so it works from any folder:
   ```bash
   bash ~/jahvis-claude-code-starter/install.sh skill
   ```
3. Open a NEW Claude Code session in your work folder (the one you want filled in, for example `~/work`), not in this repo. Type `/jah-setup-interview` and answer the questions. Have two or three things you wrote yourself ready to paste (a post, a customer email): that is how Claude learns your voice.
4. Already have a work folder? The interview fills in that folder instead. It adds what is missing (`connections.md`, `decisions/log.md`, your voice samples) and overwrites nothing.
5. Open a new session in the workspace (`~/work` by default) and ask: "What is this workspace, and where does a new client go?"

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
4. Open `AGENTS.md`, replace every `<angle-bracket placeholder>` (see a finished one in `claude-md-examples/`), delete the `>` lines, aim for under 120 lines and never over 200, start Claude Code in the folder, and run the code-word test in `proof/CODE-WORD-TEST.md`.

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

## What to add later, and what never to add

Start with what is here. Add a piece only when the work asks for it.

| Add this | When |
|---|---|
| A skill | You have asked Claude for the same job three times |
| A connection to a tool | Work in that area keeps stopping because Claude cannot see the tool. Write it in `connections.md`, start it read only |
| A department folder | You open that kind of work every week |
| A rule | You have corrected Claude on the same thing twice |
| A subagent | One job keeps filling your session with reading |
| A scheduled job | You have run the job by hand three times and it came out right each time |

Never add these:

- A real key, password or login in any file in your workspace. Keys live in one `.env` per project, and `.env` stays out of GitHub.
- Client or lead data in a public repo.
- A second copy of a fact. Prices, customers and voice live in `context/` and nowhere else.
- A skill or plugin you have not read. It is instructions Claude will follow in your name.
- A connection that can write or send before you have tested it read only.
- A job that sends, posts or pays on a schedule without your yes.
- More lines in the root `AGENTS.md` once it passes 100. It loads into every session, so a fact for one department goes in that department.

## Safety

Nothing here runs by itself. There is no install script that downloads and executes code from the internet: `install.sh` only copies files, and you can read it first. Never put real keys, passwords or client data in a file you push to GitHub.

## Learn how to use all of this

The lessons live in the JAHVIS AI community: https://www.skool.com/jahvis-ai (course 03, Claude Code).

Next step for sales work: add a `business` department to your workspace (`~/work/business`, your sales department, with leads, sales, clients and reports). It is not in this repo on purpose, because it is where your lead and client data will live, and that data never belongs in a public repo. The starter folder is attached to the lesson "Create Your Folder Architecture" in the Lead Gen, Sales and CRM Automation course of the same community.

MIT licensed. Use it, change it, make it yours.

Credit: the `/jah-grill` skill is adapted from the `grill-me` skill in Nate Herk's AIS-OS starter kit (https://github.com/nateherkai/AIS-OS, MIT License).
