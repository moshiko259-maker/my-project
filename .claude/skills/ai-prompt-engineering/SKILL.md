---
name: ai-prompt-engineering
description: "Writes one production-ready prompt per approved shot for the chosen model, with reference labels, the style line, locked elements and a repair plan. Use after the storyboard and model choice are approved. Not for choosing the model (model-selection) or running it (visual-production)."
---

# ai-prompt-engineering

## Purpose
Prompts that match the storyboard and the model's real syntax, written once and logged.

## Required inputs
Approved shot list, style bible, truth sheets, chosen model per shot.

## Workflow
1. Load the owning prompt skill for the chosen model (list below) - do not write from memory.
2. Write the prompt in the model's order; paste the style line; name each reference and its role.
3. State locked elements positively; keep one main action; give duration and aspect ratio.
4. Add the repair plan: if it fails, change one thing only, in this order.
5. Save to `08-prompts/shot-<nn>.md` with model, settings, references, expected cost line (from budget control).
6. Log working prompts back to the project's PROMPTS file.

## Expected outputs
`08-prompts/shot-<nn>.md` for every shot.

## Quality checklist
- [ ] Prompt matches the approved shot, nothing added.
- [ ] References exist on disk.
- [ ] Settings are real options of that model (verified in the registry).

## Reuse - knowledge skills that own the details (load the one you need; do not copy them here)
prompt-writing-core (router), higgsfield-seedance-prompt-builder, google-flow-video-prompts, cinematic-prompt-builder, multipurpose-ai-tools, prompt-library-video-image.

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
