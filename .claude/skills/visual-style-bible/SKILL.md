---
name: visual-style-bible
description: "The project's fixed visual language: palette, light, lens feel, texture, framing rules, typography and do-not list, written once and applied to every shot and prompt. Use before storyboarding or when shots look like different films. Not for per-shot design (cinematic-storyboarding)."
---

# visual-style-bible

## Purpose
One look, written down, so twenty generations feel like one film.

## Required inputs
Brand assets (logo, colours, fonts from the client's own material), approved concept, reference images.

## Workflow
1. Extract brand colours and fonts only from the client's files or site; record hex values with their source. Unknown = UNKNOWN, never guessed.
2. Define: palette, contrast, light direction and quality, lens feel, depth of field, camera behaviour, grain / texture, set and wardrobe rules, typography for supers.
3. Write the style line: one reusable sentence that is pasted into every prompt.
4. Write the do-not list (looks, colours, cliches to avoid).
5. Save `07-storyboard/style-bible.md`; reference images go in `07-storyboard/refs/` with a caption each.

## Expected outputs
`07-storyboard/style-bible.md` and captioned refs.

## Quality checklist
- [ ] Brand colours sourced.
- [ ] Style line under 40 words.
- [ ] Rules are checkable by eye.

## Reuse - knowledge skills that own the details (load the one you need; do not copy them here)
ai-video-realism, ai-stylized-animation, cinematic-transitions-catalog, higgsfield-cinema-studio-versions-settings-and-prices.

Templates: `advertising-studio/templates/`. Stage map and gates: `advertising-studio/workflows/master-workflow.md`.

## Hard rules (every stage)
- Never invent facts, prices, specs, product details or model capabilities. Unverified = write UNKNOWN and say what was tried.
- No paid generation, purchase, upgrade, publish or send without a recorded approval (see `production-budget-control`).
- Paid tools are never ruled out in advance: present cost, pros, cons, free alternative and a recommendation; act only after the owner's explicit yes.
- Recommend then teach: first the tool/model options (cheapest, most expensive, best quality, best value, with live prices and a pick), then, after the owner chooses, exact settings and numbered steps.
- Text meant for the owner is in Hebrew, with Hebrew and English never on the same line (file paths, gate names and skill names go on their own line or in a code block). Files, prompts and a sub-agent's report to the producer are in English.
- 'Stop for owner approval' means: a sub-agent stops and returns the decision to the producer; only the producer talks to the owner and records approvals.
- A required input is missing: do not stop silently and do not invent it - continue with what exists, mark the gap UNKNOWN in the output, and list it under open items.
- Never delete or overwrite the owner's files. Work only inside the client project folder and `advertising-studio/`.
