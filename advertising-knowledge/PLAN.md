# PLAN - advertising knowledge base and skills (written 20 Nov 2026, waiting for OK)

## 1. Preconditions (owner decisions A-E in HANDOFF.md)
Network access is the main one: without it official pages cannot be opened and the verifier cannot do its job.

## 2. Sub-agent roles (each: free tools only, isolated browser, read-only, returns a report with source link + date + tag per fact; writes no files)
| # | Role | Output feeds |
|---|---|---|
| R1a | Media map: TV, cable, streaming / CTV | knowledge 01 |
| R1b | Media map: YouTube ads, Google Ads | knowledge 02 |
| R1c | Media map: Meta, TikTok, other social paid formats | knowledge 03 |
| R1d | Media map: DOOH, radio, podcasts, print, cinema, in-app, influencer | knowledge 04 |
| R2 | Israeli market: broadcast process, approvals, law basics, kids, VAT | knowledge 05, 06 |
| R3 | Production pipeline: stages, roles, timelines | knowledge 07 |
| R4a | Tools: AI video + image (plans, prices, free tiers, commercial rights, rankings) | knowledge 08 |
| R4b | Tools: voice, music, 3D, editing, design, storyboard, script | knowledge 09 |
| R4c | Connector inventory (free read-only calls only) | knowledge 10 |
| R5 | Business: pricing, quotes, contracts, usage rights, buyouts, clients | knowledge 11, 12 |
| R6 | Learning sources + full transcripts of key videos | knowledge 13, 14 |
| V1 | Verifier: prices and specs against official pages | knowledge 15 |
| V2 | Verifier: Israeli legal and tax facts against official pages | knowledge 15 |

## 3. Order
1. Wave 1 (parallel): R1a-R1d, R2, R3, R4a-R4c, R5, R6. Raw reports saved by the main agent to research-raw/.
2. Wave 2: main agent merges, removes what existing skills already own, writes knowledge files 01-14.
3. Wave 3: V1 + V2 re-check every price, spec and legal fact. Failed or unreachable = tagged UNKNOWN, never dropped silently.
4. Wave 4: main agent writes skill drafts; validates (publisher scripts A, B); builds edit lists for saved skills and proves each (script C).
5. Wave 5 (in a claude.ai chat - this cloud session has no save-card tool): cards in rounds of 3.
6. End: Hebrew summary, list of skills, open questions, lessons, HANDOFF.md update.

## 4. Skills to CREATE (8)
1. advertising-and-media-hub - routing table: brief type -> one owning skill.
2. advertising-tv-and-streaming-specs-israel-and-global
3. advertising-social-media-specs-and-formats (paid formats; organic stays in video-marketing-distribution)
4. advertising-outdoor-radio-podcast-print-cinema-in-app-specs
5. advertising-israel-broadcast-approvals-and-ad-law-basics
6. advertising-production-pipeline-brief-to-delivery
7. advertising-client-process-quotes-contracts-rights (process + usage rights / buyouts; the pricing method stays in ai-ad-pricing-and-selling)
8. creative-request-advisor-tools-models-prices-then-teach-step-by-step
Possible extra branches if a draft passes ~18 KB.

## 5. Skills to CHANGE
- Routing rows / links to the new hub: ai-video-project-workflow, ai-advertising-director, ai-ad-pricing-and-selling, ai-video-legal-consent-labels, video-marketing-distribution, ai-video-formats-catalog, ai-video-idea-advisor, ai-connectors-map, creative-ai-platforms-guide, higgsfield-hub, suno-and-ai-sound-hub, blender-hub (12).
- New verified facts go to the OWNING skill (for example new prices -> ai-video-tools-and-prices), never duplicated.
- "General rule - recommend then teach" section (about 6 lines) in every creative skill: about 105 skills = about 35 rounds of 3. Not possible for the 25 built-in skills. Recommended to skip the 6 retired pointers and the non-creative skills.
- Risk: about 25 skills already sit at 18.0-18.5 KB; the added section pushes them past ~18 KB. Proposal: keep the section short and treat +0.5 KB as within "about 18 KB"; split only skills that are far over.

## 6. Rough size
- 13 sub-agent runs, 15 knowledge files (each under ~45 KB), 8 new skills, about 105 edited skills, about 38 card rounds.
- Likely 3-5 sessions. Session 2 = waves 1-3. Session 3 = wave 4. Card rounds = separate claude.ai chats.

## 7. What will NOT be done
No purchase, trial, generation, publish or upgrade. No write to Drive or the owner's computer. No edit of saved skills except through save cards he presses himself.
