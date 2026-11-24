# Model Policy (agents)

Set in each agent file under `.claude/agents/<name>.md`, in the `model:` line. Allowed values in Claude Code subagents: `sonnet`, `opus`, `haiku`, `fable`, a full model ID, or `inherit`. Aliases (`sonnet`, `opus`) follow the newest version of that tier; use a full model ID if you want a fixed version.

## Assignment
| Agent | Model | Why |
|---|---|---|
| studio-lead | sonnet | Frequent, routine: state tracking, gate checks, audits. Needs speed and low cost |
| scoping-analyst | opus | Scope, MVP cut and duration drive business decisions; mistakes are costly; needs judgment under missing information |
| researcher | opus | Evidence-critical synthesis across many sources; must resist inventing; long outputs |
| ux-architect | opus | Structural reasoning: flows, IA, decision trees, consistency across many screens |
| brand-strategist | sonnet | Creative strategy and guideline writing; good quality at lower cost. Move to opus for naming or hard repositioning |
| design-system-builder | sonnet | Long, rule-following Figma work with many tool calls. Move to opus if the pilot shows rule or naming mistakes |
| ui-designer | sonnet | Many Figma tool calls composing from existing components. Move to opus if the pilot shows component misuse |
| case-study-writer | sonnet | Writing from verified inputs; strong enough, cheaper |
| product-manager | opus | Trade-offs, prioritisation, MVP and roadmap reasoning |
| release-manager | opus | Policy compliance, privacy and store rules; errors cause rejections or legal risk |

No agent uses haiku: these agents must follow long rule sets (evidence, approval and safety rules) and haiku is more likely to skip them. `fable` is the top tier and costs most; it is not assigned by default. Use it only for a single hard task if your plan offers it (check `/model`).

## The main session model
`@agent-...` calls start from your main Claude Code session, which also uses tokens. Keep the main session on sonnet (`/model` in the terminal) and let each agent use its own model.

## Cost control
- Opus agents (5 of 10) are the expensive ones: call them for the deliverable, not for small questions. Ask small questions to the main session instead.
- Run one agent at a time (agent teams are off). Token cost scales with the number of agents running.
- Start a new session for each stage (`/clear`) and give each agent only the files it needs.

## Review after the pilot
After the Figma pilot and the first real runs, note per agent: errors, rule violations, cost. Move an agent up or down one tier with one line in its file, and note the change in this file.
