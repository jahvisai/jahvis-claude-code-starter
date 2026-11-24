#!/usr/bin/env python3
"""Test the jah-session-tools settings script and hooks in throwaway folders.

Run from the starter folder:  python3 proof/session-tools-test.py
Nothing outside a temporary folder is touched. Each check prints PASS or FAIL.
"""
import json
import os
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.join(HERE, "..", "plugins", "jah-session-tools", "skills", "jah-session-setup")
MERGE = os.path.join(SKILL, "scripts", "settings_merge.py")
WAITING = os.path.join(SKILL, "hooks", "jah-waiting-on-you.py")
HOOKS_JSON = os.path.join(HERE, "..", "plugins", "jah-session-tools", "hooks", "hooks.json")
RESULTS = []


def check(name, ok, detail=""):
    RESULTS.append(ok)
    print(("PASS " if ok else "FAIL ") + name + ("  [" + detail + "]" if detail else ""))


def run(args, stdin=""):
    start = time.time()
    proc = subprocess.run([sys.executable] + args, input=stdin, capture_output=True, text=True)
    return proc.returncode, proc.stdout, proc.stderr, int((time.time() - start) * 1000)


def tidy(text, tmp):
    return text.replace(tmp, "<scratch>").replace(os.path.expanduser("~"), "~")


def test_settings(tmp):
    print("\n== B1: recommended settings on a scratch settings file ==")
    path = os.path.join(tmp, "settings.json")
    original = {
        "model": "sonnet",
        "env": {"MY_SETTING": "1"},
        "permissions": {"allow": ["Bash(npm test *)", "Bash(git status *)"], "deny": ["Read(./.env)"]},
        "hooks": {"PreToolUse": [{"matcher": "Bash", "hooks": [{"type": "command", "command": "echo mine"}]}]},
    }
    with open(path, "w") as fh:
        json.dump(original, fh, indent=2)
    raw_before = open(path).read()

    code, out, err, _ = run([MERGE, "--recommended", "--dry-run", "--settings", path])
    print(tidy(out, tmp))
    check("dry run changes nothing", code == 0 and open(path).read() == raw_before)
    check("dry run shows the exact change", "+" in out and "git diff" in out and "Notification" in out)

    code, out, err, _ = run([MERGE, "--recommended", "--settings", path])
    print(tidy(out, tmp))
    after = json.load(open(path))
    check("file is valid JSON after", isinstance(after, dict))
    check("earlier keys kept", after["model"] == "sonnet" and after["env"] == {"MY_SETTING": "1"}
          and after["permissions"]["deny"] == ["Read(./.env)"]
          and after["hooks"]["PreToolUse"] == original["hooks"]["PreToolUse"]
          and "Bash(npm test *)" in after["permissions"]["allow"])
    check("3 read-only git rules present once each",
          all(after["permissions"]["allow"].count(r) == 1 for r in
              ["Bash(git status *)", "Bash(git diff *)", "Bash(git log *)"]))
    notice = after["hooks"]["Notification"][0]
    check("desktop notice hook added for this computer", notice["matcher"] == "permission_prompt|idle_prompt",
          notice["hooks"][0]["command"])
    check("backup made", any(f.startswith("settings.json.bak-") for f in os.listdir(tmp)))

    code, out, err, _ = run([MERGE, "--recommended", "--settings", path])
    check("second run adds nothing", "already there" in out and json.load(open(path)) == after)

    code, out, err, _ = run([MERGE, "--undo-recommended", "--settings", path])
    print(tidy(out, tmp))
    check("undo restores the original exactly (the user's own git status rule is kept)",
          json.load(open(path)) == original)

    print("\n== B1: no settings file at all ==")
    path2 = os.path.join(tmp, "empty", "settings.json")
    run([MERGE, "--recommended", "--settings", path2])
    made = json.load(open(path2))
    check("file made and valid", "permissions" in made and "hooks" in made)
    run([MERGE, "--undo-recommended", "--settings", path2])
    check("undo leaves an empty settings object", json.load(open(path2)) == {})

    print("\n== B1: broken settings file ==")
    path3 = os.path.join(tmp, "broken.json")
    with open(path3, "w") as fh:
        fh.write("{ not json")
    code, out, err, _ = run([MERGE, "--recommended", "--settings", path3])
    check("stops, changes nothing", code == 1 and "Stopped" in out and open(path3).read() == "{ not json")


def transcript(path, entries):
    with open(path, "w") as fh:
        for e in entries:
            fh.write(json.dumps(e) + "\n")


def assistant(text):
    return {"type": "assistant", "message": {"role": "assistant", "content": [{"type": "text", "text": text}]}}


def user(text):
    return {"type": "user", "message": {"role": "user", "content": text}}


