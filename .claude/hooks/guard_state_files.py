#!/usr/bin/env python3
"""PreToolUse guard for Edit and Write.

Enforces two studio rules for subagents:
1. Inside projects/, the state files (project_state.md and decisions.md) are
   written only by Studio Lead or by the main session.
2. The owner's rule files (studio/house_rules.md and a product's
   pack/product_rules.md) are written only by Studio Lead or by the main
   session.
Any other subagent is denied and told to propose the change in its handoff
note instead.

Fails open: on any unexpected input the call is allowed (exit 0, no output),
so this hook can never block normal work by mistake."""
import json
import os
import sys

STATE_FILES = ("project_state.md", "decisions.md")
ALLOWED_AGENTS = ("studio-lead",)

try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)

try:
    agent = data.get("agent_type") or ""  # empty in the main session
    tool_input = data.get("tool_input") or {}
    path = "/" + str(tool_input.get("file_path") or "").replace("\\", "/")
    name = os.path.basename(path)
    is_state_file = name in STATE_FILES and "/projects/" in path
    is_rule_file = path.endswith("/studio/house_rules.md") or (
        name == "product_rules.md" and "/projects/" in path
    )
    if agent and agent not in ALLOWED_AGENTS and (is_state_file or is_rule_file):
        if is_state_file:
            reason = (
                name + " is written only by Studio Lead or the main session, "
                "after the owner approves. Propose the change in your handoff note instead."
            )
        else:
            reason = (
                name + " holds the owner's rules. Agents do not edit it. "
                "Propose the rule or known issue in your handoff note instead."
            )
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": reason,
            }
        }))
except Exception:
    pass
sys.exit(0)
