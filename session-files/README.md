# Session tools

Tools that help you start, run and end a Claude Code session without remembering the steps.

| Tool | What it does | How to use it |
|---|---|---|
| `jah-session-setup` skill | One-time setup: your name line, HANDOFF.md, and the reminder hook. | Say "run session setup" once. |
| `jah-wrap` skill | Ends a piece of work: updates HANDOFF.md, saves and uploads, gives you the next first message. | Say "wrap up" when you finish something. |
| `jah-handoff-reminder.py` hook | Tells Claude to suggest a wrap-up when the session gets heavy. | Turned on by session setup. Nothing to do. |
| `HANDOFF.template.md` | The note one session leaves for the next. | Setup copies it to your project as HANDOFF.md. |
| `RISKS.template.md` | A list of known problems and dates. | Copy it to your project as RISKS.md if you want one. |
| `canary-CLAUDE.md` | Shows how the name line tells you Claude still follows your rules. | Read it. Setup adds the line for you. |
| `clear-vs-compact-guide.md` | When to start fresh and when to shrink a session. | Read it once. |

The two skills are in `.claude/skills/` in this starter. The hook is in `.claude/skills/jah-session-setup/hooks/`.

To undo the hook: `python3 ~/.claude/skills/jah-session-setup/scripts/settings_merge.py --uninstall`
