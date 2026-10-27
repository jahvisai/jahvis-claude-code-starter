# Prove an instruction file actually loaded

A file sitting in the right folder proves nothing. Claude can sound sure about its own setup and
still be wrong. These three checks prove what really loaded. Run them in a NEW session started in
the folder you want to test, and again after any change, move or rename.

## 1. The code-word test (works for everyone)

1. Open the AGENTS.md you want to test and add one made-up line, for example:
   `Code word for this folder: blue-heron`
2. Close Claude Code (`/exit`), then start it again inside that same folder.
3. Ask: "What is the code word for this folder?"
4. The right word means the file loaded. A guess, or "I don't know", means it did not.
5. Delete the line when you're done. Test an area folder and a project folder separately.

## 2. /context

Type `/context` in the session and look under Memory files. That list is what actually loaded,
which can differ from what Claude says when it describes its own setup. `/memory` opens the files.

## 3. The load log (needs the load-log hook)

The `load-log.py` hook writes one line per loaded instruction file to `.claude/loaded.log`. The
workspace kit's optional hooks install it for every session (log at your workspace root); the
03.2.2 settings kit installs it for one folder (log in that folder). Start a new session, then
open the log. Each line shows the time, the file's type, why it loaded, and its path. If a
folder's AGENTS.md is missing from the log, the `@AGENTS.md` pointer in that folder's CLAUDE.md is
missing, or you started in the wrong folder. The kit's `.gitignore` keeps the log out of git.

## What each result means

| What you see | What it means | Fix |
|---|---|---|
| Right code word | The file loaded | Nothing |
| Wrong word or "I don't know" | The file did not load | Check that CLAUDE.md line 1 is exactly `@AGENTS.md`, and that you started inside this folder |
| Right word only after Claude opened the file | It read the file during the chat, it did not load at start | Same fix as above |
| File missing from /context | Not loaded | Same fix as above |

Trust the code word and the load log, not Claude's description of itself.
