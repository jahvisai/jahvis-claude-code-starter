---
name: jah-session-setup
description: One-time setup for the session tools. Asks one question (what Claude should call you), adds your name line to your global rules file, makes HANDOFF.md, and makes sure the handoff reminder is on exactly once. Use for "set up my sessions", "run session setup", "/jah-session-setup", or the first time someone uses the session tools.
---

# /jah-session-setup: set up the session tools, once

The person may be new to all of this. Use short, plain words. Do the steps in order.
Keep a list of every change you make, for step 6.

## 0. Find out how these tools were installed

This skill's folder is: `${CLAUDE_SKILL_DIR}`
Call it SKILL_DIR below. It holds `hooks/` and `scripts/`.
The plugin folder is: `${CLAUDE_PLUGIN_ROOT}`

- If the plugin folder line shows a real folder path, the tools came in as the **plugin**
  (jah-session-tools). The plugin already turns the reminder on by itself. Call this PLUGIN MODE.
- If it still shows the text `${CLAUDE_PLUGIN_ROOT}` (a dollar sign and curly brackets), the tools were
  **copied in by hand** (the older way). Call this COPY MODE.
- If the skill folder line still shows `${CLAUDE_SKILL_DIR}` instead of a folder, look for the folder
  yourself: `~/.claude/skills/jah-session-setup`, then
  `~/jahvis-claude-code-starter/plugins/jah-session-tools/skills/jah-session-setup`. That is COPY MODE.

Say in one line which mode you found.

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

If the project folder already has a `HANDOFF.md`, leave it alone.
Otherwise:
- If `~/jahvis-claude-code-starter/session-files/HANDOFF.template.md` exists, copy it to `HANDOFF.md` in the project folder.
- If not, make `HANDOFF.md` with the title `# HANDOFF` and the four headings the jah-wrap skill uses:
  `### Current state`, `### What is done`, `### What is next`, `### Gotchas and open questions`.

## 5. Make sure the handoff reminder is on, once

The reminder must run once, never twice. (On Windows, use `python` if `python3` is not found.)

**PLUGIN MODE:** do not add anything to `settings.json`. The plugin carries the reminder.
1. Check for an older copy that the hand install put in settings.json:
   `python3 "SKILL_DIR/scripts/settings_merge.py" --uninstall --dry-run`
2. If it says "Nothing to remove", the older copy is not there. Go to step 3 of this list.
3. If it shows a change, run it for real so the reminder does not fire twice:
   `python3 "SKILL_DIR/scripts/settings_merge.py" --uninstall`
   It backs up `~/.claude/settings.json` first and keeps every other hook.
4. Check for older hand-copied skills: `~/.claude/skills/jah-session-setup` and `~/.claude/skills/jah-wrap`.
   If either folder is there, say: "You have an older copy of these tools too. The plugin replaces it.
   Can I delete the old folders so you only see one of each?" Delete them only if the person says yes.

**COPY MODE:**
1. Run the dry run first and show the person what will change:
   `python3 "SKILL_DIR/scripts/settings_merge.py" --dry-run`
2. Then run it for real:
   `python3 "SKILL_DIR/scripts/settings_merge.py"`
   It copies the hook to `~/.claude/hooks/`, backs up `~/.claude/settings.json` to
   `settings.json.bak-<date>`, and adds the hook without removing any you have.
3. If it says "Stopped", show the person the message and do not edit settings.json by hand.
4. Tell the person, in one line: "There is now an easier way to get these tools that updates itself: the
   jah-session-tools plugin. The lesson shows how."

## 6. Tell the person what changed and how to undo it

Print a short list, one line per change, each with its undo:
- Name line in `~/.claude/CLAUDE.md`. Undo: delete that last line.
- `HANDOFF.md` made (if you made it). Undo: delete the file.
- PLUGIN MODE: "The reminder comes with the plugin." If you removed an older copy, say so. Undo: copy the
  `settings.json.bak-<date>` file back over `settings.json`. To turn the whole plugin off: in the desktop
  app click + next to the prompt box, then Plugins, then Manage plugins (in the terminal:
  `claude plugin disable jah-session-tools@jahvis`).
- COPY MODE: Reminder hook on. Undo: `python3 "SKILL_DIR/scripts/settings_merge.py" --uninstall`
  (or copy the `settings.json.bak-<date>` file back over `settings.json`).

Then say: "Start a new session so the changes load: in the desktop app click + New (in the terminal, type /clear). When work is done, say: wrap up."
