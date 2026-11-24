#!/usr/bin/env python3
"""Handoff reminder (a UserPromptSubmit hook for Claude Code).

What it does: before each message you send, it checks how full this session's
memory (its "context") is. When the session gets heavy, it adds a short note
that asks Claude to suggest running the jah-wrap skill at the next good
stopping point. It speaks at most once per session for each level below.

How it measures: it reads the session's log file (the "transcript") and adds up
the three token counts on the last main reply (input, cache creation and cache
read). Replies from helper agents are skipped, because they have their own memory.

Safe by design: it only uses the Python standard library, it never blocks you,
and on any error it prints nothing and exits 0.
"""
import json
import os
import re
import sys

# The two levels, in tokens. The note is added once when the session passes each one.
# Lower them if your sessions feel slow sooner; raise them if the note comes too early.
FIRST_REMINDER_TOKENS = 150000
SECOND_REMINDER_TOKENS = 300000


def to_int(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def context_size(transcript_path):
    size = 0
    with open(transcript_path, "r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            if '"usage"' not in line:
                continue
            try:
                entry = json.loads(line)
            except ValueError:
                continue
            if not isinstance(entry, dict) or entry.get("type") != "assistant":
                continue
            if entry.get("isSidechain"):
                continue
            usage = (entry.get("message") or {}).get("usage")
            if not isinstance(usage, dict):
                continue
            size = (
                to_int(usage.get("input_tokens"))
                + to_int(usage.get("cache_creation_input_tokens"))
                + to_int(usage.get("cache_read_input_tokens"))
            )
    return size


def main():
    payload = json.loads(sys.stdin.read())
    if not isinstance(payload, dict):
        return
    session_id = payload.get("session_id")
    transcript_path = payload.get("transcript_path")
    if not isinstance(session_id, str) or not session_id.strip():
        return
    if not isinstance(transcript_path, str) or not os.path.isfile(transcript_path):
        return
    safe_id = re.sub(r"[^A-Za-z0-9_-]", "_", session_id.strip())[:120]

    size = context_size(transcript_path)
    if size >= SECOND_REMINDER_TOKENS:
        level = "second"
    elif size >= FIRST_REMINDER_TOKENS:
        level = "first"
    else:
        return

    mark_dir = os.path.join(os.path.expanduser("~"), ".claude", "session-kit", "reminder-marks")
    mark_file = os.path.join(mark_dir, safe_id + "." + level)
    if os.path.exists(mark_file):
        return
    os.makedirs(mark_dir, exist_ok=True)
    with open(mark_file, "w", encoding="utf-8") as fh:
        fh.write(str(size))

    note = (
        "Handoff reminder: this session is heavy (about {:,} tokens). "
        "Every new message re-reads all of it, so it gets slower and costs more. "
        "Finish what you are doing now. At the next natural stopping point, suggest "
        "in one short sentence that the user runs the jah-wrap skill, which saves "
        "HANDOFF.md and gets them ready for a fresh session. Do not stop the current task to say it."
    ).format(size)
    sys.stdout.write(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": note,
        }
    }))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
