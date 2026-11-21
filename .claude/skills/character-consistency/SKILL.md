---
name: character-consistency
description: "Keeps a person or mascot identical across shots: consent check for real people, character sheet, identity reference set and per-shot identity rules. Use when a human, presenter or mascot appears in more than one shot. Not for products (product-fidelity)."
---

# character-consistency

## Purpose
One face, one body, one wardrobe across the whole film - and no real person without a release.

## Required inputs
Concept and script; photos of real people only with a signed release; casting description for invented characters.

## Workflow
1. Real person? Stop until a written release exists (template in `ai-video-legal-consent-labels`). No look-alikes of real people.
2. Invented character: write the identity file (age range, build, face, hair, wardrobe, distinguishing marks).
3. Plan the character sheet (front, three-quarter, profile, full body, expressions) - a paid generation that needs the budget gate.
4. Fix which reference image is used for which shot size; one edit away from the master sheet, never a copy of a copy.
5. Record in the shot list: identity reference file, wardrobe, continuity notes.

## Expected outputs
`07-storyboard/character-<name>.md`; reference files in `07-storyboard/refs/`.

## Quality checklist
- [ ] Release on file for every real face and voice.
- [ ] One master sheet per character.
- [ ] Wardrobe and props listed per scene.

## Reuse - knowledge skills that own the details (load the one you need; do not copy them here)
higgsfield-consistent-characters-soul-id-elements-sheets, ai-video-realism, ai-avatars-and-presenters, human-body-proportions-and-blender-base-mesh-guide, ai-video-legal-consent-labels.

Templates: `advertising-studio/templates/`. Stage map and gates: `advertising-studio/workflows/master-workflow.md`.

## Hard rules (every stage)
- Never invent facts, prices, specs, product details or model capabilities. Unverified = write UNKNOWN and say what was tried.
- No paid generation, purchase, upgrade, publish or send without a recorded approval (see `production-budget-control`).
- Paid tools are never ruled out in advance: present cost, pros, cons, free alternative and a recommendation; act only after the owner's explicit yes.
- Recommend then teach: first the tool/model options (cheapest, most expensive, best quality, best value, with live prices and a pick), then, after the owner chooses, exact settings and numbered steps.
- Reply to the owner in Hebrew; Hebrew and English never on the same line. Files and prompts are in English.
- Never delete or overwrite the owner's files. Work only inside the client project folder and `advertising-studio/`.
