#!/usr/bin/env python3
"""Change ~/.claude/settings.json for the session tools, safely.

Usage:
  python3 settings_merge.py --recommended --dry-run   show the recommended settings change, change nothing
  python3 settings_merge.py --recommended             apply it (read-only git without asking, desktop notice)
  python3 settings_merge.py --undo-recommended        take back exactly what --recommended added
  python3 settings_merge.py            add the reminder hook by hand (copy installs only; copies it to ~/.claude/hooks/ too)
  python3 settings_merge.py --dry-run  show what would change, change nothing
  python3 settings_merge.py --uninstall  take the reminder hook back out
  Add --settings <file> to any of these to work on another settings file (used for testing).

Rules it keeps:
  - It backs up settings.json to settings.json.bak-<date> before any change.
  - It keeps every setting and every hook you already have.
  - Running it twice does not add the hook twice.
Standard library only. Works on macOS, Linux and Windows.
"""
import argparse
import datetime
import difflib
import json
import os
import shutil
import sys

HOOK_NAME = "jah-handoff-reminder.py"

# The recommended settings. Claude Code already treats read-only git commands as safe in most
# cases; these rules make sure they never ask, in every mode.
GIT_READ_ONLY = ["Bash(git status *)", "Bash(git diff *)", "Bash(git log *)"]
NOTICE_TEXT = "Claude needs you"
NOTICE_COMMANDS = {
    "mac": "osascript -e 'display notification \"" + NOTICE_TEXT + "\" with title \"Claude Code\"' || true",
    "linux": "notify-send 'Claude Code' '" + NOTICE_TEXT + "' || true",
    "windows": "powershell -NoProfile -Command \"[void][Reflection.Assembly]::LoadWithPartialName('System.Windows.Forms');"
               " (New-Object Windows.Forms.NotifyIcon -Property @{Icon=[Drawing.SystemIcons]::Information; Visible=1})"
               ".ShowBalloonTip(5000,'Claude Code','" + NOTICE_TEXT + "',0); Start-Sleep 6\"",
}
NOTICE_MATCHER = "permission_prompt|idle_prompt"
RECORD_NAME = "session-setup-added.json"
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


def platform_key():
    if sys.platform == "darwin":
        return "mac"
    if sys.platform.startswith("win"):
        return "windows"
    return "linux"


def is_notice(hook):
    return isinstance(hook, dict) and hook.get("command") in NOTICE_COMMANDS.values()


def has_notice(settings):
    for group in settings.get("hooks", {}).get("Notification", []) or []:
        if any(is_notice(h) for h in (group or {}).get("hooks", [])):
            return True
    return False


def with_recommended(settings):
    """Return (new settings, record of what was added). Keeps everything already there."""
    new = json.loads(json.dumps(settings))
    record = {"allow_added": [], "notice_added": None, "created": []}
    if "permissions" not in new:
        record["created"].append("permissions")
    perms = new.setdefault("permissions", {})
    if "allow" not in perms:
        record["created"].append("permissions.allow")
    allow = perms.setdefault("allow", [])
    for rule in GIT_READ_ONLY:
        if rule not in allow:
            allow.append(rule)
            record["allow_added"].append(rule)
    if not has_notice(new):
        if "hooks" not in new:
            record["created"].append("hooks")
        hooks = new.setdefault("hooks", {})
        if "Notification" not in hooks:
            record["created"].append("hooks.Notification")
        command = NOTICE_COMMANDS[platform_key()]
        hooks.setdefault("Notification", []).append(
            {"matcher": NOTICE_MATCHER, "hooks": [{"type": "command", "command": command}]})
        record["notice_added"] = command
    return new, record


