# House Rules

The owner's own design rules. Every agent reads this file before it starts and follows it. Reviewers check deliverables against it.

Agents never edit this file. They propose new rules and known issues in their handoff notes, and the owner decides. Studio Lead adds an entry only after the owner approves (`add rule`).

## How to write a rule
- Start with one. Pick a decision you make the same way every time and write it down.
- Write what to do. "Consistent spacing" is a wish; "spacing comes from the seven-step scale and nothing in between" is a rule.
- Put the number in the rule whenever there is one.
- Say how to check it. A rule nobody can check is still a habit.
- If a rule is hard to write, that is worth knowing: the decision may not be a rule yet.

## Rules
The four rules below are starter rules. Keep, change or delete them, then add your own.

| ID | Rule | Why | How to check | Since |
|---|---|---|---|---|
| R01 | Do not invent new values. When a token, style or component exists, use it: no new colours, spacing values, radii or easing curves | Near-duplicates are hard to see and they spread quietly. Two almost identical greys can live on different pages for months | Every colour, type style, spacing and radius on a screen maps to a variable or style | starter |
| R02 | Every animation has a reduced-motion alternative | People who are sensitive to motion turn it down in their system settings, and the product should respect that | For each animation, the reduced-motion behaviour is specified next to it | starter |
| R03 | Mistakes go on record. After a bug or a design error is fixed, add it to the Known issues log below, with the one-line rule it produced | Otherwise the fix lives only in the head of whoever made it | Every fix mentioned in a handoff note has an entry in the Known issues log | starter |
| R04 | Do not invent the owner's experience. No made-up projects, results, numbers, quotes or anecdotes in anything written in the owner's name | A plausible story that did not happen is still false | Every claim in a case study or post has a source in the project files, or is listed for the owner to confirm | starter |

## Known issues log
One entry per problem that was solved. Newest at the bottom.

| Date | Problem | Cause | Fix | Rule it produced |
|---|---|---|---|---|
| | | | | |

## Rules for one product only
Rules that apply to a single product (its tokens, its tone, its limits) go in that product's pack as `projects/<product>/pack/product_rules.md`, in the same format. When a product rule and a house rule conflict, the agent stops and asks the owner.
