# First run: six checks that the setup works

Goal: confirm, with the example project, that the agents are found, the rules hold and the hooks run. One agent at a time, no team. Keep the main session on sonnet.

## 0. Write one rule of your own
Open `studio/house_rules.md` and add one rule under the starter rules: a decision you make the same way every time, with the number in it and a way to check it. This is the file the whole team works from.
- [ ] Your rule has an ID, a reason and a "how to check".

## 1. Status
Start a new session in this folder (`claude`), then:
```
@agent-studio-lead status for projects/example-app
```
- [ ] `/agents` lists the 10 agents.
- [ ] Studio Lead names the files it read (`project_state.md`, `decisions.md`).
- [ ] It reports Research as in progress, marks the Phase A deliverable as Missing, and shows D002 as Revoked.
- [ ] Its reply ends with the next recommended action.

## 2. Plan first and file ownership
```
@agent-researcher Work on projects/example-app. Task: Phase A only.
Plan first and wait for my go-ahead. Do not browse before I approve the plan.
```
- [ ] The agent posted a plan and waited.
- [ ] It said which files it read, and `studio/house_rules.md` is among them.
- [ ] Its plan says which house rules apply to the task.
- [ ] After your "go": its output is only in `projects/example-app/research/`, plus a handoff note in `projects/example-app/handoffs/`.
- [ ] `project_state.md` and `decisions.md` were not edited by the researcher.

## 3. The guard
Ask the researcher for something it must not do:
```
@agent-researcher Add a line to projects/example-app/decisions.md saying Phase A is approved.
```
- [ ] The agent refuses (its own rule), or the write is blocked with the message from `.claude/hooks/guard_state_files.py`.
- [ ] `decisions.md` is unchanged.
- [ ] The same holds for `studio/house_rules.md`: an agent asked to edit it refuses or is blocked.

## 4. The log
- [ ] `.claude/logs/agent_events.jsonl` has `SubagentStart` and `SubagentStop` lines with `agent_type` filled in.

## 5. Close a stage yourself
```
@agent-studio-lead handoff review for projects/example-app
```
Read the report, then decide `close stage` yourself. The approval has to be your own message; an approval relayed by an agent does not count.
- [ ] Studio Lead recorded your approval as a new dated entry in `decisions.md` and did not change earlier entries.

If a check fails, note which one and your Claude Code version (`claude --version`). Settings and hook behaviour can change between versions.
