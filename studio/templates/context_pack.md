# Product Context Pack (template)

Each product has its own context pack in `projects/<product>/pack/`. Agents read it together with project_state.md and decisions.md, and each agent reads only the files it needs.

## Files in a pack (create what applies; mark the rest "Not applicable")
| File | Purpose | Who writes it first | Needed by |
|---|---|---|---|
| product_overview.md | What it is, purpose, key facts, features, design decisions, visual language, brand summary | Owner or Scoping Analyst | All agents |
| audience_and_personas.md | Segments, personas (evidence or [A] assumptions), anti-audience, validation plan | UX Architect (from Researcher) | Researcher, PM, UX, Brand, Release |
| brand_guidelines.md | Logo, colour, type, tone, photography, rules | Brand Strategist | DS Builder, UI Designer, Release, Case Study |
| design_system_summary.md | Tokens, components, rules, backlog | Design System Builder | UI Designer, Release |
| screens_and_flows.md | Screens, flows, states, UX rules | UX Architect, UI Designer | PM, Release, Case Study |
| onboarding_flow.md (if the product has one) | Screen-by-screen onboarding | UX Architect | PM, Release |
| product_decisions.md | Product-level decisions, experiments, open questions | PM | All |
| release_facts.md (apps) | Store and legal facts: accounts, bundle ID, data collected, third parties, prices | Release Manager | Release Manager, PM |
| competitor_report.md | Latest competitor analysis | Researcher | PM, UX, Release |
| product_rules.md (optional) | Rules that apply to this product only, in the format of `studio/house_rules.md` | Owner | All agents |

## Rules
- A pack describes one product only. Never reuse a pack's content for another product.
- Names: previous or placeholder product names must not appear in documents that will be public.
- Mark assumptions [A] and unverified facts [Unverified].
- Keep each file focused and short; move history to decisions.md.
- Update the pack when a stage is approved; the Studio Lead checks that the pack and project_state.md agree.
