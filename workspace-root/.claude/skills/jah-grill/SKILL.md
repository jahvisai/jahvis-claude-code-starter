---
name: jah-grill
description: Interview the user one question at a time about a plan, offer, design or idea, saving every answer to a capture file before the next question so nothing is lost when the session gets long. Use for "grill me", "/jah-grill", "stress-test this plan", "pressure-test my idea", "interview me about X", "get this out of my head", or a discovery session before building something.
---

# /jah-grill: interview one question at a time, save every answer to a file

Goal: move what is in the user's head into one organized markdown file. The file is the
record. The chat is not. A long interview fills the session, and answers held only in the
session get mixed up or dropped, so each answer is written to disk the moment it is given.

Loading this skill does not start an interview. Start when the user asks for one.

## 1. Before the first question

1. Read the `AGENTS.md` of the folder you are in, and only the `context/` files that bear
   on the topic. Reuse facts already written down. Ask about gaps, changes, decisions and
   tradeoffs.
2. Get today's date from the shell: `date +%F`.
3. Create the capture file at `brainstorms/<date>-<topic-slug>.md` in the workspace root
   (create the `brainstorms/` folder if it is missing). Write the header from section 4
   with the goal and an empty "Open items" list.
   - A file with that name already exists: add a time suffix. Never overwrite a capture.
   - The user asks to continue an earlier session: read that file first and continue its
     question numbers.
   - No topic yet: name it `untitled`, mark the goal as pending, ask what to explore, then
     write the topic and goal into the same file.
4. Tell the user in one line where the answers are being saved. Then ask question 1.

## 2. After every answer, before the next question

1. Append one entry to the capture file: the question, the facts and decisions from the
   answer (in the user's words where the wording matters), and any open item with the
   person who can answer it.
2. When an answer changes an earlier one, keep the earlier entry, mark it "replaced by
   Q<n>", and update the summary at the top.
3. Read the saved entry back from the file.
4. Then ask the next question.

One answer per write. If the write fails, say so, keep the answer visible in chat, and fix
the save before collecting another answer.

## 3. How to ask

- One question at a time.
- A decision question comes with a recommended answer, labeled as a recommendation.
- A question about a fact of their business or life is asked neutrally. A guess is never
  saved as their answer.
- Keep four kinds of content apart in the file: confirmed by the user, tentative,
  suggested by Claude, and open.
- Settle the upstream decision before the ones that depend on it.
- If a file in the workspace can answer the question, read it instead of asking. When the
  user hands over a doc, read it and ask only about what is new.
- When the user cannot answer, record an open item with its owner and move on.
- Stop the moment the user says stop. Near the end ask once: "Anything we have not touched?"

## 4. Capture file layout

```
# <Topic>: interview notes
Date: <date>. Goal: <one line>.
Status: in progress | paused | complete
Files read first: <paths, if any>

## Summary and decisions so far
(kept current as answers arrive)

## Questions and answers
### Q1: <topic>
- Asked: <question>
- Confirmed by the user: <facts and decisions>
- Tentative or suggested: <unconfirmed ideas, each labeled>
- Open items: <item, then who can answer>

## Open items
- <item>, owner: <who can answer>
```

## 5. At the end or on a pause

1. Read the whole capture for contradictions and gaps. Mark a conflict as open. The user
   picks between two business facts.
2. Set the status and write the resume point (the next question to ask).
3. Confirmed, lasting facts go into the `context/` file that already owns them, with the
   date. A confirmed decision is added to `decisions/log.md` as a new dated entry.
   Tentative and suggested items stay in the capture until the user confirms them.
4. Recap in chat: the capture path, the files updated, the open items, and the next step.

## Scope

The interview writes the capture file and the context updates the user asked for. It sends
nothing and changes nothing outside the workspace. Passwords and keys are referred to by
name and never written into a capture.

Credit: adapted from the `grill-me` skill in Nate Herk's AIS-OS starter kit
(https://github.com/nateherkai/AIS-OS, MIT License, Copyright (c) 2026 Nate Herk).
