# agents/

Three starter subagents (`research-seat`, `draft-seat`, `verify-seat`) and two reading files. Course lessons 03.6.1 and 03.6.2 use them.

## Where they go

A subagent is one markdown file. It is not a setting, so nothing goes in `settings.json`.

| Copy the seats to | They are available in | Same name in both folders |
|---|---|---|
| `.claude/agents/` inside a project | that project only | this one wins |
| `~/.claude/agents/` in your home folder | every project | this one loses |

The closest folder wins, and a project file beats a personal one with the same `name`. Keep each `name` unique inside one folder.

```bash
mkdir -p .claude/agents
cp agents/research-seat.md agents/draft-seat.md agents/verify-seat.md .claude/agents/
```

## Prove it worked

In Claude Code run `/context` and find `research-seat`, `draft-seat` and `verify-seat` in the **Custom agents** block. Or ask: `list every subagent you can hand work to`. If the `agents` folder did not exist before the session started, open a fresh session once.

(`/agents` does not list them. In current Claude Code it only prints a reminder.)
