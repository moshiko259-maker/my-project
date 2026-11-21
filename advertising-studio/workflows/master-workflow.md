# Master workflow (controlled by the Executive Producer)

```
client folder
   |
 [1 INTAKE] executive-producer ............ ad-project-intake
   |
 [2 RESEARCH] research-brand-strategist ... brand-product-research, audience-market-analysis
   |
 [3a STRATEGY] research-brand-strategist .. advertising-strategy ........ GATE strategy
 [3b CONCEPTS] creative-director .......... creative-concept-development  GATE concept
   |
 [4 SCRIPT] scriptwriter-story-architect .. ad-scriptwriting ............ GATE script
   |
 [5 STORYBOARD] storyboard-art-director ... visual-style-bible, product-fidelity,
   |                                        character-consistency, cinematic-storyboarding  GATE storyboard
   |
 [6a PLAN] ai-visual-production-director .. model-selection (GATE models), ai-prompt-engineering
 [6b BUDGET] executive-producer ........... production-budget-control ... GATE paid-images / paid-video / paid-audio / bulk-run
 [6c GENERATE] ai-visual-production-director  visual-production (one approved batch)
   |        ^
 [7 QC] quality-control-director .......... production-quality-control   (REGENERATE -> back to 6b)
   |
 [8 POST] post-production-delivery-director  post-production-delivery, campaign-variations
   |
 [9 DELIVERY] same ........................ final-report ................ GATE delivery, GATE publish
```

| Phase | Owner agent | Input | Output folder | Gate before the next phase |
|---|---|---|---|---|
| 1 Intake | executive-producer | client material | 01-brief, 02-original-assets | - |
| 2 Research | research-brand-strategist | 01-brief | 03-research | - |
| 3 Strategy + concepts | research-brand-strategist, creative-director | 03-research | 04-strategy, 05-concepts | strategy, concept |
| 4 Script | scriptwriter-story-architect | approved concept | 06-scripts | script |
| 5 Storyboard | storyboard-art-director | approved script | 07-storyboard | storyboard |
| 6 Visual production | ai-visual-production-director (+ producer for budget) | approved storyboard | 08-prompts, 09, 10 | models, paid-* |
| 7 Quality control | quality-control-director | outputs | 11-quality-control | - (rejections loop to 6) |
| 8 Post | post-production-delivery-director | QC-passed clips | 12-post-production | paid-audio if generated |
| 9 Delivery | post-production-delivery-director | finished versions | 13-final-delivery | delivery, publish |

Dependencies: no phase starts before the previous gate is APPROVED. Storyboard frame images are paid generations: they belong to phase 6 and need `paid-images`.
Free at any time: reading, research, writing, `higgsfield model list`, `higgsfield generate cost`, balance checks.
