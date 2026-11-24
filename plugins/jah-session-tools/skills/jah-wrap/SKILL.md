---
name: jah-wrap
description: Close a piece of work. Brings HANDOFF.md up to date, saves and uploads the changed files if the folder uses git, then prints the one line to paste into a new session. Use for "wrap up", "wrap this", "/jah-wrap", "save my progress", "I am done for now", or when the handoff reminder says the session is heavy.
---

# /jah-wrap: close this piece of work

The person you help may be new to all of this. Use short, plain words. Do every step in order.

## 1. Update HANDOFF.md

1. Look for `HANDOFF.md` in the top folder of this project (the folder this session was opened in).
2. If it is missing, copy `~/jahvis-claude-code-starter/session-files/HANDOFF.template.md` to `HANDOFF.md`.
   If that template is not there either, make the file with the four headings below.
3. Add a new block at the TOP, under the title, with today's date. Newest block always goes on top.
   Keep older blocks below it. Use these four headings:

   ```
   ## <YYYY-MM-DD>: <what this work was, in five words>
   ### Current state
   One or two sentences: what is true right now.
   ### What is done
   - Only things that are finished and checked.
   ### What is next
   1. The very next step, clear enough to start without asking.
   ### Gotchas and open questions
   - Anything that tripped you up, or a choice still waiting on the person.
   ```
4. Write only true things. If you did not check it, do not put it under "What is done".

## 1b. Keep the "Waiting on you" list right

This list holds questions the person has not answered yet. It sits near the top of HANDOFF.md, right
under the title and above the dated blocks, so the next session sees it first.

1. Read the `## Waiting on you` list if it is there. For each item the person has now answered (in this
   session, or by saying so), delete that line. Put the answer in this block's "What is done" or
   "What is next". If the list is now empty, delete the heading too.
2. Look at this session: did you ask the person anything they have not answered yet? For each one, add a
   line under `## Waiting on you` (make the heading if it is missing):

   ```
   - [ ] <the question, one line> (asked <YYYY-MM-DD>; blocked: <what cannot go on until it is answered>)
   ```
3. Never add a question that was answered. Never delete one that was not.
4. If anything is waiting, say in one line: "N questions are waiting on you. They are at the top of HANDOFF.md."

## 2. Save and upload the work (only if this folder uses git)

1. Run `git rev-parse --is-inside-work-tree`. If it fails, say in one line:
   "This folder does not use git, so there is nothing to upload. Your files are saved on this computer." Then go to step 3.
2. Run `git status --short` and sort the list into two groups:
   - files YOU changed in this session (including HANDOFF.md),
   - files you did NOT change.
3. Add only your own files, by name: `git add -- <file> <file>`. Never use `git add .` or `git add -A`.
4. If there are files you did not change, list them and ASK: "These files changed too, but not by me. Should I save them as well?" Add them only if the person says yes.
5. Commit with a short message that says what the work did: `git commit -m "<what changed>"`.
6. If `git remote` prints nothing, say: "Saved on this computer. This folder has no online copy set up, so nothing was uploaded." Then go to step 3.
7. Otherwise run `git push`. Then prove it landed: run `git fetch` and `git status -sb`.
   It must not say "ahead". If the push failed or it still says "ahead", tell the person plainly
   what the error said and stop. Never say it uploaded when it did not.

## 3. Hand off to a fresh session

End your reply with these lines, exactly:

1. "All saved. Start a new session now: in the desktop app click + New (in the terminal, type /clear)."
2. "Then paste this as your first message:"

```
Read HANDOFF.md and tell me what is next.
```