def test_waiting(tmp):
    print("\n== B2: waiting on you ==")
    folder = os.path.join(tmp, "project")
    tdir = os.path.join(tmp, "transcripts")
    os.makedirs(folder)
    os.makedirs(tdir)
    now_t = os.path.join(tdir, "now-session.jsonl")
    transcript(now_t, [user("hello")])
    with open(os.path.join(folder, "HANDOFF.md"), "w") as fh:
        fh.write("# HANDOFF\n\n## Waiting on you\n"
                 "- [ ] Which logo should the site use? (asked 2026-11-23; blocked: the home page)\n"
                 "- [ ] Is the price $49 or $59? (asked 2026-11-23; blocked: the sales page)\n\n"
                 "## 2026-11-23: site start\n### Gotchas and open questions\n- [ ] not counted, wrong heading\n")
    payload = {"session_id": "now-session", "cwd": folder, "transcript_path": now_t, "source": "startup"}
    code, out, err, ms = run([WAITING, "start"], json.dumps(payload))
    print(tidy(out, tmp))
    msg = json.loads(out)["systemMessage"] if out.strip() else ""
    check("2 open questions: one line naming 2", code == 0 and msg.startswith("Waiting on you: 2 questions")
          and "\n" not in msg, "{} ms".format(ms))

    empty = os.path.join(tmp, "empty-project")
    os.makedirs(empty)
    with open(os.path.join(empty, "HANDOFF.md"), "w") as fh:
        fh.write("# HANDOFF\n\n## 2026-11-23: done\n### What is done\n- all of it\n")
    code, out, err, ms = run([WAITING, "start"], json.dumps(dict(payload, cwd=empty)))
    check("no open questions: prints nothing", code == 0 and out == "" and err == "", "{} ms".format(ms))

    old = os.path.join(tdir, "old-session.jsonl")
    transcript(old, [user("build my site"), assistant("Done with the menu.\n\nShould the footer show your phone number?")])
    answered = os.path.join(tdir, "answered-session.jsonl")
    transcript(answered, [assistant("Should I use blue?"), user("yes")])
    code, out, err, ms = run([WAITING, "start"], json.dumps(dict(payload, cwd=empty)))
    print(tidy(out, tmp))
    msg = json.loads(out)["systemMessage"] if out.strip() else ""
    check("earlier session still waiting on a question is counted (answered one is not)",
          msg.startswith("Waiting on you: 1 question is") and "earlier session" in msg, "{} ms".format(ms))

    asked = os.path.join(tdir, "asked-session.jsonl")
    transcript(asked, [user("go"), {"type": "assistant", "message": {"content": [
        {"type": "tool_use", "name": "AskUserQuestion", "input": {"questions": [{"question": "Which plan?"}]}}]}}])
    code, out, err, ms = run([WAITING, "start"], json.dumps(dict(payload, cwd=empty)))
    check("an unanswered question box counts too", out and json.loads(out)["systemMessage"].startswith("Waiting on you: 2"))
    os.remove(asked)

    print("\n== B2: session end writes the open question to HANDOFF.md ==")
    end_payload = {"session_id": "old-session", "cwd": empty, "transcript_path": old, "reason": "prompt_input_exit"}
    code, out, err, ms = run([WAITING, "end"], json.dumps(end_payload))
    text = open(os.path.join(empty, "HANDOFF.md")).read()
    print(text)
    check("question written under Waiting on you with date and blocked",
          code == 0 and "## Waiting on you\n- [ ] Should the footer show your phone number? (asked " in text
          and "blocked:" in text, "{} ms".format(ms))
    run([WAITING, "end"], json.dumps(end_payload))
    check("second end does not write it twice",
          open(os.path.join(empty, "HANDOFF.md")).read().count("phone number") == 1)
    code, out, err, ms = run([WAITING, "start"], json.dumps(dict(payload, cwd=empty)))
    check("same question in HANDOFF.md and the old session is counted once",
          json.loads(out)["systemMessage"].startswith("Waiting on you: 1 question is"))

    print("\n== B2: the hook never fails a session start ==")
    cases = {"garbage input": "not json", "empty input": "", "a list": "[]",
             "missing folder": json.dumps({"cwd": os.path.join(tmp, "nope"), "transcript_path": 5}),
             "HANDOFF.md is a folder": None}
    bad = os.path.join(tmp, "bad")
    os.makedirs(os.path.join(bad, "HANDOFF.md"))
    cases["HANDOFF.md is a folder"] = json.dumps({"cwd": bad})
    for name, stdin in cases.items():
        for mode in ("start", "end"):
            code, out, err, ms = run([WAITING, mode], stdin)
            check("{} ({}): exit 0, silent".format(name, mode), code == 0 and out == "" and err == "")


def test_hooks_json():
    print("\n== Plugin hooks file ==")
    data = json.load(open(HOOKS_JSON))
    events = sorted(data["hooks"])
    check("hooks.json is valid and has the 3 events", events == ["SessionEnd", "SessionStart", "UserPromptSubmit"],
          ", ".join(events))


def main():
    with tempfile.TemporaryDirectory() as tmp:
        tmp = os.path.realpath(tmp)
        test_settings(tmp)
        test_waiting(tmp)
    test_hooks_json()
    print("\n{} of {} checks passed".format(sum(RESULTS), len(RESULTS)))
    return 0 if all(RESULTS) else 1


if __name__ == "__main__":
    sys.exit(main())
