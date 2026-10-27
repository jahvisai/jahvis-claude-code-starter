# Model tiering, for one person with one plan

Every agent seat you build gets to pick which model it runs on. This is not
about pricing tiers or which plan you're subscribed to, it's about matching
the DIFFICULTY of a seat's actual job to how much reasoning it genuinely
needs. Get this wrong in one direction and you overpay in time and cost for
routine work; get it wrong in the other and you under-power the one seat
whose whole job is catching mistakes.

## The three tiers, and what each is actually for

**Toughest tier (in Claude Code today: Opus).** Reserve this for seats where
being wrong is expensive and where the reasoning is genuinely hard:
planning, architecture decisions, debugging a subtle failure, and, most
importantly, the VERIFY seat in any build-and-check pair. Finding a mistake
usually takes more reasoning than avoiding one in the first place, that is
why the review seat earns the better model even when the seat that did the
writing didn't need it.

A step above Opus exists (the `fable` model). It is opt-in, can bill usage credits, and you do not need it for a subagent roster.

**Workhorse tier (in Claude Code today: Sonnet).** This is where almost all
of your day-to-day work belongs: implementation from a plan you've already
written, research, exploring a codebase or a document, drafting from a
brief, most seats in a multi-agent team. If you're not sure which tier a
seat needs, start here, it's built for volume and it's good.

**Bulk tier (in Claude Code today: Haiku).** Mechanical, well-specified,
repetitive work where the task is so clearly defined that a lighter model
won't need to backtrack: renaming a batch of files, extracting the same
piece of information from many documents, reformatting, scanning a log for
one pattern. If a task needs judgment calls partway through, it's not a
bulk-tier task.

## The rule that matters most

**The seat that BUILT something should never be the same seat that APPROVES
it.** This is true whether it's one seat or three: a chat thread reviewing
its own draft in the same conversation is not a real review, it already
knows what it meant to say. A genuinely separate agent seat, with a fresh
context that never saw the draft get written, catches things a
self-review never will.

If you build nothing else from this course, build that: one seat writes,
a DIFFERENT seat checks, and the checking seat runs on your best available
model.

## Sizing this for one person

You do not need a large roster to get the benefit. A single verify-seat
checking your own work before you ship it is already the whole pattern.
Add a second seat (research, or draft) only when you actually have a
recurring task with a second distinct step in it, not because more seats
sounds more impressive.

**A realistic ceiling for one person with no dedicated reviewer is two to
four seats running at once, each touching separate files.** Past that,
you personally can no longer review everything each seat produced, and
you're just trusting output instead of checking it, which defeats the
point of having a verify seat in the first place. Run seats in waves:
finish and check one wave completely before starting the next, never open
a second wave while the first is still unverified.

## Applying it to the three example seats in this kit

- `research-seat.md`: workhorse tier. Pulling and summarizing real
  information is exactly the kind of volume work the middle tier is built
  for.
- `draft-seat.md`: workhorse tier. Writing a first draft from a finished
  brief is implementation work, not a hard judgment call.
- `verify-seat.md`: toughest tier. It is the one seat whose entire job is
  catching what the other two missed, which is precisely where the extra
  reasoning power earns its cost.
