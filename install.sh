#!/usr/bin/env bash
# Copy one starter template into the folder you are standing in. Never overwrites a file you already have.
# Usage (from inside your project or client folder):  bash ~/jahvis-claude-code-starter/install.sh freelancer
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
NAME="${1:-}"
if [ "$NAME" = "skill" ]; then
  # Install the setup interview for every folder, so it works from your work folder (no need to open this repo).
  D="$HOME/.claude/skills/jah-setup-interview"
  mkdir -p "$HOME/.claude/skills"
  if [ -e "$D" ]; then rm -rf "$D"; fi
  cp -R "$HERE/.claude/skills/jah-setup-interview" "$D"
  echo "Installed /jah-setup-interview for every folder."
  echo "Next: open a NEW Claude Code session in your work folder and type /jah-setup-interview"
  exit 0
fi
if [ "$NAME" = "workspace" ]; then
  if [ "$PWD" = "$HOME" ]; then echo "Stop: you are in your home folder. cd into a NEW empty folder (for example ~/work) first."; exit 1; fi
  if [ -e AGENTS.md ] || [ -e CLAUDE.md ]; then echo "This folder already has an AGENTS.md or CLAUDE.md. Nothing was copied."; exit 0; fi
  cp -Rn "$HERE/workspace-root/." ./
  echo "Copied the workspace root into $PWD"
  echo "Next: fill the <placeholders> in AGENTS.md and context/, delete departments you will not open weekly."
  exit 0
fi
if [ -z "$NAME" ] || [ ! -d "$HERE/claude-md-templates/$NAME" ]; then
  echo "Pick one template (or: workspace):"; ls "$HERE/claude-md-templates"; echo "Example: bash $HERE/install.sh small-business"; exit 1
fi
if [ "$PWD" = "$HOME" ]; then echo "Stop: you are in your home folder. cd into one project or client folder first."; exit 1; fi
if [ -e AGENTS.md ] || [ -e CLAUDE.md ]; then
  echo "This folder already has an AGENTS.md or CLAUDE.md. Nothing was copied."
  echo "Open Claude Code here and ask it to merge the template in, keeping everything you already have:"
  echo "  $HERE/claude-md-templates/$NAME"
  exit 0
fi
cp -Rn "$HERE/claude-md-templates/$NAME/." ./
echo "Copied the $NAME template into $PWD"
echo "Next: open AGENTS.md, replace every <angle-bracket placeholder> with real facts, delete the > lines."
echo "Line 1 of CLAUDE.md must stay: @AGENTS.md"
echo "If you add a CLAUDE.local.md for your own notes, add it to .gitignore yourself."
echo "Your own slash commands go in .claude/skills/<name>/SKILL.md (see $HERE/commands/README.md)."
echo "Your own subagents go in .claude/agents/ (see $HERE/agents/README.md)."
echo "Check it loaded: start Claude Code here and type /memory."
