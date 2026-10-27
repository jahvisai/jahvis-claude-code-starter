#!/usr/bin/env bash
# Copy one starter template into the folder you are standing in. Never overwrites a file you already have.
# Usage (from inside your project or client folder):  bash ~/jahvis-claude-code-starter/install.sh freelancer
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
NAME="${1:-}"
if [ -z "$NAME" ] || [ ! -d "$HERE/claude-md-templates/$NAME" ]; then
  echo "Pick one template:"; ls "$HERE/claude-md-templates"; echo "Example: bash $HERE/install.sh small-business"; exit 1
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
