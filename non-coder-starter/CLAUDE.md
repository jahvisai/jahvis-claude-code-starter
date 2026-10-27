@AGENTS.md

<!-- Line 1 pulls in AGENTS.md. Below it: only how Claude Code should operate here.
     Keep this file under 25 lines. -->

- Before any task, find the matching file in `workflows/` and follow it.
- Look in `tools/` before writing a new script; build one only when nothing covers the job.
- When something fails: read the full error, fix the tool, run it again, then add what you
  learned to the workflow file so it doesn't trip the same way twice.
- Ask before re-running anything that spends paid credits.
- Plan first on anything with more than three steps, and run `/clear` between unrelated jobs.
