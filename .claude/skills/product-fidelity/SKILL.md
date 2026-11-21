---
name: product-fidelity
description: "Protects the real product in every generated frame: builds the product truth sheet from the original photos, sets what is locked and what may change per shot, and defines how accuracy is checked. Use whenever a real product, package or logo appears. Not for people (character-consistency)."
---

# product-fidelity

## Purpose
The original product photos are the source of truth; nothing about the product is invented.

## Required inputs
Original product photos in `02-original-assets/`; product facts.

## Workflow
1. Pick the hero reference photos (front, side, back, detail, scale) and list gaps.
2. Write `07-storyboard/product-truth-sheet.md` from `templates/product-truth-sheet.md`: shape and proportions, colours, materials, logo position, text on pack, parts and accessories - only what the photos or facts show.
3. Mark three columns for every shot: A product facts (locked), B creative interpretation (allowed), C generated elements (free).
4. Choose the fidelity route per shot: real photo composited in post; reference-driven generation; packshot from the original photo. Text and logos that must be exact are added in post, not generated.
5. Improving an original photo (relight, clean, upscale, background) must not change the product itself: compare before and after side by side.
6. If a model cannot keep an essential detail, record the limitation and switch route - never present a wrong product as correct.

## Expected outputs
`07-storyboard/product-truth-sheet.md`; locked / free columns in the shot list.

## Quality checklist
- [ ] No feature, colour, size, material, logo or accessory that the sources do not show.
- [ ] Each product shot names its fidelity route.
- [ ] Exact text and logos are composited.

## Reuse - knowledge skills that own the details (load the one you need; do not copy them here)
ai-advertising-director (product consistency kit, packshot), client-brand-film-production (packshot), higgsfield-product-photoshoot, screen-ui-compositing.

Templates: `advertising-studio/templates/`. Stage map and gates: `advertising-studio/workflows/master-workflow.md`.

## Hard rules (every stage)
- Never invent facts, prices, specs, product details or model capabilities. Unverified = write UNKNOWN and say what was tried.
- No paid generation, purchase, upgrade, publish or send without a recorded approval (see `production-budget-control`).
- Paid tools are never ruled out in advance: present cost, pros, cons, free alternative and a recommendation; act only after the owner's explicit yes.
- Recommend then teach: first the tool/model options (cheapest, most expensive, best quality, best value, with live prices and a pick), then, after the owner chooses, exact settings and numbered steps.
- Reply to the owner in Hebrew; Hebrew and English never on the same line. Files and prompts are in English.
- Never delete or overwrite the owner's files. Work only inside the client project folder and `advertising-studio/`.
