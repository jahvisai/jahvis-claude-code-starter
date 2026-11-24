---
name: jah-session-setup
description: One-time setup for the session tools. Asks one question (what Claude should call you), adds your name line to your global rules file, makes HANDOFF.md, and turns on the handoff reminder hook. Use for "set up my sessions", "run session setup", "/jah-session-setup", or the first time someone uses the session kit.
---

# /jah-session-setup: set up the session tools, once

The person may be new to all of this. Use short, plain words. Do the steps in order.
Keep a list of every change you make, for step 6.

The kit lives in `~/jahvis-claude-code-starter`. This skill's own folder has `hooks/` and `scripts/`.
Find this skill's folder first: it is `~/.claude/skills/jah-session-setup` if installed there,
otherwise `~/jahvis-claude-code-starter/.claude/skills/jah-session-setup`. Call it SKILL_DIR below.

## 1. Ask one question

Ask only this: "What name should Claude call you?" Wait for the answer. Call it NAME.

## 2. Find this folder's rules file

Look at `CLAUDE.md` in the folder this session was opened in (the project folder).
- If its only real line is `@AGENTS.md`, the rules file is `AGENTS.md`.
- Otherwise (or if there is no CLAUDE.md), the rules file is `CLAUDE.md`.
Say in one line which one you picked and why. Change nothing in it now. Use it later when the person adds project rules.

## 3. Add the name line to the global rules file

The file is `~/.claude/CLAUDE.md` (on Windows: `%USERPROFILE%\.claude\CLAUDE.md`).
1. If it already has a line with "every single time you reply" or "start every reply with", skip this step and say so.
2. Otherwise add this line at the very END of the file, with one blank line before it. Change nothing else.
   Make the file if it does not exist.

   ```
   Call me NAME every single time you reply. (If a reply stops opening with my name, you have stopped following this file: I will start a new session.)
   ```
   (Put the real name in place of NAME.)

## 4. Make HANDOFF.md

If the project folder has no `HANDOFF.md`, copy `~/jahvis-claude-code-starter/session-files/HANDOFF.template.md` to `HANDOFF.md` there.
If it already exists, leave it alone.

## 5. Turn on the handoff reminder

1. Run the dry run first and show the person what will change:
   `python3 "SKILL_DIR/scripts/settings_merge.py" --dry-run`
2. Then run it for real:
   `python3 "SKILL_DIR/scripts/settings_merge.py"`
   It copies the hook to `~/.claude/hooks/`, backs up `~/.claude/settings.json` to
   `settings.json.bak-<date>`, and adds the hook without removing any you have.
   (On Windows, use `python` if `python3` is not found.)
3. If it says "Stopped", show the person the message and do not edit settings.json by hand.

## 6. Tell the person what changed and how to undo it

Print a short list, one line per change, each with its undo:
- Name line in `~/.claude/CLAUDE.md`. Undo: delete that last line.
- `HANDOFF.md` made (if you made it). Undo: delete the file.
- Reminder hook on. Undo: `python3 "SKILL_DIR/scripts/settings_merge.py" --uninstall`
  (or copy the `settings.json.bak-<date>` file back over `settings.json`).

Then say: "Start a new session so the changes load: in the desktop app click + New (in the terminal, type /clear). When work is done, say: wrap up."
