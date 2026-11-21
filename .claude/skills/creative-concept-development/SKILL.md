---
name: creative-concept-development
description: "Phase 3 ideas: at least three clearly different ad concepts grounded in the product truth, each scored for originality, feasibility and cost, with one recommendation. Use when ideas, routes, concepts or a big idea are requested. Not for the full script (ad-scriptwriting) or shot design (cinematic-storyboarding)."
---

# creative-concept-development

## Purpose
Give the owner real choices, not three versions of one idea.

## Required inputs
Approved strategy; facts; competitor conventions.

## Workflow
1. Write 6-10 raw ideas fast, then discard any that could run for a competitor unchanged.
2. Develop at least 3 concepts with different mechanisms (for example: demonstration, human story, visual metaphor, category reversal).
3. For each, fill `templates/concept.md`: title, one-line idea, why it fits this brand only, opening image, story in 4 beats, emotional and commercial logic, product role, risks, feasibility with AI video (hard shots named), rough production size.
4. Score each 1-5 on originality, brand fit, clarity in 3 seconds, feasibility, cost; show the table.
5. Recommend one, say why, and what would change the pick.
6. Stop for owner approval (gate `concept`).

## Expected outputs
`05-concepts/concept-1..n.md` and `05-concepts/comparison.md`.

## Quality checklist
- [ ] Concepts differ in mechanism, not only in setting.
- [ ] No concept needs a claim that is not VERIFIED.
- [ ] Hard-to-generate actions are flagged before approval.

## Reuse - knowledge skills that own the details (load the one you need; do not copy them here)
ai-advertising-director (hooks, format recipes), cinematic-director, cinematic-writing, ai-video-idea-advisor, ai-video-lessons-tree (hard-action check).

Templates: `advertising-studio/templates/`. Stage map and gates: `advertising-studio/workflows/master-workflow.md`.

## Hard rules (every stage)
- Never invent facts, prices, specs, product details or model capabilities. Unverified = write UNKNOWN and say what was tried.
- No paid generation, purchase, upgrade, publish or send without a recorded approval (see `production-budget-control`).
- Paid tools are never ruled out in advance: present cost, pros, cons, free alternative and a recommendation; act only after the owner's explicit yes.
- Recommend then teach: first the tool/model options (cheapest, most expensive, best quality, best value, with live prices and a pick), then, after the owner chooses, exact settings and numbered steps.
- Reply to the owner in Hebrew; Hebrew and English never on the same line. Files and prompts are in English.
- Never delete or overwrite the owner's files. Work only inside the client project folder and `advertising-studio/`.
