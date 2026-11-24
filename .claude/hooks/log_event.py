#!/usr/bin/env python3
"""Append one JSON line per agent event to .claude/logs/agent_events.jsonl.
Never blocks anything: always exits 0. Field names are read defensively and the
raw keys are kept, so the log stays useful if the hook input changes."""
import json, sys, os, datetime
try:
    data = json.load(sys.stdin)
except Exception:
    data = {}
root = os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or os.getcwd()
last = data.get("last_assistant_message")
rec = {
    "ts": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
    "event": data.get("hook_event_name"),
    "session": data.get("session_id"),
    "agent_id": data.get("agent_id"),
    "agent_type": data.get("agent_type"),
    "teammate": data.get("teammate_name"),
    "task": data.get("task_subject") or data.get("task_id"),
    "last_message_chars": len(last) if isinstance(last, str) else None,
    "keys": sorted(data.keys()),
}
# Does any handoff note exist that changed in the last 30 minutes?
try:
    import glob, time
    notes = glob.glob(os.path.join(root, "projects", "*", "handoffs", "*.md"))
    rec["recent_handoff"] = any(time.time() - os.path.getmtime(n) < 1800 for n in notes)
except Exception:
    rec["recent_handoff"] = None
try:
    d = os.path.join(root, ".claude", "logs")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "agent_events.jsonl"), "a") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
except Exception:
    pass
sys.exit(0)
