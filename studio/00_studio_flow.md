# Studio Flow

## Principles
- Agents work only when the owner calls them, one at a time or as a named team the owner asks for. No agent starts another agent on its own, contacts anyone, or publishes anything.
- Stages are dependencies, not a fixed queue. An agent may start as soon as its inputs exist and are approved, so independent stages can run at the same time (see Parallel work).
- Each agent does one stage and delivers one defined output.
- The owner approves every stage gate.
- Single source of truth per project: `project_state.md` and `decisions.md`.
- The owner's own rules live in `studio/house_rules.md`. Every agent reads them first, and reviewers check deliverables against them.
- Nobody reviews their own deliverable.

## Where agents work
- All agents run in this workspace and read and write files under `projects/<product>/`.
- Three agents also write to Figma and need the Figma connection in `.mcp.json`: UX Architect (flows, maps and wireframes), Design System Builder and UI Designer. The UX Architect also saves its maps as .md files so the other agents can read them.
- The other seven work with files only: Studio Lead, Scoping Analyst, Researcher, Brand Strategist, Case Study Writer, Product Manager, Release Manager. Researcher, Brand Strategist, Product Manager and Release Manager can also search the web; each search asks for the owner's permission.

## Stages and gates
| Stage | Agent | Works in | Input | Output | Owner approval |
|---|---|---|---|---|---|
| 1 Scoping | Scoping Analyst | Files | Brief, call notes, constraints.md (optional) | Scope, MVP cut, duration range, fit to constraints | Scope approved |
| 2 Research | Researcher | Files, web | Scope doc or context pack | Competitor and user report | Report approved |
| 3a UX | UX Architect | Files, Figma | Scope, report | Decisions, personas, flows, IA, decision trees, wireframes | UX approved |
| 3b Brand (parallel) | Brand Strategist | Files, web | Scope, report, existing brand assets | Brand guide, visual style | Brand approved |
| 4 Design system | Design System Builder | Figma | Brand, wireframes | Tokens, components, docs | System approved |
| 5 Screens | UI Designer | Figma | Wireframes, design system | Screens, prototype | Design approved, after both reviews |
| 6 Case study | Case Study Writer | Files | All outputs | Web document | Publish approved |

Gate rule: a stage is Done only when (a) its deliverable file exists, (b) open questions are listed, and (c) the owner's approval is recorded in `decisions.md`.

## Reviews (no extra agent)
Review is a second job for two agents that did not make the work under review.

| What is reviewed | Reviewer | What it checks | Output |
|---|---|---|---|
| Screens and prototype (stage 5) | UX Architect | Critique against scope, decisions, flows and house rules; heuristic evaluation (cognitive walkthrough, Nielsen's ten heuristics) | `reviews/<date>-design-review.md` |
| Screens and prototype (stage 5) | Design System Builder | Accessibility against the system's standards; system conformance (no invented values, no detached components) | `reviews/<date>-accessibility-review.md` |

- Reviews are read-only. Reviewers write findings, not fixes, and make no write call to Figma during a review.
- Every finding has a severity: Blocker, Major, Minor or Note (see `templates/review_note.md`).
- The UI Designer answers every finding: Fixed, or Not fixed and why. A Blocker closes only when it is fixed, or when the owner accepts it in `decisions.md`.
- If the two reviews conflict, Studio Lead shows both findings side by side and the owner decides.
- Stage 5 cannot close without both reviews.

## Outside the pipeline
- Studio Lead: process controller. It checks state at the start and end of every stage, recommends the next agent, and never does specialist work.
- Product Manager: turns the approved research report into MVPs, a roadmap, feature briefs and experiments. It does not start before the research report is approved.
- Release Manager: iOS App Store readiness (audit, listing, privacy answers, legal drafts, TestFlight plan, rejection responses). It audits and prepares; it never submits.

## Parallel work (agent team, optional)
- Only when the owner asks for a team in plain words, naming the agents. Default size 3, at most 5 at once; at most 2 opus agents at once (cost).
- A stage can start when every input in its row is approved in `decisions.md`. Typical parallel sets: Research + Release audit + UX gap list (all read the existing pack); Brand + UX; Design system + wireframes (different Figma pages); Case study + PM planning (after approved outputs).
- Not parallel: UI screens before wireframes and design system are approved; PM MVP before the research report is approved.
- File ownership: each agent writes only its own stage folder and its handoff note. Only Studio Lead (or the main session) writes `project_state.md` and `decisions.md`, after the owner approves. Two agents never write the same Figma page.
- Teammates message each other for questions only. An approval relayed by an agent is never an approval: only the owner's own message counts.
- Agent teams make every named subagent start as a teammate without asking; turn them back off (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` = "0") when the team work is done.

Studio Lead checks state at the start and end of every stage. Nothing moves to the next stage without the owner's approval recorded in `decisions.md`.

## Per-project folder (same for every product)
pack/ · scope/ · research/ · ux/ · brand/ · design_system/ · screens/ · reviews/ · case_study/ · handoffs/ · project_state.md · decisions.md

Existing products enter at the stage that fits (for example "existing product" mode skips Scoping and starts from `pack/`). Studio Lead sets this in project_state.md.

## Figma file template (one file per project)
Pages: Cover, Research, UX, Wireframes, Brand, Components, Screens, Prototype, Archive. Each agent writes only to its own pages.

## Figma safety rules for all Figma agents
- Confirm the target file and page with the owner before the first write of a session.
- Save a version checkpoint (or work on a duplicate) before any large write; the owner does this in Figma or approves the agent's request to.
- Read in small parts: one frame or section at a time. Never request a whole large page in one call (a full component page can return about 445,000 characters and gets truncated).
- Never delete or rename existing nodes the agent did not create unless asked.
- After each write, report what changed with node IDs.
- Use the Figma tool guidance that requires loading the matching Figma skill before writing.

## Pilot test (before real project work)
See `pilot_checklist.md`.

## Two layers of files
- Studio layer (shared, never product-specific): `studio/` (including `house_rules.md`) and `.claude/agents/`.
- Product layer (one folder per product): `project_state.md`, `decisions.md` and a context pack (see `templates/context_pack.md`). Give each agent only the files it needs. Never copy one product's pack into another product's folder.

## Agents list
Studio Lead, Scoping Analyst, Researcher, UX Architect, Brand Strategist, Design System Builder, UI Designer, Case Study Writer, Product Manager, Release Manager.
