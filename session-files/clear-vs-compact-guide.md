# When to /clear vs /compact: a plain-English guide

Claude Code has a limited amount of working memory (its "context window"). As
a session runs longer, it fills up with everything that's happened: every
file it read, every command it ran, every message you sent. On current models it holds about a million tokens,
and Claude Code compacts on its own just before it fills, but long before
that your instructions get buried. Eventually you have to do something about
that, and there are two very different tools for
it.

## The two commands

| Command | What it actually does | What it costs |
|---|---|---|
| `/compact` | Summarizes the current session into a shorter version and keeps going in the same conversation | Carries a summary of everything so far, plus your CLAUDE.md and the files it changed most recently, so a session you keep compacting keeps dragging old work along |
| `/clear` | Starts a new, empty conversation (the old one is saved, and `/resume` can reopen it) | The new session knows nothing that wasn't written down somewhere durable (a file, a commit, a HANDOFF.md), but you're back at the cheapest possible starting point |

## The rule of thumb

**One unit of work per session, then `/clear`.** A "unit of work" is
something you could commit or consider genuinely finished, a feature, a fix,
a piece of content, a completed research task. When you hit that point:

1. Make sure anything worth keeping is actually saved somewhere: committed
   to git, written into a file, or logged in `HANDOFF.md`.
2. Update `HANDOFF.md` with what's done and what's next (see the template in
   this kit).
3. Run `/clear`, not `/compact`.

**Use `/compact` only when you're genuinely still mid-task** and the session
has grown long, but stopping now would lose useful momentum, mid-debugging
session, for example, where you'd otherwise have to re-explain the whole
investigation from scratch.

## Why this matters more than it sounds like it should

Everything a session has already read gets re-read by the model on every
turn that follows. That means cost and slowdown grow much faster than the
number of things you've asked it to do, a long session that keeps
`/compact`-ing forward carries more and more dead weight every single reply,
even about things that have nothing to do with what you're currently
working on.

A fresh `/clear` resets that cost back to the starting floor: the system
prompt, your CLAUDE.md files and the tool list. If your `HANDOFF.md`
is good, the next session picks up just as fast as the old one would have,
minus all the accumulated baggage.

## The tell that you're doing it wrong

If you find yourself running `/compact` far more often than `/clear`, that's
usually a sign you're treating one long session as the whole project instead
of breaking it into finished units. A single very long session (hundreds of
turns) usually costs many times more than the same work done as several
shorter, cleanly-closed sessions, even though the total amount of work is
identical.

## How the canary rule fits in

The canary trick in this kit's `canary-CLAUDE.md` gives you an early warning
sign for the SAME underlying problem: once your instructions are buried under
a long session, or Claude is working from one summary too many, it quietly
stops following your rules. The canary is how you notice; `/clear`
at the right moment is how you prevent it from happening as often.
