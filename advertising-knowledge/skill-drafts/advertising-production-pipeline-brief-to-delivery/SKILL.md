---
name: "advertising-production-pipeline-brief-to-delivery"
description: "The professional ad production pipeline from client brief to delivery, adapted for a solo AI creator: stages in order, the purpose, inputs, documents, owner and approval gate of each, what a good brief contains, script timing, storyboard and animatic terms, review rounds, deliverables matrix, which agency and crew roles Moshe performs alone, timelines, and where to learn each stage. Use at the start of any client ad job or when asking what comes next, who does what, or which document is needed. Not for platform specs, prices or contract clauses (sibling branches). Hebrew triggers: תהליך הפקה, מבריף עד מסירה, מה השלב הבא, אנימטיק, סבבי תיקונים, רשימת תוצרים, מי עושה מה."
---

# Ad production pipeline - brief to delivery

Built 21 Nov 2026. [V] = re-read on the source by a separate verifier on 21 Nov 2026. [D] = found in research on 20-21 Nov 2026, not re-read. [C] = a creator's or vendor's own claim. Stage structure is common industry practice; numbers carry their tag.
Branch of `advertising-and-media-hub`.

## Output rules for Moshe (hard)
- Answer in Hebrew, every message. Hebrew and English never on the same line: every English name, number label, path or link on its own line or in a code block.
- Never invent facts, prices, specs or rules; unverified -> say so.
- Never spend credits or buy anything without first stating in writing what and how much, and getting his explicit yes.
- Paid tools are never ruled out in advance: present them with cost, pros, cons, free alternative and a recommendation, and act only after his explicit approval.
- Never tell him "see section X": paste the text he needs. Do not end a reply with a question or an offer.
- Teach: define a new term once, the why in one sentence, numbered steps.

## Scope and routing
Owns: the order of work and the documents. Specs per medium -> the three specs branches. Contract, payment, rights -> `advertising-client-process-quotes-contracts-rights`. Price -> `ai-ad-pricing-and-selling`. Strategy and hooks -> `ai-advertising-director`. Brand film from a website -> `client-brand-film-production`. In Claude Code the same pipeline runs as the advertising studio (8 agents and gates) in the owner's repository.

## The pipeline
| # | Stage | Purpose | Output document | Owner skill | Gate |
|---|---|---|---|---|---|
| 1 | Client brief | fix goal, audience, budget, deliverables | written brief, 1-2 pages | this skill, section "Brief" | client signs the brief |
| 2 | Research and strategy | one message, proof, tone, media | one-page strategy | ai-advertising-director | Moshe approves |
| 3 | Concepts | 3 different routes, one recommended | concept sheets | ai-advertising-director, cinematic-director | client picks one |
| 4 | Script | timed audio / visual script, cut-downs | two-column script | cinematic-writing | client approves in writing |
| 5 | Storyboard and animatic | every shot decided before spending | shot list, storyboard, animatic | seedance-shotlist-director, ai-3d-previs-blocking | client approves |
| 6 | Pre-production | models, references, budget, schedule | production doc, credit estimate | ai-video-tools-and-prices, higgsfield-hub | Moshe's written yes to spend |
| 7 | Production | generate, shoot or animate | selects | higgsfield-hub and craft skills | quality check per shot |
| 8 | Offline edit | story and timing | rough cut, fine cut | ai-video-post-production | review rounds, then picture lock |
| 9 | Finishing | colour, effects, titles, legal text | graded master | ai-video-post-production | - |
| 10 | Sound | voice, music, effects, mixes per medium | mixes | voice-audio-music, suno-and-ai-sound-hub | licences recorded |
| 11 | Versions | lengths, ratios, languages | deliverables matrix filled | specs branches | - |
| 12 | Legal gate and delivery | releases, labels, claims; hand over files | delivery package, usage terms | ai-video-legal-consent-labels | client sign-off; final payment |

## Brief - what a good one contains
ISBA guide (updated March 2023) [V]: briefing has three stages - clarifying, writing, meeting; the written brief is short and "acts as a contract". Example components: Timeline; Key Stakeholders; Deliverables and Scope; Challenges; Target Audience; Budget ("ballparks are very useful"); KPIs; Background.
IPA / BetterBriefs study (UK, 2022) [D]: 26% of marketing budget is wasted on poor briefs; only 6% of agencies feel clear on strategic direction - so asking questions is normal, not rude.
Add for AI work (INFERENCE): which real products, logos and people appear and who supplies the files; whether AI use is accepted; where it will run.

