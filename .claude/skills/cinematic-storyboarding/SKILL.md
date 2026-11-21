---
name: cinematic-storyboarding
description: "Phase 5 storyboard and shot list: the approved script broken into numbered shots with duration, framing, lens, camera move, light, colour, action, references and what must stay unchanged, ready for prompt writing. Use when a storyboard, shot list, shooting board or animatic plan is needed. Not for writing the model prompts (ai-prompt-engineering)."
---

# cinematic-storyboarding

## Purpose
Every shot decided on paper before a credit is spent.

## Required inputs
Approved script; style bible; product and character reference files.

## Workflow
1. Number the shots; give each a duration so the total equals the script length.
2. Per shot fill `templates/shot.md`: purpose, shot size, angle, lens feel, camera move, subject action (one main action), light, palette, sound note, transition in/out.
3. Per shot list references by file name and the LOCKED elements (product shape, logo, colours, face) versus FREE elements.
4. Flag hard shots (hands on product, text on screen, liquids, fast action, crowds) and give a simpler fallback for each.
5. Build `07-storyboard/shot-list.md` (table) and `07-storyboard/storyboard.md` (one block per shot, frame image added when generated).
6. Plan coverage for the edit: at least one cutaway and one alternative angle per scene.
7. Stop for owner approval (gate `storyboard`). Frame images are paid generations and need the budget gate first.

## Expected outputs
`07-storyboard/shot-list.md`, `storyboard.md`.

## Quality checklist
- [ ] Durations sum to the script length.
- [ ] Every shot names its references and locked elements.
- [ ] One main action per shot.
- [ ] Each hard shot has a fallback.

## Reuse - knowledge skills that own the details (load the one you need; do not copy them here)
seedance-shotlist-director, cinematic-director, cinematic-transitions-catalog, ai-3d-previs-blocking, ai-video-acting-director.

Templates: `advertising-studio/templates/`. Stage map and gates: `advertising-studio/workflows/master-workflow.md`.

## Hard rules (every stage)
- Never invent facts, prices, specs, product details or model capabilities. Unverified = write UNKNOWN and say what was tried.
- No paid generation, purchase, upgrade, publish or send without a recorded approval (see `production-budget-control`).
- Paid tools are never ruled out in advance: present cost, pros, cons, free alternative and a recommendation; act only after the owner's explicit yes.
- Recommend then teach: first the tool/model options (cheapest, most expensive, best quality, best value, with live prices and a pick), then, after the owner chooses, exact settings and numbered steps.
- Reply to the owner in Hebrew; Hebrew and English never on the same line. Files and prompts are in English.
- Never delete or overwrite the owner's files. Work only inside the client project folder and `advertising-studio/`.
