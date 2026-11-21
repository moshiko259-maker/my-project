---
name: advertising-strategy
description: "Phase 3 strategy: one page that fixes objective, audience, single message, proof, tone, media and success measure before any idea is written. Use after research and before concepts, or when a brief is vague. Not for the ideas themselves (creative-concept-development) or media specs (model and platform specs live in the knowledge base)."
---

# advertising-strategy

## Purpose
One decision page so every concept is judged against the same target.

## Required inputs
Both research reports; brief; owner's goal.

## Workflow
1. Write the diagnosis in two sentences: what stops the buyer today.
2. Fill `04-strategy/strategy.md` from `templates/strategy.md`: objective, audience, the one thing to say, reasons to believe (only VERIFIED facts), tone, mandatories, what must never be claimed.
3. Choose media and lengths; copy the platform specs from `advertising-knowledge/knowledge/` with their source links, or mark UNKNOWN.
4. State how success would be judged, and what is out of scope.
5. Ask the owner to approve the strategy (gate `strategy`).

## Expected outputs
`04-strategy/strategy.md` (one page).

## Quality checklist
- [ ] Exactly one main message.
- [ ] Every reason to believe traces to facts.md.
- [ ] Media choice lists length, ratio and spec source.

## Reuse - knowledge skills that own the details (load the one you need; do not copy them here)
ai-advertising-director (diagnosis, awareness), ai-video-formats-catalog (format shapes), video-marketing-distribution (organic formats).

Templates: `advertising-studio/templates/`. Stage map and gates: `advertising-studio/workflows/master-workflow.md`.

## Hard rules (every stage)
- Never invent facts, prices, specs, product details or model capabilities. Unverified = write UNKNOWN and say what was tried.
- No paid generation, purchase, upgrade, publish or send without a recorded approval (see `production-budget-control`).
- Paid tools are never ruled out in advance: present cost, pros, cons, free alternative and a recommendation; act only after the owner's explicit yes.
- Recommend then teach: first the tool/model options (cheapest, most expensive, best quality, best value, with live prices and a pick), then, after the owner chooses, exact settings and numbered steps.
- Reply to the owner in Hebrew; Hebrew and English never on the same line. Files and prompts are in English.
- Never delete or overwrite the owner's files. Work only inside the client project folder and `advertising-studio/`.
