# The Command Bank: paste-ready prompts by business function

Every row below is a complete, ready-to-paste prompt. Copy the whole
"Prompt" cell into Claude Code (swap in your own specifics wherever you see
`[bracketed placeholders]`), and it runs as a real, bounded task instead of
a vague ask. This is the same content as `command-bank.csv`, in table form
for reading, use the CSV if you want to import it into a spreadsheet.

## Marketing and content

| Command | Prompt | When to use it |
|---|---|---|
| Repurpose a long piece | Read `[path or URL to the source content]`. Pull out the 3 strongest standalone ideas, then write one LinkedIn post and one Twitter/X thread for each, in my voice (see my CLAUDE.md for tone). Save each as its own file under `content/repurposed/`. | You wrote one long piece (a blog post, a newsletter, a video transcript) and want it turned into several shorter posts without starting from a blank page each time. |
| Weekly content plan | Look at what I've published in the last 30 days under `content/`. Propose 5 post ideas for next week that do NOT repeat a topic I already covered, each with a one-line angle and the platform it fits best. | Planning content without re-pitching yourself the same idea for the third time. |
| Headline/hook options | Here is a piece of content: `[paste it or point to the file]`. Write 8 different opening hooks for it, each using a different angle (a stat, a question, a contrarian claim, a story opener, and so on). Rank them by how likely they are to stop a scroll. | You have the body of a post but the opening line is the hardest part. |
| Turn a testimonial into content | Here is a piece of customer feedback: `[paste it]`. Turn it into a short case-study style post: the problem they had, what changed, the result, without inventing any detail that isn't in the original quote. | You collect testimonials but never do anything with them. |

## Research

| Command | Prompt | When to use it |
|---|---|---|
| Competitor scan | Research `[competitor name]`'s public positioning: their homepage headline, their pricing page, and their most recent 5 pieces of public content. Summarize what they're claiming, who they seem to be targeting, and one gap I could exploit. Cite sources. | Before writing new positioning or launching something they might already be doing. |
| Vendor comparison | I need `[category of tool, e.g. "email marketing tool"]` for `[the specific need]`. Research the top 3 options, compare them on price, the one feature I actually need, and switching cost from what I use now. Give me a recommendation with your reasoning, not just a feature table. | Before signing up for or switching a paid tool. |
| Market sizing sanity check | I'm considering `[a specific offer or product idea]` for `[the audience]`. Find real evidence this audience actually has this problem and will pay to solve it: forum threads, reviews of competitors, search volume, anything real. Do not just tell me it sounds like a good idea. | Before investing real time building something nobody asked for. |
| Summarize a long document | Read `[path or URL]`. Give me a one-paragraph summary, then the 5 most important facts as bullets, then anything in it that contradicts what I currently believe about `[topic]`. | A report, a long article, or a contract you don't have time to read start to finish. |

## Sales and outreach

| Command | Prompt | When to use it |
|---|---|---|
| Cold outreach draft | Here's a lead: `[name, company, and anything you know about them]`. Draft a short, specific cold email, under 100 words, that references something real and specific about them (not "I saw your company and was impressed"), and ends with a single, low-friction ask. | Reaching out to a new prospect without writing from scratch every time. |
| Follow-up sequence | Here's the first email I sent: `[paste it]`. They haven't replied in `[X days]`. Write 2 follow-ups, spaced a week apart, each one adding a new reason to reply rather than just repeating "just following up." | A lead has gone quiet and you don't want to just bump the thread. |
| Objection response | A prospect said: `[paste their objection]`. Draft a reply that addresses the real concern honestly (don't just argue past it), and if it's a fair objection, say so before responding. | Mid-conversation, when you want a considered reply instead of a reflexive one. |
| Proposal draft from notes | Here are my rough notes from a call with `[client/prospect name]`: `[paste notes]`. Turn this into a clean, short proposal: what they need, what I'd do, timeline, and price. Flag anything in my notes that's ambiguous instead of guessing. | Right after a sales call, while the context is still fresh. |

## Operations and admin

| Command | Prompt | When to use it |
|---|---|---|
| Meeting notes to action items | Here's a transcript or my rough notes from today's meeting: `[paste them]`. Extract every action item, who owns it, and any deadline that was mentioned. Flag anything that sounded like a decision but was never actually confirmed. | Right after any meeting, instead of letting notes rot in a doc nobody re-reads. |
| Process writeup | Walk me through how I actually do `[a task you do regularly]` right now, asking me one question at a time, then write it up as a clean, numbered SOP I can hand to someone else or automate later. | The first time you write down a process instead of just doing it from memory. |
| Inbox triage plan | I have `[N]` unread emails/messages I'm behind on. Help me sort them into: needs a real reply, can be a one-line reply, can wait, can be deleted or archived. Draft the one-line replies for me to approve. | Digging out from a backlog without missing something important. |
| Weekly review | Here's what I said I'd do this week: `[paste last week's plan or task list]`. Compare it against what actually got done (ask me if you're not sure), and help me write next week's plan based on what's actually still open. | End of week, closing the loop instead of just starting a new list from nothing. |

## Finance and admin

| Command | Prompt | When to use it |
|---|---|---|
| Invoice/expense sanity check | Here's this month's `[expenses export or invoice list]`. Flag anything that looks like a duplicate charge, an unexpected increase from last month, or a subscription I might have forgotten I'm paying for. | Monthly, before you approve or file it away unread. |
| Pricing sanity check | Here's my current pricing for `[product/service]`: `[paste it]`. Given what `[competitors, if known]` charge and what this actually costs me to deliver, tell me honestly if this is underpriced, and by how much. | Before a price change, or when you suspect you're leaving money on the table. |

## Customer support

| Command | Prompt | When to use it |
|---|---|---|
| Draft a support reply | A customer wrote: `[paste their message]`. Our policy on this is `[state the policy, or point to the doc]`. Draft a reply that's warm but doesn't promise anything outside policy, and flag if this looks like a pattern worth fixing upstream. | Responding to support without either over-promising or sounding like a form letter. |
| Turn recurring questions into an FAQ | Here are the last `[N]` support questions I've answered: `[paste them or point to a log]`. Group them by topic and draft FAQ answers for the 5 most common ones. | You keep answering the same question individually instead of writing it down once. |

## Product and code (for a non-coder business owner)

| Command | Prompt | When to use it |
|---|---|---|
| Explain what changed | Look at what changed in this project in the last `[timeframe]` (check the git log). Explain it to me in plain English, no jargon, as if I've never seen the code. | You paid for or directed development work and want to actually understand what you got. |
| Bug report triage | A customer reported: `[paste their description]`. Investigate whether this is a real bug, reproduce it if you can, and tell me plainly: is this broken, is it working as designed, or do you need more information from them. | Before promising a fix (or dismissing a complaint) you haven't actually verified. |

---

## How to write your own

A good command in this bank has three parts, in this order:

1. **The real input**, not a description of it. "Here's the transcript:
   `[paste]`" beats "summarize my last meeting", because Claude can act on
   pasted content immediately, it can't go find the meeting itself.
2. **The specific output shape you want**, not just the topic. "5 bullets,
   ranked by X" beats "give me some ideas."
3. **What NOT to do**, when it matters. "Don't invent a detail that isn't in
   the original" or "flag anything ambiguous instead of guessing" stops the
   two most common failure modes: hallucinated specifics and silently
   guessed assumptions.

Save any prompt you find yourself retyping more than twice, either as a row
in this bank, or as a proper slash command (see `commands/goal-contract.md` in this
kit for a fuller example) if you use it often enough to want it one keystroke
away.
