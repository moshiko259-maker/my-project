---
name: production-quality-control
description: "Phase 7 checks: compares every generated image and clip with the storyboard, the product truth sheet and the character sheet, checks continuity between shots and visual defects, and returns pass, fix or reject with a precise correction. Use after any generation and before the edit and delivery. Not for making the fix."
---

# production-quality-control

## Purpose
Nothing defective or inaccurate reaches the edit or the client.

## Required inputs
Generated file, its shot card, truth sheets, neighbouring shots.

## Workflow
1. Open the output and the originals side by side (Read tool on both).
2. Product: shape, proportions, colours, logo, text, parts - against the truth sheet. Any invented detail = reject.
3. Character: face, hair, wardrobe, hands, body proportions.
4. Shot: matches the approved framing, action, light and style line.
5. Continuity with the previous and next shot: screen direction, light, props, time of day, wardrobe.
6. Defects: warped text, extra fingers, melting objects, flicker, morphing, watermark, banding.
7. Verdict per file in `11-quality-control/qc-log.md` from `templates/qc-check.md`: PASS / FIX IN POST / REGENERATE with the one change to make. Regeneration is paid and goes back through the budget gate.

## Expected outputs
`11-quality-control/qc-log.md`; selects list for the edit.

## Quality checklist
- [ ] Every delivered frame has a QC row.
- [ ] Rejections say exactly what to change.
- [ ] Limits of the check are stated (for example: colour judged by eye on this screen).

## Reuse - knowledge skills that own the details (load the one you need; do not copy them here)
ai-video-realism (QA), ai-video-post-production (fix in post vs regenerate), ai-video-lessons-tree, screen-ui-compositing.

Templates: `advertising-studio/templates/`. Stage map and gates: `advertising-studio/workflows/master-workflow.md`.

## Hard rules (every stage)
- Never invent facts, prices, specs, product details or model capabilities. Unverified = write UNKNOWN and say what was tried.
- No paid generation, purchase, upgrade, publish or send without a recorded approval (see `production-budget-control`).
- Paid tools are never ruled out in advance: present cost, pros, cons, free alternative and a recommendation; act only after the owner's explicit yes.
- Recommend then teach: first the tool/model options (cheapest, most expensive, best quality, best value, with live prices and a pick), then, after the owner chooses, exact settings and numbered steps.
- Reply to the owner in Hebrew; Hebrew and English never on the same line. Files and prompts are in English.
- Never delete or overwrite the owner's files. Work only inside the client project folder and `advertising-studio/`.
