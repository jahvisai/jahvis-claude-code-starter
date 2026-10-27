# <BUSINESS PROCESS NAME>

Updated: <YYYY-MM-DD>

<!-- Facts for any AI tool working in this folder. Claude reads this file through the
     @AGENTS.md line in CLAUDE.md beside it. Keep it under 120 lines. -->

## What this folder is

<one sentence: the business process this folder runs, e.g. "Turns new client intake forms
into a quote and a welcome email.">

## How the work is split: Workflows, Agents, Tools

- **Workflows** (`workflows/`): the instructions. One markdown file per process: the goal,
  the inputs it needs, which tools to run, what the output looks like, and what to do when
  something goes wrong. Written in plain language, the way you'd brief a new hire.
- **Agents** (the AI): the decision-maker. It reads the right workflow, runs the tools in
  order, handles failures, and asks when something is unclear.
- **Tools** (`tools/`): scripts that do the actual work (API calls, file changes, data
  clean-up) the same way every time.

Why the split matters: if each step done by hand in chat is 90% reliable, five steps in a row
succeed only about 59% of the time. A script does the same thing every run, so the error
doesn't compound.

## Folder layout

```
workflows/   markdown instructions, one per process
tools/       scripts that do the work
.tmp/        throwaway working files, safe to delete, rebuilt as needed
.env         real API keys (never committed, never printed)
```

- Finished work goes to the service you already check (a sheet, a doc, your CRM), not to a
  local file.
- Everything in `.tmp/` is disposable.

## Where keys live

- Real keys live in `.env` in this folder, kept out of git by `.gitignore`.
- Refer to a key by its NAME only, in files and in chat. Never print or paste a value.

## House rules

<!-- Swap these for your own. This is the shape, not your specific rules. -->
- Never create or overwrite a workflow file without asking first.
- Ask before running anything that spends money or paid credits.
- Never send anything to a real person without an explicit yes.
