#!/usr/bin/env python3
"""
launch-folder-warning.py: a SessionStart hook for Claude Code.

Install: copy to ~/.claude/hooks/jah-workspace/launch-folder-warning.py (the same
place the 03.2.1 workspace kit installs it). It runs once it is
registered in ~/.claude/settings.json: the SessionStart block in this kit's
settings/global-settings.example.json. Read that block before you merge it.

What it does: if a session starts in your home folder, Desktop, Documents or
Downloads, it does two things. It returns a "systemMessage" (a line Claude Code
can show you), and it adds a note to Claude's own context asking Claude to tell
you, before doing anything else, to type /exit and start again inside your
workspace. Anything Claude creates with a relative path lands in the folder you
started in, which is how stray files end up in your home folder. In every other
folder it prints nothing. It never blocks a session.

Test it without Claude Code:
  echo '{"cwd": "'"$HOME"'"}' | python3 launch-folder-warning.py
"""
import json
import sys
from pathlib import Path


def label_for(cwd: Path):
    try:
        home = Path.home().resolve()
        cwd = cwd.resolve()
    except Exception:
        return None
    if cwd == home:
        return "home"
    for name in ("Desktop", "Documents", "Downloads"):
        if cwd == home / name:
            return name
    return None


def main() -> int:
    try:
        raw = sys.stdin.read()
        try:
            payload = json.loads(raw) if raw.strip() else {}
        except json.JSONDecodeError:
            payload = {}
        label = label_for(Path(payload.get("cwd") or "."))
        if label is None:
            return 0
        where = "your home folder" if label == "home" else f"your {label} folder"
        message = (
            f"You started Claude Code in {where}. Anything it creates lands here. "
            "Type /exit, then start again inside your workspace, for example: cd ~/work && claude"
        )
        print(json.dumps({
            "systemMessage": message,
            "hookSpecificOutput": {
                "hookEventName": "SessionStart",
                "additionalContext": (
                    f"This session started in {where}. Before doing any work, tell the user in "
                    "one sentence to type /exit and start Claude Code again inside their "
                    "workspace folder, and do not create files here."
                ),
            },
        }))
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
