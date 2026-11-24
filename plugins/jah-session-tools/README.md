# jah-session-tools

Free session tools for Claude Code from the JAHVIS AI community. 2 skills and 3 small checks (hooks).
Needs Python 3 on your computer. Works on Mac, Windows and Linux.

## Install

Paste these 2 commands in a terminal (or ask Claude to run them):

```bash
claude plugin marketplace add jahvisai/jahvis-claude-code-starter
claude plugin install jah-session-tools@jahvis
```

Then start a new session and type `/jah-session-tools:jah-session-setup` once.

## What each tool does, what it changes, how to undo it

| Tool | What it does | What it changes on your computer | How to undo |
|---|---|---|---|
| `/jah-session-tools:jah-session-setup` | Runs once. Asks your name, makes `HANDOFF.md`, and offers the recommended settings. | 1. Adds 1 name line at the end of `~/.claude/CLAUDE.md`. 2. Makes `HANDOFF.md` in your folder. 3. Only if you say yes: adds 3 read-only git rules and 1 desktop notice to `~/.claude/settings.json`. It shows you the exact change first and keeps everything already there. | 1. Delete the name line. 2. Delete `HANDOFF.md`. 3. Say "undo the recommended settings". It takes out only what it added. |
| `/jah-session-tools:jah-wrap` | Ends a piece of work. Updates `HANDOFF.md`, keeps the "Waiting on you" list right, saves and uploads your files if the folder uses git, and gives you the first message for a new session. | Writes `HANDOFF.md`. Makes a git save (commit) and upload (push) of only the files it changed. | Edit `HANDOFF.md` by hand. To take back a save, ask Claude: "undo my last save, safely". |
| Handoff reminder | When a session gets heavy (about 150,000 and 300,000 tokens), Claude suggests a wrap-up at the next stopping point. | Writes tiny marker files in `~/.claude/session-kit/reminder-marks/` so it speaks only once per level. | Turn the plugin off (below). |
| Waiting on you check | When a session starts, it tells you in 1 line if this folder has questions you never answered: from `HANDOFF.md`, or from another session here in the last 3 days. Says nothing when there are none. | Reads `HANDOFF.md` and this folder's session history. When a session ends on a question you never answered, it adds that question to `HANDOFF.md` under "Waiting on you". It only writes if `HANDOFF.md` already exists. | Delete the line from `HANDOFF.md`, or answer it and say "wrap up". |

## The recommended settings, in plain words

1. Claude can run `git status`, `git diff` and `git log` without asking you. They only look; they never change files.
   (Claude Code already lets most read-only git commands run without asking. These rules make sure.)
2. Your computer shows a small notice, "Claude needs you", when Claude is waiting for your yes or your answer.
   Mac uses the built-in notices. Windows uses PowerShell. Linux needs `notify-send` (most desktops have it).

If the desktop app already notifies you and you get 2 notices, say "undo the recommended settings".

## When you have a question waiting

1. If Claude says "Waiting on you: 2 questions...", go back to the session that asked (it is in your session list) and answer there.
2. If that session is gone, ask the new session: "What is waiting on me?" and answer it here.
3. When you say "wrap up", answered questions are taken off the list.

## Turn it all off

Type `/plugin`, find `jah-session-tools`, and turn it off. Or in a terminal:

```bash
claude plugin disable jah-session-tools@jahvis
```

Removing it for good: `claude plugin uninstall jah-session-tools@jahvis`.
The name line and the recommended settings stay until you undo them (see the table).

## Safety

All checks use only the Python standard library. They never block a session: on any error they stay quiet.
No tool sends anything off your computer, except `jah-wrap` uploading your own files to your own git remote.
