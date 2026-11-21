---
name: ad-scriptwriting
description: "Phase 4 script: the approved concept written as a timed two-column audio/visual script with hook, voiceover or dialogue, supers and call to action, plus short cut-down versions. Use when a script, voiceover, dialogue or cut-downs are needed. Not for camera and lighting design (cinematic-storyboarding)."
---

# ad-scriptwriting

## Purpose
A script that can be read against a stopwatch and shot without guessing.

## Required inputs
Approved concept; strategy; target lengths; language.

## Workflow
1. Fix lengths (master and cut-downs) and language. Hebrew copy goes through `hebrew-proofreading`.
2. Write the master in `templates/script-av.md`: time code, VISUAL, AUDIO (VO / dialogue / SFX / music), on-screen text.
3. Hook in the first 2-3 seconds; brand or product visible early; one call to action.
4. Read the voiceover aloud against the time codes; trim until it fits without rushing. Record the word count per version.
5. Write cut-downs as their own scripts, not as trims described in a sentence.
6. List every claim in the script with its source in facts.md.
7. Stop for owner approval (gate `script`).

## Expected outputs
`06-scripts/script-master.md`, `script-<length>.md`, `claims-check.md`.

## Quality checklist
- [ ] Timing adds up to the target length.
- [ ] No unverified claim.
- [ ] Each cut-down stands alone.
- [ ] On-screen text is short enough to read in its time.

## Reuse - knowledge skills that own the details (load the one you need; do not copy them here)
cinematic-writing, ai-advertising-director (hooks by awareness level), jingles-and-ad-songs-writing-method-with-suno, hebrew-proofreading.

Templates: `advertising-studio/templates/`. Stage map and gates: `advertising-studio/workflows/master-workflow.md`.

## Hard rules (every stage)
- Never invent facts, prices, specs, product details or model capabilities. Unverified = write UNKNOWN and say what was tried.
- No paid generation, purchase, upgrade, publish or send without a recorded approval (see `production-budget-control`).
- Paid tools are never ruled out in advance: present cost, pros, cons, free alternative and a recommendation; act only after the owner's explicit yes.
- Recommend then teach: first the tool/model options (cheapest, most expensive, best quality, best value, with live prices and a pick), then, after the owner chooses, exact settings and numbered steps.
- Reply to the owner in Hebrew; Hebrew and English never on the same line. Files and prompts are in English.
- Never delete or overwrite the owner's files. Work only inside the client project folder and `advertising-studio/`.
