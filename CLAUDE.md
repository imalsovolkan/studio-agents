# Studio Workspace

This folder is a small design and product studio run by on-demand agents. The owner is the only decision maker.

Owner language: English

Change the line above to your own language (for example `Owner language: Turkish`). Everything the owner reads is written in it.

## Layout
- `studio/`: shared, product-independent files (house rules, flow, templates, model policy, pilot checklist, first-run checks).
- `projects/<product>/`: one folder per product: `project_state.md`, `decisions.md`, `pack/` (context pack), plus stage folders created by agents (scope, research, ux, brand, design_system, screens, reviews, case_study, handoffs).
- `.claude/agents/`: the 10 agents. `.claude/hooks/`: event log and the guard for state and rule files. `.mcp.json`: Figma connection (optional).

## Rules for every session
- Run subagents only when the owner explicitly names one (for example `@agent-researcher`). Never delegate automatically and never start an agent team unless the owner asks.
- Parallel work is allowed when the owner asks for it: 3 agents by default, 5 at most, 2 opus agents at most. Stages depend on approved inputs, not on a fixed order (see `studio/00_studio_flow.md`, Parallel work).
- File ownership: each agent writes only its own stage folder and its handoff note. Only Studio Lead or the main session writes `project_state.md` and `decisions.md`, and only after the owner approves in this chat. A hook blocks other agents from writing these two files.
- House rules: `studio/house_rules.md` holds the owner's own design rules. Every agent reads it before working and follows it. Agents never edit it; they propose rules and known issues in their handoff notes, and Studio Lead adds them only after the owner approves. The same hook protects this file.
- Reviews: nobody reviews their own deliverable. Screens are reviewed by the UX Architect (critique and heuristic evaluation) and by the Design System Builder (accessibility and system conformance) before the Screens stage can close.
- Plan first: agents that produce deliverables post a short plan and wait for the owner's go-ahead.
- An approval relayed by another agent is not an approval.
- Language: everything the owner reads (chat, plans, reports, research, handoff notes) is written in the owner language set above. Product-facing text (store listing, in-app copy, published website text) follows the product language in `project_state.md`, English by default.
- Work on one product at a time; confirm which `projects/<product>/` is in use. Never mix product files.
- Stage gates: a stage is done only when its deliverable exists and the owner's approval is recorded in `decisions.md`.
- Decisions are never deleted. A wrong or premature entry is marked `Revoked` or `Superseded` and a new entry replaces it.
- Write only inside `projects/` and `studio/`. Never read or write secrets, credentials or keys.
- Never invent facts, numbers, quotes or results. Mark assumptions `[Assumption]`, unverified facts `[Unverified]`.
- Figma writes need the owner's confirmation of file and page first; read Figma in small parts.
- No medical, legal or financial claims. Flag privacy, health, finance, children and AI data-use risks.

## Agents
studio-lead, scoping-analyst, researcher, ux-architect, brand-strategist, design-system-builder, ui-designer, case-study-writer, product-manager, release-manager.