## Script timing
- A two-column script: picture on one side, sound on the other, timed by reading aloud [D].
- About 65-85 words of voice-over fit 30 seconds (voice-over marketplace blog) [C]; Spotify's own guidance is no more than 65 words for 30 seconds and 100 for 60 [V].
- Legal text on screen (UK broadcast model) [V]: hold 0.2 seconds per word plus 2 seconds (up to 9 words) or 3 seconds (10 or more).

## Storyboard family - terms
Storyboard = still frames. Animatic = the frames cut to time with rough sound. Rip-o-matic = a mood film cut from existing footage (reference only - never delivered). Previz = rough 3D version that fixes camera and blocking. [D, general references]

## Pitching and bidding (US / UK models)
- No more than three bidders; a treatment needs at least a week [D].
- A bid = price, letter, treatment and / or storyboards; unawarded treatments stay the maker's property [D].
- Do not start before a contract or purchase order [D].

## Edit and review
Stages: assembly -> rough cut -> fine cut -> picture lock; after lock no editorial changes, so colour, sound and finishing can start (Frame.io workflow guide) [D]. Show a client a polished cut, not a rough assembly [D]. No trade body sets a number of review rounds; two to three is commonly reported [C] - fix the number in the contract.

## Deliverables matrix (fill before the edit)
Rows = version x length x ratio x language x with / without text. Columns = container and codec, resolution and frame rate, loudness, captions, slate, file name, destination, spec source link. Cut-downs (60 -> 30 -> 15 -> 6) and each ratio are separate deliverables and are priced as such (the AICP bid form has its own "Social Versions" section) [D].

## Roles - who Moshe is at each stage (INFERENCE)
Strategist and copywriter (stages 2-4); art director and storyboard artist (5); producer - budget, schedule, rights (1, 6, 12); director and "camera" through prompting (7); editor, colourist, sound (8-10); quality control (every stage). He cannot be: the client's approver, the lawyer, the media buyer, the broadcaster's clearance.

## Timelines
- Traditional 30-second TV commercial: six to twelve weeks is reported by one production blog [C]; a live shoot is usually one to three days [C].
- AI-made spots: vendors and creators report days, not weeks - for example "2-5 production days" [C] and a two-day national spot whose creator says he made 300-400 generations for 15 usable clips [C, press]. Treat as claims; time the first job and log it.
- Payment milestones (trade-body models) [V]: 75% on award / 25% on delivery for post-production work; details in the client-process branch.

## What the tested creators say about the AI stage (videos read in full by the researcher, 21 Nov 2026; creators' own claims) [C]
1. Assets first - characters, locations, objects - before any shot ("garbage in equals garbage out").
2. Ask the model for camera position, movement and timing for every shot.
3. Draft at low resolution first, then finish only the chosen takes.
4. Generate a few extra seconds at the start and end of each shot for the edit.
5. Expect most generations to be discarded; plan the budget for it.
6. The last 5-10% of polish takes as long as the first 80%.
7. Hook in the first one and a half seconds; no slow opener.

## Where to learn each stage (free unless noted; pages seen 20-21 Nov 2026)
| Topic | Source |
|---|---|
| Effective video ads (ABCD) | Google's ABCD guide and YouTube's official videos |
| Paid social creative | Meta Blueprint, TikTok Academy (both state free courses) |
| AI advertising workflow | Runway Academy "AI for Advertising" (10 modules, free enrol); Higgsfield Academy (free to watch) |
| Edit, colour, sound | Blackmagic DaVinci Resolve official training videos and books |
| Producing | StudioBinder "Stages of Filmmaking" series |
| Contracts and bidding documents | AICP guidelines |

## General rule - recommend then teach
For any creative request first run `creative-request-advisor-tools-models-prices-then-teach-steps`: show the tool and model options (cheapest, most expensive, best quality, best value, free alternative) with live prices, commercial rights and one pick; wait for Moshe's choice; then guide him with the exact tool, settings and numbered steps from this skill.

## Open questions - verify before use
1. Rows tagged [D] and [C] have not been re-read by a verifier.
2. Israeli agency practice (pitch, pre-production meeting, approval rounds): no source found.
3. A measured timeline for Moshe's own AI spot: log the first real job.

## Lessons learned
- 21 Nov 2026: most "AI ad in two days" numbers come from sellers or creators; they are useful as a range, not as a promise to a client.
