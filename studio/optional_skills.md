# Optional skills

The agents work without any skill. Some agent files name skills in their `skills:` frontmatter. If a named skill is not installed, Claude Code skips it and the agent still runs. This repository does not bundle third-party skills; install the ones you want yourself, per project, in `.claude/skills/`.

| Agent | Skill named in its frontmatter | Source (GitHub) | Licence as noted on 2026-11-02 |
|---|---|---|---|
| researcher | competitive-brief, synthesize-research | anthropics/knowledge-work-plugins | Apache 2.0 |
| product-manager | competitive-brief | anthropics/knowledge-work-plugins | Apache 2.0 |
| ux-architect | journey-mapping, design-critique | cuellarfr/design-skills | MIT |
| design-system-builder | design-systems, accessibility-audit | cuellarfr/design-skills | MIT |
| ui-designer | accessibility-audit | cuellarfr/design-skills | MIT |
| case-study-writer | ux-writing | cuellarfr/design-skills | MIT |
| release-manager | app-store-review | safaiyeh/app-store-review-skill | MIT |

Other skills from cuellarfr/design-skills that fit this team: ux-research, ux-strategy, interaction-design, design-ops.

## Before installing any skill
- Read its SKILL.md and every script in its folder. A skill runs with the agent's permissions.
- Install per project (`.claude/skills/`), not globally.
- Check the licence in the source repository yourself. The column above is a note, not a guarantee.
- The Release Manager audits and prepares; it never submits. Do not add a skill that can submit to App Store Connect unless you record that decision in `decisions.md`.
- In an agent team the `skills:` field is not applied; teammates load skills from project and user settings.
- Figma's own skills, served by the Figma MCP server or plugin, must be loaded before any write to Figma.
