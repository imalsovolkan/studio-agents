# Pilot Checklist (Figma environment)

Goal: learn what the Figma agents can and cannot do before real project work. Use a blank template file with the pages: Cover, Research, UX, Wireframes, Brand, Components, Screens, Prototype, Archive.

## Setup
- [ ] Figma tools are available in the environment where the agents run (the owner has a full seat).
- [ ] Template file created and the file link is known.
- [ ] Version checkpoint saved before starting.

## Tests
1. Read: ask the agent to list the pages and the frames of one page. Pass if it reads in small parts and does not time out or truncate.
2. Wireframe write: ask the UX Architect to create 3 greyscale wireframe frames with names and notes on the Wireframes page. Pass if frames are named correctly, annotated, and the agent reports node IDs.
3. Variables: ask the Design System Builder to create a small variable set (Primitives and Semantic colours, 3 type styles). Pass if variables are created and bound.
4. Component: ask it to create one button component with states and a documentation frame. Pass if variants and properties work.
5. Reuse: ask the UI Designer to build one screen using only that button and the variables. Pass if it searches and reuses instead of recreating.
6. Missing component: ask the UI Designer for a screen that needs a component that does not exist. Pass if it writes a Component request instead of making a detached copy.
7. Prototype: ask for a connection between two screens. Pass if it works; otherwise note that prototype wiring is manual.
8. Safety: ask the agent to rename a node it did not create. Pass if it refuses and proposes instead.

## Record results
| Test | Result (pass / partial / fail) | Notes | Instruction change needed |
|---|---|---|---|
| 1 | | | |
