---
name: jah-setup-interview
description: Set up a new business workspace from this starter by interview, or fill in a workspace folder the person already has. Asks at most 7 questions, one at a time, saves each answer to a file before the next question, then fills the workspace AGENTS.md, the context/ folder and connections.md from the saved answers. Use for "set up my workspace", "run the setup interview", "/jah-setup-interview", or the first time someone opens this starter folder and asks what to do.
---

# /jah-setup-interview: build a workspace from seven saved answers

You are setting up a workspace for a business owner who may never have used a terminal.
Use plain words. Ask one question at a time. Write nothing into their workspace files until
step 4.

The answers file is the record, not this chat. Save each answer to it before you ask the
next question, so a closed window or a full session loses nothing.

## 1. Find the workspace folder

1. The workspace folder is `~/work` unless the person names another one. Never use the home
   folder, Desktop, Documents or Downloads.
2. Look at the folder before you copy anything. It is one of three cases:

   | The folder | Case | What you do |
   |---|---|---|
   | Is missing or empty | New workspace | Step 3 |
   | Has an `AGENTS.md` or `CLAUDE.md` at its top and a `context/` folder | Existing workspace | Step 4 |
   | Holds other files | Not a workspace | Stop and ask for a new folder name |

3. New workspace: create the folder, then run the copy from inside it. The copy never
   overwrites a file:

   ```bash
   mkdir -p ~/work && cd ~/work && bash ~/jahvis-claude-code-starter/install.sh workspace
   ```

4. Existing workspace: say in one line that you will fill in the folder they have and
   overwrite nothing. Do not run the install. Copy in only the pieces below, and each one
   only if it is missing:

   ```bash
   cd ~/work && S=~/jahvis-claude-code-starter/workspace-root && mkdir -p context decisions .claude/skills
   for f in connections.md decisions/log.md context/business-overview.md context/customer-personas.md context/offers-and-pricing.md context/brand-voice.md; do [ -e "$f" ] || cp "$S/$f" "$f"; done
   [ -e .claude/skills/jah-grill ] || cp -R "$S/.claude/skills/jah-grill" .claude/skills/
   ```

   Never add a department folder the person does not have.

5. Create `setup-answers.md` in the workspace folder with this header, before question 1:

   ```
   # Setup answers
   Started: <today, from the shell: date +%F>
   Status: in progress
   Workspace: <new or existing>
   Next question: 1
   ```

6. Tell the person in one line where the workspace is and that every answer is saved to
   `setup-answers.md`.

If `setup-answers.md` already exists there, read it and continue from its "Next question"
line. Do not ask an answered question again.

## 2. The seven questions

Ask them in this order. Skip one only when the person says to; record it as skipped.

| # | Question | Where the answer goes in step 4 |
|---|---|---|
| 1 | What is the business called, and what does it do, in one or two sentences? | `context/business-overview.md`, the title of `AGENTS.md` |
| 2 | Who is your best kind of customer, and what problem do they come to you with? | `context/customer-personas.md` |
| 3 | What do you sell, and what does each thing cost? | `context/offers-and-pricing.md` |
| 4 | Which of these areas do you work in every week: marketing, sales, operations, finance, clients? | the department table in `AGENTS.md` |
| 5 | Paste two or three things you wrote yourself: a post, an email to a customer, a sales message. Paste them, do not describe them. | `context/voice-samples.md` and `context/brand-voice.md` |
| 6 | For each area you kept, which app or tool do you use today? | `connections.md` |
| 7 | What is the one thing Claude must never do without asking you first? | the hard rules in `AGENTS.md` |

Rules for asking:

- Question 4 is a choice, so give a recommendation ("most one-person businesses start with
  marketing, sales and finance") and label it as a recommendation.
- Questions 1, 2, 3, 5 and 7 are facts about their business. Ask them neutrally. Never
  offer a made-up answer and never save your guess as their answer.
- Question 5 needs real pasted text. If the person describes their voice instead, ask once
  more for a paste. If they have nothing to paste, record "no samples yet" and leave
  `brand-voice.md` as the unfilled template.
- Never ask for a password, key or login. Question 6 wants tool names only.
- In an existing workspace, read before you ask. Open the file each answer goes to. If it
  already holds a real answer (not a `<placeholder>`), show that answer in one line and ask
  "Keep this, or change it?". Save a kept answer as "kept" with what the file says. The
  first setup usually answered questions 4 and 7 already.

## 3. After every answer, before the next question

1. Append the answer to `setup-answers.md` under `## Q<n>`, in the person's own words. Save
   pasted voice samples exactly as pasted.
2. Update the "Next question" line.
3. Read the entry back from the file.
4. Then ask the next question.

If the save fails, say so and fix it before you ask anything else.

## 4. Fill the workspace from the answers file

Read `setup-answers.md` from disk and work only from it.

In an existing workspace, change only what the answers changed. Edit `AGENTS.md` in place and
never rewrite it. Skip any item whose answer is "kept". Never delete a folder, so skip item 2.
Never replace text the person wrote with a placeholder.

1. `AGENTS.md`: put in the business name and today's date, keep only the departments from
   answer 4 in both tables, write answer 7 as the first hard rule, delete the `>` lines.
   Keep it under 100 lines.
2. Delete each department folder the person did not pick, only if it still holds nothing
   but its template `AGENTS.md` and `CLAUDE.md`. Always keep `context/`, `inbox/`,
   `archive/` and `decisions/`.
3. `context/business-overview.md`, `customer-personas.md`, `offers-and-pricing.md`: fill
   from answers 1 to 3. Leave a `<placeholder>` wherever the person gave no answer. Never
   invent a price, a customer or an offer.
4. `context/voice-samples.md`: the pasted samples, word for word. `context/brand-voice.md`:
   fill its four lines from the samples, and quote one sentence from them as the "sounds
   exactly like us" line.
5. `connections.md`: one row per kept area with the tool from answer 6. Set every "How
   Claude reaches it" cell to "not connected yet". Connecting comes later.
6. `decisions/log.md`: add one dated entry, "Workspace set up", listing the departments
   kept and the never-do rule.
7. Set `Status: complete` in `setup-answers.md`.

## 5. Show the result and hand over

1. List every file you filled and every placeholder still open.
2. Tell the person to open a new session in the workspace folder (not this starter folder)
   and ask: "What is this workspace, and where does a new client go?" A new session reads
   the files from disk, which proves they work.
3. Say that `/jah-grill` now exists in their workspace for thinking a plan through.

## Scope

This skill writes only inside the workspace folder. It never pushes to GitHub, never
changes the starter folder and never edits settings outside the workspace.
