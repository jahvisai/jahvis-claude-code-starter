# Annotated example: what each part of an AGENTS.md is for

This is a teaching copy. Every line that starts with `>` is a note for you, not for Claude.
The business (Ridgeline Landscaping) is invented. The clean version of this file, with no notes,
is `../small-business/AGENTS.md`.

How to read it: each section has a label (what it is) and a reason (why it is there).

---

> **1. ROLE LINE.** One sentence that tells Claude what job it has in this folder.
> **Why:** Claude answers as an office assistant, not as a general chatbot, from the first message.

```
# Ridgeline Landscaping

Role: you are the office assistant for a two-crew residential landscaping company.
```

> **2. UPDATED DATE.** The day a person last checked this file against real life.
> **Why:** you and Claude can both tell when the file is old enough to doubt.

```
Updated: 2026-11-10
```

> **3. THE FACTS.** What the business is, who it serves, what it sells and at what price.
> **Why:** these are the things Claude cannot see in your files and would otherwise guess.

```
## What we sell
- Weekly maintenance: $180 to $320 a month, mowing, edging and seasonal cleanup
- Garden bed install: $1,200 to $4,500, design, soil, plants and mulch
- Pricing rules: always give a range until the walkthrough happens. Quotes are good for 30 days.
```

> **4. ROUTING MAP.** A table with three columns: the need, the path, and the rule for that path.
> **Why:** Claude opens the right file on the first try instead of searching the whole folder.

```
## Routing map

| Need | Path | Rule |
|---|---|---|
| Who is booked where | `crew-calendar.csv` | Read it before naming any date. |
| How to quote a new inquiry | `workflows/quote_new_client.md` | Follow the steps in order. |
| New files with no home yet | `inbox/` | Park it there and tell me. |
```

> **5. PLACEMENT.** Where each kind of new file goes, and what it is named.
> **Why:** new work lands in the same place every time, so you can find it next month.

```
## Placement
- New quote: this year's folder in `quotes/`, named client then date
- Anything unclear: `inbox/`
```

> **6. HARD RULES.** A short list of things that must never happen, each with its reason.
> **Why:** a rule with its reason is followed better, and Claude can apply it to cases you did not list.
> Keep this list short. A rule that truly can never break belongs in a hook, not in a sentence.

```
## Hard rules
- Never promise a start date before checking `crew-calendar.csv`, because Crew B books out
  three weeks and a missed date loses the job.
- Never send anything to a real person without my yes, because I sign every message that
  leaves this office.
```

> **7. DECISIONS.** Dated one-liners: what you decided and why.
> **Why:** Claude stops re-suggesting the thing you already tried and dropped.

```
## Decisions
- 2026-10-07: quotes are good for 30 days. Material prices moved too much to hold them longer.
- 2026-09-12: stopped quoting by phone. Every quote now follows a walkthrough.
```

---

## And the CLAUDE.md that sits beside it

> **LINE 1 IS `@AGENTS.md`.** That one line pulls the whole facts file in.
> **Why:** other AI tools read `AGENTS.md` too, so you keep one set of facts, not two.
> Your `CLAUDE.md` looks almost empty. That is correct. Open `AGENTS.md` to read or change
> your instructions. When Claude updates your rules, the change shows up in `AGENTS.md`.

```
@AGENTS.md

# Claude-only habits
- When I correct you, add the correction to AGENTS.md as a one-line rule with its reason,
  then tell me what you added.
```

## Length

Aim for under 120 lines, never over 200. The clean version of this example is 72 lines.
