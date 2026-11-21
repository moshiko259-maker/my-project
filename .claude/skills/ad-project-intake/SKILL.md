---
name: ad-project-intake
description: "Phase 1 of a client ad project: create the project workspace, inventory every supplied file, extract verified facts into a project knowledge base and list what is missing. Use when a new client folder, brief or asset pack arrives, or when the owner says start a project. Not for market research (brand-product-research) or ideas (creative-concept-development)."
---

# ad-project-intake

## Purpose
Turn a pile of client material into an organised workspace and a facts file that every later stage can trust.

## Required inputs
Path to the client material (folder, PDFs, images, links); project slug; any words from the owner about the goal, deadline, and whether the client may be contacted.

## Workflow
1. Run `python3 advertising-studio/tools/studio.py new <slug>` to create the 13 stage folders and the production log. Never move the owner's originals: copy them into `02-original-assets/`.
2. Inventory every file into `01-brief/asset-inventory.md` (template: `templates/asset-inventory.md`): file, type, what it shows, usable as reference yes/no, rights known yes/no.
3. Read every document fully. Look at every image (Read tool) and describe what is actually visible.
4. Write `01-brief/client-profile.md` and `01-brief/facts.md` from `templates/facts.md`: each fact with its source file or URL and tag VERIFIED / CLAIMED-BY-CLIENT / ASSUMPTION / UNKNOWN.
5. Write `01-brief/missing.md`: what is missing, why it matters, and how to get it without contacting the client if contact is not allowed.
6. Fill `01-brief/brief.md` from `templates/brief.md`; mark every field the owner has not confirmed.
7. Record the constraint flags in `production-log/project.json` (for example `client_contact_allowed`, `spec_work`).

## Expected outputs
`01-brief/` with asset-inventory.md, client-profile.md, facts.md, missing.md, brief.md; `02-original-assets/` copies; production log entry.

## Quality checklist
- [ ] Every file in the source folder appears in the inventory.
- [ ] No fact without a source.
- [ ] Originals untouched.
- [ ] Spec / surprise work is flagged, with the consent and trademark notes from `ai-video-legal-consent-labels`.

## Reuse - knowledge skills that own the details (load the one you need; do not copy them here)
client-brand-film-production (site mining, verifying who the client is), ai-advertising-director (truth and consent gate, spec-ad rule), ai-video-legal-consent-labels.

Templates: `advertising-studio/templates/`. Stage map and gates: `advertising-studio/workflows/master-workflow.md`.

## Hard rules (every stage)
- Never invent facts, prices, specs, product details or model capabilities. Unverified = write UNKNOWN and say what was tried.
- No paid generation, purchase, upgrade, publish or send without a recorded approval (see `production-budget-control`).
- Paid tools are never ruled out in advance: present cost, pros, cons, free alternative and a recommendation; act only after the owner's explicit yes.
- Recommend then teach: first the tool/model options (cheapest, most expensive, best quality, best value, with live prices and a pick), then, after the owner chooses, exact settings and numbered steps.
- Reply to the owner in Hebrew; Hebrew and English never on the same line. Files and prompts are in English.
- Never delete or overwrite the owner's files. Work only inside the client project folder and `advertising-studio/`.