def without_recommended(settings, record):
    """Take back exactly what with_recommended added, and nothing else."""
    new = json.loads(json.dumps(settings))
    perms = new.get("permissions")
    if isinstance(perms, dict) and isinstance(perms.get("allow"), list):
        perms["allow"] = [r for r in perms["allow"] if r not in record.get("allow_added", [])]
        if not perms["allow"] and "permissions.allow" in record.get("created", []):
            del perms["allow"]
        if not perms and "permissions" in record.get("created", []):
            del new["permissions"]
    hooks = new.get("hooks")
    added = record.get("notice_added")
    if added and isinstance(hooks, dict) and isinstance(hooks.get("Notification"), list):
        kept = []
        for group in hooks["Notification"]:
            inner = [h for h in (group or {}).get("hooks", []) if not (isinstance(h, dict) and h.get("command") == added)]
            if inner:
                kept.append(dict(group, hooks=inner))
        hooks["Notification"] = kept
        if not kept and "hooks.Notification" in record.get("created", []):
            del hooks["Notification"]
        if not hooks and "hooks" in record.get("created", []):
            del new["hooks"]
    return new


def show_diff(before, after, label):
    old = json.dumps(before, indent=2).splitlines()
    new = json.dumps(after, indent=2).splitlines()
    lines = list(difflib.unified_diff(old, new, label + " now", label + " after", lineterm="", n=2))
    return "\n".join(lines) if lines else "(no change)"


def record_path(settings_path):
    return os.path.join(os.path.dirname(os.path.abspath(settings_path)), "session-kit", RECORD_NAME)


def recommended(settings_path, current, dry_run):
    new, record = with_recommended(current)
    if not record["allow_added"] and not record["notice_added"]:
        print("The recommended settings are already there. Nothing to change.")
        return 0
    print("Change to " + tidy(settings_path) + " (lines with + are added, nothing is removed):")
    print(show_diff(current, new, "settings.json"))
    if dry_run:
        print("Dry run. Nothing was changed.")
        return 0
    saved = backup(settings_path)
    save(settings_path, new)
    rec = record_path(settings_path)
    os.makedirs(os.path.dirname(rec), exist_ok=True)
    with open(rec, "w", encoding="utf-8") as fh:
        json.dump(record, fh, indent=2)
    print("Done. Backup: " + (tidy(saved) if saved else "none (there was no settings file before)"))
    print("Undo: python3 \"" + tidy(os.path.abspath(__file__)) + "\" --undo-recommended"
          + ("" if settings_path == default_settings() else " --settings \"" + tidy(settings_path) + "\""))
    return 0


def undo_recommended(settings_path, current, dry_run):
    rec = record_path(settings_path)
    if not os.path.exists(rec):
        print("Nothing to undo: there is no record of a recommended-settings change here.")
        return 0
    with open(rec, "r", encoding="utf-8") as fh:
        record = json.load(fh)
    new = without_recommended(current, record)
    print("Change to " + tidy(settings_path) + " (lines with - are taken out):")
    print(show_diff(current, new, "settings.json"))
    if dry_run:
        print("Dry run. Nothing was changed.")
        return 0
    saved = backup(settings_path)
    save(settings_path, new)
    os.remove(rec)
    print("Undone. Backup of the file before the undo: " + tidy(str(saved)))
    return 0


def tidy(path):
    """Show a path with ~ in place of the home folder, so no private folder name is printed."""
    home = os.path.expanduser("~")
    return "~" + path[len(home):] if path.startswith(home) else path


def default_settings():
    return os.path.join(claude_dir(), "settings.json")


def main():
    parser = argparse.ArgumentParser(description="Change settings.json for the session tools, safely.")
    parser.add_argument("--dry-run", action="store_true", help="show the change, write nothing")
    parser.add_argument("--uninstall", action="store_true", help="remove the hook")
    parser.add_argument("--recommended", action="store_true", help="add the recommended settings")
    parser.add_argument("--undo-recommended", action="store_true", help="take the recommended settings back out")
    parser.add_argument("--settings", help="work on this settings file instead of ~/.claude/settings.json")
    args = parser.parse_args()

    settings_path = os.path.abspath(os.path.expanduser(args.settings)) if args.settings else default_settings()
    hook_dest = os.path.join(claude_dir(), "hooks", HOOK_NAME)
    hook_src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "hooks", HOOK_NAME)

    try:
        current = load(settings_path)
    except ValueError as err:
        print("Stopped: " + tidy(settings_path) + " is not valid JSON (" + str(err) + "). Nothing changed.")
        return 1

    if args.recommended:
        return recommended(settings_path, current, args.dry_run)
    if args.undo_recommended:
        return undo_recommended(settings_path, current, args.dry_run)

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
