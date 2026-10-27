# commands/

`goal-contract.md` is one prompt that writes a contract file before Claude does any work.
Install it as a skill, which is how Claude Code stores your own slash commands now:

```bash
mkdir -p ~/.claude/skills/goal-contract
cp goal-contract.md ~/.claude/skills/goal-contract/SKILL.md
```

Start a fresh session and type `/goal-contract` plus a one-line job.

A file at `~/.claude/commands/goal-contract.md` still works and gives you the same command.
If both exist, the skill wins. Do not name either one `goal`: Claude Code already has a
built-in `/goal`.

`command-bank.md` is a table of paste-ready prompts. Nothing to install.
