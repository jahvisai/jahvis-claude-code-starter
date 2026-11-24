#!/usr/bin/env python3
"""Add (or remove) the handoff reminder hook in ~/.claude/settings.json.

Usage:
  python3 settings_merge.py            add the hook (copies it to ~/.claude/hooks/ too)
  python3 settings_merge.py --dry-run  show what would change, change nothing
  python3 settings_merge.py --uninstall  take the hook back out

Rules it keeps:
  - It backs up settings.json to settings.json.bak-<date> before any change.
  - It keeps every setting and every hook you already have.
  - Running it twice does not add the hook twice.
Standard library only. Works on macOS, Linux and Windows.
"""
import argparse
import datetime
import json
import os
import shutil
import sys

HOOK_NAME = "jah-handoff-reminder.py"
COMMAND = 'python3 "$HOME/.claude/hooks/' + HOOK_NAME + '"'


def claude_dir():
    return os.path.join(os.path.expanduser("~"), ".claude")


def load(path):
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read().strip()
    if not text:
        return {}
    data = json.loads(text)
    if not isinstance(data, dict):
        raise ValueError("settings.json is not a JSON object")
    return data


def is_ours(hook):
    return isinstance(hook, dict) and HOOK_NAME in str(hook.get("command", ""))


def has_ours(settings):
    for group in settings.get("hooks", {}).get("UserPromptSubmit", []):
        if any(is_ours(h) for h in (group or {}).get("hooks", [])):
            return True
    return False


def with_hook(settings):
    new = json.loads(json.dumps(settings))
    hooks = new.setdefault("hooks", {})
    groups = hooks.setdefault("UserPromptSubmit", [])
    groups.append({"hooks": [{"type": "command", "command": COMMAND}]})
    return new


def without_hook(settings):
    new = json.loads(json.dumps(settings))
    hooks = new.get("hooks")
    if not isinstance(hooks, dict) or "UserPromptSubmit" not in hooks:
        return new
    kept = []
    for group in hooks["UserPromptSubmit"]:
        inner = [h for h in (group or {}).get("hooks", []) if not is_ours(h)]
        if inner:
            kept.append(dict(group, hooks=inner))
    if kept:
        hooks["UserPromptSubmit"] = kept
    else:
        del hooks["UserPromptSubmit"]
    if not hooks:
        del new["hooks"]
    return new


def backup(path):
    if not os.path.exists(path):
        return None
    stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")
    target = path + ".bak-" + stamp
    shutil.copy2(path, target)
    return target


def save(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2)
        fh.write("\n")
    os.replace(tmp, path)


def main():
    parser = argparse.ArgumentParser(description="Add or remove the handoff reminder hook.")
    parser.add_argument("--dry-run", action="store_true", help="show the change, write nothing")
    parser.add_argument("--uninstall", action="store_true", help="remove the hook")
    args = parser.parse_args()

    settings_path = os.path.join(claude_dir(), "settings.json")
    hook_dest = os.path.join(claude_dir(), "hooks", HOOK_NAME)
    hook_src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "hooks", HOOK_NAME)

    try:
        current = load(settings_path)
    except ValueError as err:
        print("Stopped: ~/.claude/settings.json is not valid JSON (" + str(err) + "). Nothing changed.")
        return 1

    if args.uninstall:
        if not has_ours(current):
            print("The reminder hook is not in settings.json. Nothing to remove.")
        else:
            new = without_hook(current)
            if args.dry_run:
                print("Dry run. settings.json would become:\n" + json.dumps(new, indent=2))
            else:
                saved = backup(settings_path)
                save(settings_path, new)
                print("Removed the reminder hook from ~/.claude/settings.json. Backup: " + str(saved))
        if os.path.exists(hook_dest) and not args.dry_run:
            os.remove(hook_dest)
            print("Deleted ~/.claude/hooks/" + HOOK_NAME)
        return 0

    if args.dry_run:
        if has_ours(current):
            print("Dry run. The hook is already in settings.json. Nothing would change.")
        else:
            print("Dry run. settings.json would become:\n" + json.dumps(with_hook(current), indent=2))
        print("Dry run. Would copy the hook to ~/.claude/hooks/" + HOOK_NAME)
        return 0

    os.makedirs(os.path.dirname(hook_dest), exist_ok=True)
    shutil.copy2(hook_src, hook_dest)
    print("Copied the hook to ~/.claude/hooks/" + HOOK_NAME)
    if has_ours(current):
        print("The hook was already in settings.json. Nothing added.")
        return 0
    saved = backup(settings_path)
    save(settings_path, with_hook(current))
    print("Added the hook to ~/.claude/settings.json under hooks, UserPromptSubmit.")
    print("Backup: " + (saved or "none (there was no settings.json before)"))
    print("Undo: python3 " + os.path.abspath(__file__).replace(os.path.expanduser("~"), "~") + " --uninstall")
    return 0


if __name__ == "__main__":
    sys.exit(main())
