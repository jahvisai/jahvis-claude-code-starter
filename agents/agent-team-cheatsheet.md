# Agent Team Cheat Sheet

One page. The three team patterns, the model-tier split, the build checklist, and the real parallelism ceiling.

## 3 Ways to Structure a Team

| Pattern | What it is | The one rule |
|---|---|---|
| Hub and spoke | Your main session coordinates, every seat reports back to it | Spokes never talk to each other, only to the coordinator |
| Standing verifier seat | One seat's whole job is reviewing everyone else's output | The seat that built something never approves it |
| Model-tiered roster | Each seat runs the model its job actually needs | Route routine work down, hard reasoning up |

## Model Tier Guide

| Tier | Use it for |
|---|---|
| Toughest model | Planning, architecture, debugging a subtle failure, the verifier that reviews everyone else |
| Workhorse model | Implementation from a written plan, research, codebase exploration, most day-to-day seats |
| Cheapest model | Bulk renames and extraction, log scanning, high-volume well-specified tasks |

## Build Checklist: Your First Three-Seat Team

1. **Name the three jobs first.** Research, draft, check. Write each as one plain-English line before touching syntax.
2. **Assign a model tier to each seat.** Match tier to real difficulty. The verifier earns the better model.
3. **Write each seat as its own agent file.** One file per seat: name, description, tools, model, system prompt.
4. **Dispatch hub and spoke.** Research seat reports to you, its summary goes to the draft seat, the draft goes to the verify seat. Nothing talks sideways.
5. **Run seats in waves.** Two to four seats per wave, each on its own files. Verify, merge, then start the next wave.

## Your Real Parallelism Ceiling

- **Roughly ten agents per person** is a common rule of thumb, not a Claude Code limit, for where one person's review still holds up. Past that, verification shifts from you to another model.
- **Ten to twenty agents** is where people who push the limits report their own review turning into skimming. Treat it as a warning, not a target. (Claude Code itself stops you at 20 subagents running at once by default.)
- **Two to four seats per wave**, each in its own git worktree, is the honest ceiling for a solo operator with no dedicated reviewer.
- **Waves run one after another.** Only seats inside the same wave, on separate files, run at the same time.

## Common Mistakes

- One agent playing two roles: the agent that wrote the draft cannot also approve it.
- Skipping the gap check: a coordinator's too-narrow breakdown leaves whole pieces uncovered, and no seat can flag it.
- Opening a second wave before the first one proved itself.
- Two seats in one wave touching the same files: that's a merge conflict, not parallel-safe work.

## Shelf Life

This is a current best bet, not settled architecture. Re-check the Claude Code docs every few months, because how agents run keeps changing.
