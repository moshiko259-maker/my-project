---
name: audience-market-analysis
description: "Phase 2 analysis of the target audience, market and competitors' advertising: who buys, why, what rivals already say and show, and where the open space is. Use when defining who the ad speaks to or what competitors run. Not for company facts (brand-product-research) or the strategy decision (advertising-strategy)."
---

# audience-market-analysis

## Purpose
Find the buyer, the buying motive and the gap in the category's advertising.

## Required inputs
Brand-product report; market / geography; competitor names if known.

## Workflow
1. Define 1-3 audience segments: who, situation, need, barrier, awareness level. Mark each line EVIDENCE (with source) or HYPOTHESIS.
2. List 3-6 competitors; for each open their site and their live ads in the free libraries (Meta Ad Library, Google Ads Transparency Center, TikTok Creative Center).
3. Log each competitor ad: format, length, hook, promise, proof, call to action, visual style. Link each one.
4. Summarise category conventions (what everyone does) and the open space (what nobody does).
5. Write `03-research/audience-market-report.md`.

## Expected outputs
`03-research/audience-market-report.md`: segments, competitor ad log with links, conventions, open space.

## Quality checklist
- [ ] No invented statistics or market sizes.
- [ ] Hypotheses are labelled.
- [ ] At least one real competitor ad linked per competitor, or UNKNOWN.

## Reuse - knowledge skills that own the details (load the one you need; do not copy them here)
ai-advertising-director (awareness levels, hooks), higgsfield-ad-tools-creator-academy-lessons-and-real-ad-budgets (Meta Ad Library research method).

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
