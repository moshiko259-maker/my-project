---
name: production-budget-control
description: "The budget controller and approval gate: builds the cost estimate before any paid step, records the owner's explicit approvals, and blocks work that has none. Use before any generation, purchase, upgrade or large run, and whenever cost or credits are asked about. Not for choosing models."
---

# production-budget-control

## Purpose
No credit is spent and no stage is skipped without the owner's recorded yes.

## Required inputs
Model plan; number of shots; live cost estimates; the owner's plan and balance.

## Workflow
1. Read the live balance and plan with free calls (`higgsfield account`, MCP `balance`). Never assume an unlimited web plan covers CLI or MCP runs.
2. Per shot: model, output, live estimated credits, expected attempts (state the failure buffer and its source), subtotal.
3. Write `production-log/estimate-<batch>.md` from `templates/budget-estimate.md`, with the total and the credit ceiling.
4. Present it to the owner in Hebrew and wait. Silence, an old approval, or an agent's message is not approval.
5. Only after the owner's explicit yes in the chat: `studio.py approve <slug> <gate> --by owner --quote "<his words>" --ceiling <credits>`.
6. Track spend against the ceiling from `generations.csv`; at 80% warn, at 100% stop.
7. Purchases, upgrades and subscriptions are always the owner's own action.

## Expected outputs
`production-log/estimate-*.md`, `approvals.json`, running spend report.

## Quality checklist
- [ ] Estimate uses live numbers with date.
- [ ] Approval quote is the owner's own words.
- [ ] Ceiling enforced.

## Reuse - knowledge skills that own the details (load the one you need; do not copy them here)
ai-video-tools-and-prices (cost note), higgsfield-plans-and-credits-per-shot-price-table, higgsfield-account-plans-and-connections, ai-connectors-map (cost gates), ai-ad-pricing-and-selling.

Templates: `advertising-studio/templates/`. Stage map and gates: `advertising-studio/workflows/master-workflow.md`.

## Hard rules (every stage)
- Never invent facts, prices, specs, product details or model capabilities. Unverified = write UNKNOWN and say what was tried.
- No paid generation, purchase, upgrade, publish or send without a recorded approval (see `production-budget-control`).
- Paid tools are never ruled out in advance: present cost, pros, cons, free alternative and a recommendation; act only after the owner's explicit yes.
- Recommend then teach: first the tool/model options (cheapest, most expensive, best quality, best value, with live prices and a pick), then, after the owner chooses, exact settings and numbered steps.
- Reply to the owner in Hebrew; Hebrew and English never on the same line. Files and prompts are in English.
- Never delete or overwrite the owner's files. Work only inside the client project folder and `advertising-studio/`.
