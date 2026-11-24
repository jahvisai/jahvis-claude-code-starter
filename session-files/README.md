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

The two skills and the hook are one plugin, `jah-session-tools`, in `plugins/jah-session-tools/` in this starter.
The hook file is `plugins/jah-session-tools/skills/jah-session-setup/hooks/jah-handoff-reminder.py`.

## Install (the plugin way, gets updates)

In the desktop app or a terminal, these two commands add our free marketplace and install the plugin:

```bash
claude plugin marketplace add jahvisai/jahvis-claude-code-starter
claude plugin install jah-session-tools@jahvis
```

Then start a new session and type `/jah-session-tools:jah-session-setup` once.

Turn on updates once: type `/plugin` in a terminal session, open the Marketplaces tab, pick `jahvis`, turn auto-update on.
Without it, get the newest version with `claude plugin update jah-session-tools@jahvis`.

## The older way (copy by hand, no updates)

Copy `plugins/jah-session-tools/skills/jah-session-setup` and `plugins/jah-session-tools/skills/jah-wrap` into `~/.claude/skills/`, then say "run session setup".
To undo that hook: `python3 ~/.claude/skills/jah-session-setup/scripts/settings_merge.py --uninstall`

If you switch to the plugin, run the setup skill again: it takes the old hook out so the reminder never shows twice.
