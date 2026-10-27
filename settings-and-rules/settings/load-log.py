#!/usr/bin/env python3
"""
load-log.py: an InstructionsLoaded hook for Claude Code. The proof tool.

Install: copy to <your project>/.claude/hooks/load-log.py. It runs once it is
registered in that project's .claude/settings.json: the InstructionsLoaded block in
this kit's settings/project-settings.example.json. It runs only in sessions started
in that folder.

What it does: every time Claude Code loads an instruction file (a CLAUDE.md, an
AGENTS.md through the @AGENTS.md pointer, or a rule), Claude Code runs this hook with
the file's path, its type and the reason it loaded. This appends one plain line per
file to .claude/loaded.log in the folder the session started in. Start a new session,
then open that log: if a file you expected is missing, you started in the wrong folder
or its pointer is missing. It writes only where a .claude folder already exists, never
in your home folder, and it never blocks a session. Keep .claude/loaded.log out of git.

Test it without Claude Code, from the project folder:
  echo '{"file_path": "CLAUDE.md", "load_reason": "test"}' | python3 .claude/hooks/load-log.py
"""
import json
import os
import sys
from datetime import datetime
from pathlib import Path


def short(path: str) -> str:
    """Show the home folder as ~ so the log is safe to screen-share."""
    home = str(Path.home())
    return "~" + path[len(home):] if path.startswith(home) else path


def main() -> int:
    try:
        raw = sys.stdin.read()
        try:
            payload = json.loads(raw) if raw.strip() else {}
        except json.JSONDecodeError:
            payload = {}
        start = os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or "."
        folder = Path(start).resolve()
        if folder == Path.home().resolve():
            return 0
        claude_dir = folder / ".claude"
        if not claude_dir.is_dir():
            return 0
        path = str(payload.get("file_path") or payload.get("path") or "unknown file")
        kind = str(payload.get("memory_type") or payload.get("type") or "-")
        reason = str(payload.get("load_reason") or payload.get("reason") or "-")
        stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with (claude_dir / "loaded.log").open("a") as f:
            f.write(f"{stamp}  {kind:<8}  {reason:<18}  {short(path)}\n")
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
