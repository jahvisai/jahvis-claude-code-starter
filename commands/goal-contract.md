---
description: Turn a raw ask into a Perfectly Prompt Engineered goal contract, then execute against it
argument-hint: [the raw ask, or blank to use the previous message]
---

# /goal-contract

Convert the request into an explicit, verifiable GOAL CONTRACT before doing any
work. The contract is a file on disk, not a paragraph in chat, because it has to
survive a `/clear` and be checkable at the end.

## Step 1: write the contract

Create `.planning/GOAL.md` in the most relevant repo (create the directory if
needed). It MUST contain all nine sections below. A section you cannot fill is a
question for the user, not a section to skip.

1. **The goal in one sentence.** Phrased as the state of the world when it is
   done, from the user's point of view. Not a list of tasks. If the sentence
   contains "and also", it is two goals: split it or pick one.
2. **The audiences.** Who consumes the output, what each one gets, and where
   that artifact physically lives. A deliverable with no named consumer is
   scope you invented.
3. **Definition of Done, per unit.** A table: deliverable, and the CHECK that
   proves it. Every row needs a check that could fail. "Looks good" is not a
   check.
4. **Definition of Done, at the top level.** The same, for the whole thing.
5. **Quality bars.** The standards a deliverable must clear to count. Name
   your own house rules here (tone, formatting, brand voice, anything you
   always want followed without having to say it every time).
6. **Verification protocol.** How each layer is PROVEN. Never accept a
   subagent's or your own self-reported success as done, actually run it and
   look at the output. Name what an adversarial second pass would check.
7. **Explicit non-goals.** What this build will not do. This is the anti-scope-
   creep clause and it is not optional.
8. **Decisions reserved for you.** Only genuine ones: money, scope, anything
   client-facing, anything irreversible. Everything else gets decided and
   reported, not asked.
9. **Open questions.** Anything that would change the work if answered
   differently, each with the DEFAULT to proceed on if unanswered.

## Step 2: check the contract before executing

- Does every Done row have a check that could actually fail?
- Is there a non-goal? If not, you have not bounded it.
- Have you tested every either/or you are about to hand over? Two options you
  never tried to combine (running them one after the other, or one feeding the
  other) is not a real decision, it is an unfinished analysis.
- Are the "reserved for you" items really yours to decide, or are they things
  that could just be decided and reported?
- Could someone with zero context execute against this file alone?

## Step 3: show it, then execute

Open the file so you can actually look at it before agreeing to anything in
it. You cannot approve what you have not seen.

Then execute against the contract. Track progress with a checklist, one item
per Done row. When work finishes, walk the contract row by row and report each
check as PASS, FAIL, or NOT RUN. Never report NOT RUN as done.

## Step 4: close the loop

Append the outcome to the contract file under `## Result`, with the date and
the per-row verdicts. The contract plus its result is the handoff for next
time.

---

Raw ask: $ARGUMENTS
