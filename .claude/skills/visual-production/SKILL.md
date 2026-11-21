---
name: visual-production
description: "Phase 6 execution: generates approved reference images, final images and video clips through Higgsfield (official skills, CLI or MCP) or another approved tool, one approved batch at a time, logging every job and its cost. Use only after storyboard, model plan and budget are approved. Not for deciding models or budgets."
---

# visual-production

## Purpose
Run exactly what was approved, record everything, stop when the approved budget is used.

## Required inputs
Approved prompts, model plan, references, and an approval record for this batch.

## Workflow
1. Run `python3 advertising-studio/tools/studio.py check <slug> <batch-gate>`. If it does not print APPROVED, stop and go to `production-budget-control`.
2. Use the official Higgsfield skills first (`higgsfield-generate`, `higgsfield-product-photoshoot`, `higgsfield-soul-id`); do not rebuild what they do.
3. Upload references; start with the cheapest draft setting the plan allows; one shot first as a test.
4. After each job run `studio.py log <slug> ...` with job id, model, settings, credits, result path.
5. Save outputs to `09-generated-images/` or `10-generated-videos/` named `shot-<nn>_v<k>`.
6. Send each result to quality control before generating the next dependent shot.
7. When the approved credit ceiling is reached, stop and report - a new batch needs a new approval.

## Expected outputs
Generated files; `production-log/generations.csv`.

## Quality checklist
- [ ] No job without an approval record.
- [ ] Every job logged with real credits.
- [ ] Nothing published or shared.

## Reuse - knowledge skills that own the details (load the one you need; do not copy them here)
higgsfield-hub and its branches, higgsfield-generate, higgsfield-product-photoshoot, higgsfield-mcp-slash-commands-katana-recipes-and-workflows, ai-video-realism, ai-motion-control, ai-lip-sync-and-dialogue.

Templates: `advertising-studio/templates/`. Stage map and gates: `advertising-studio/workflows/master-workflow.md`.

## Hard rules (every stage)
- Never invent facts, prices, specs, product details or model capabilities. Unverified = write UNKNOWN and say what was tried.
- No paid generation, purchase, upgrade, publish or send without a recorded approval (see `production-budget-control`).
- Paid tools are never ruled out in advance: present cost, pros, cons, free alternative and a recommendation; act only after the owner's explicit yes.
- Recommend then teach: first the tool/model options (cheapest, most expensive, best quality, best value, with live prices and a pick), then, after the owner chooses, exact settings and numbered steps.
- Reply to the owner in Hebrew; Hebrew and English never on the same line. Files and prompts are in English.
- Never delete or overwrite the owner's files. Work only inside the client project folder and `advertising-studio/`.
