#!/usr/bin/env python3
"""Waiting on you (a SessionStart and SessionEnd hook for Claude Code).

What it does, in plain words:
  1. When a session ENDS while Claude's last message was a question you never
     answered, it writes that question into HANDOFF.md, under the heading
     "## Waiting on you". It only writes if HANDOFF.md already exists.
  2. When a session STARTS, it counts the questions still waiting on you in
     this folder: the open items under "## Waiting on you" in HANDOFF.md, plus
     any other session in this folder from the last 3 days that stopped on a
     question you never answered. If there are any, it shows you one line.
     If there are none, it says nothing.

Usage (the plugin runs these for you):
  python3 jah-waiting-on-you.py start
  python3 jah-waiting-on-you.py end

Safe by design: Python standard library only, works on Mac, Windows and Linux,
never blocks a session, and on any error it prints nothing and exits 0.
"""
import datetime
import glob
import json
import os
import re
import sys
import time

HEADING = "## Waiting on you"
OPEN_ITEM = re.compile(r"^\s*-\s*\[ \]\s*(.+?)\s*$")
RECENT_DAYS = 3
MAX_FILES = 30
TAIL_BYTES = 256 * 1024


def read_text(path):
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def open_items(handoff_text):
    """Return the open '- [ ]' items under the Waiting on you heading."""
    items = []
    inside = False
    for line in handoff_text.splitlines():
        if line.strip().lower() == HEADING.lower():
            inside = True
            continue
        if inside and line.startswith("#"):
            break
        if inside:
            match = OPEN_ITEM.match(line)
            if match:
                items.append(match.group(1))
    return items


def last_entries(path):
    """Read the end of a transcript file and return its JSON lines, oldest first."""
    size = os.path.getsize(path)
    with open(path, "rb") as fh:
        if size > TAIL_BYTES:
            fh.seek(size - TAIL_BYTES)
            fh.readline()
        raw = fh.read().decode("utf-8", errors="replace")
    entries = []
    for line in raw.splitlines():
        try:
            entry = json.loads(line)
        except ValueError:
            continue
        if isinstance(entry, dict):
            entries.append(entry)
    return entries


def text_of(content):
    if isinstance(content, str):
        return content
    parts = []
    if isinstance(content, list):
        for block in content:
            if isinstance(block, dict) and block.get("type") == "text":
                parts.append(str(block.get("text", "")))
    return "\n".join(parts)


def question_in(entry):
    """If this assistant entry ends on a question to the person, return it."""
    content = (entry.get("message") or {}).get("content")
    if isinstance(content, list):
        for block in content:
            if (isinstance(block, dict) and block.get("type") == "tool_use"
                    and block.get("name") == "AskUserQuestion"):
                questions = (block.get("input") or {}).get("questions") or []
                if questions and isinstance(questions[0], dict):
                    return str(questions[0].get("question", "")).strip() or None
    text = text_of(content).strip()
    if not text:
        return None
    last_line = [ln.strip() for ln in text.splitlines() if ln.strip()][-1]
    last_line = last_line.strip("*_` ")
    if not last_line.endswith("?"):
        return None
    sentences = re.split(r"(?<=[.!?])\s+", last_line)
    return sentences[-1][:300]


def waiting_question(path):
    """Return the unanswered question a transcript stopped on, or None."""
    for entry in reversed(last_entries(path)):
        if entry.get("isSidechain") or entry.get("isMeta"):
            continue
        kind = entry.get("type")
        if kind == "user":
            return None
        if kind == "assistant":
            return question_in(entry)
    return None


def other_sessions_waiting(transcript_path, session_id):
    if not isinstance(transcript_path, str) or not transcript_path:
        return []
    folder = os.path.dirname(transcript_path)
    if not os.path.isdir(folder):
        return []
    cutoff = time.time() - RECENT_DAYS * 86400
    files = []
    for path in glob.glob(os.path.join(folder, "*.jsonl")):
        name = os.path.splitext(os.path.basename(path))[0]
        if name == session_id:
            continue
        try:
            mtime = os.path.getmtime(path)
        except OSError:
            continue
        if mtime >= cutoff:
            files.append((mtime, path))
    found = []
    for _, path in sorted(files, reverse=True)[:MAX_FILES]:
        try:
            question = waiting_question(path)
        except Exception:
            continue
        if question:
            found.append(question)
    return found


def start(payload):
    cwd = payload.get("cwd") or os.getcwd()
    handoff = os.path.join(cwd, "HANDOFF.md")
    items = open_items(read_text(handoff)) if os.path.isfile(handoff) else []
    known = " ".join(items)
    others = [q for q in other_sessions_waiting(payload.get("transcript_path"), payload.get("session_id"))
              if q not in known]
    total = len(items) + len(others)
    if total == 0:
        return
    word = "question is" if total == 1 else "questions are"
    places = []
    if items:
        places.append("{} in HANDOFF.md".format(len(items)))
    if others:
        places.append("{} in an earlier session in this folder".format(len(others)))
    them = "it" if total == 1 else "them"
    line = "Waiting on you: {} {} still open from before ({}). Answer {} before starting that work again.".format(
        total, word, " and ".join(places), them)
    context = ["Questions this folder is still waiting on the person to answer:"]
    context += ["- (HANDOFF.md) " + q for q in items]
    context += ["- (earlier session, still open in the session list) " + q for q in others]
    context.append("If the person's first message starts the same work again, mention these first and offer to "
                   "answer them here. When one is answered, the jah-wrap skill removes it from HANDOFF.md.")
    sys.stdout.write(json.dumps({
        "systemMessage": line,
        "hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": "\n".join(context)},
    }))


def end(payload):
    cwd = payload.get("cwd") or os.getcwd()
    handoff = os.path.join(cwd, "HANDOFF.md")
    transcript = payload.get("transcript_path")
    if not os.path.isfile(handoff) or not isinstance(transcript, str) or not os.path.isfile(transcript):
        return
    question = waiting_question(transcript)
    if not question:
        return
    text = read_text(handoff)
    if question in text:
        return
    today = datetime.date.today().isoformat()
    item = "- [ ] {} (asked {}; blocked: the work that question was about, the session ended before you answered)".format(
        question, today)
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip().lower() == HEADING.lower():
            lines.insert(i + 1, item)
            break
    else:
        at = 1 if lines and lines[0].startswith("# ") else 0
        lines[at:at] = ["", HEADING, item, ""]
    with open(handoff, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines).rstrip("\n") + "\n")


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    raw = sys.stdin.read()
    payload = json.loads(raw) if raw.strip() else {}
    if not isinstance(payload, dict):
        return
    if mode == "start":
        start(payload)
    elif mode == "end":
        end(payload)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
