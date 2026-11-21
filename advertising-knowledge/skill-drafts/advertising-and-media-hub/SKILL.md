---
name: "advertising-and-media-hub"
description: "Central entry point for any client advertising brief in any medium: a routing table that sends each brief type and each advertising question to the ONE branch skill that owns it (TV and streaming specs, social paid specs, outdoor / radio / podcast / cinema / in-app specs, Israeli broadcast approvals and ad law, production pipeline, client process and rights), plus the existing ad skills. Use when Moshe brings a client brief or asks where an advertising answer lives. Not for the answers themselves. Hebrew triggers: בריף, לקוח רוצה פרסומת, פרסומת לטלוויזיה, קמפיין, מפרט מודעה, איזה סקיל פרסום, פרסום בכל מדיה."
---

# Advertising and media hub - read this, then load ONE branch

Built 21 Nov 2026. This hub holds no specs, prices or legal facts. It only routes. One question -> one owner.

## Output rules for Moshe (hard)
- Answer in Hebrew, every message. Hebrew and English never on the same line: every English name, spec, path or link on its own line or in a code block.
- Never invent facts, prices, specs or rules; unverified -> say so. Legal content is not legal advice.
- Never spend credits or buy anything without first stating in writing what and how much, and getting his explicit yes.
- Paid tools are never ruled out in advance: present them with cost, pros, cons, free alternative and a recommendation, and act only after his explicit approval.
- Never tell him "see section X": paste the text he needs. Do not end a reply with a question or an offer.
- Teach: the why in one sentence, numbered steps.

## How to use (every advertising task)
1. Find the row. 2. Load that ONE skill. 3. For tools, models and prices run `creative-request-advisor-tools-models-prices-then-teach-steps` first. 4. Before anything leaves the computer: `ai-video-legal-consent-labels`.

## Routing by brief type
| Brief | First skill | Then |
|---|---|---|
| "Company A wants a 30-second TV ad" | advertising-production-pipeline-brief-to-delivery | advertising-tv-and-streaming-specs-israel-and-global; in Israel also advertising-israel-broadcast-approvals-and-ad-law-basics |
| Streaming / connected-TV ad (Netflix, Prime Video, Disney, Roku, YouTube on TV) | advertising-tv-and-streaming-specs-israel-and-global | ai-advertising-director |
| Social campaign, paid (Meta, TikTok, YouTube ads, Google Ads, Pinterest, LinkedIn) | advertising-social-media-specs-and-formats | ai-advertising-director (hooks, variants) |
| Organic social posting, AI-label toggles | video-marketing-distribution | - |
| Brand film from a client's website | client-brand-film-production | advertising-production-pipeline-brief-to-delivery |
| Billboard / digital outdoor, radio spot, podcast ad, cinema ad, in-app / playable ad, print | advertising-outdoor-radio-podcast-print-cinema-in-app-specs | sound: suno-and-ai-sound-hub |
| Influencer / creator campaign, disclosure rules | advertising-outdoor-radio-podcast-print-cinema-in-app-specs (influencer part) | ai-avatars-and-presenters for AI influencers |
| Jingle or ad song | jingles-and-ad-songs-writing-method-with-suno | ad-music-licensing-stock-libraries-and-sfx-sources-verified |
| UGC-style, product ad, ad variations | ai-advertising-director | higgsfield-marketing-studio-ads-studio-ad-multiplier-ugc-ads |

## Routing by question
| Question | Owner |
|---|---|
| Lengths, ratios, file format, loudness, captions, safe zones for a platform | the specs branch for that medium (three branches above) |
| How does an ad get on TV or radio in Israel; approvals; what may not be advertised; kids; VAT and invoices | advertising-israel-broadcast-approvals-and-ad-law-basics |
| Stages, who does what, documents, timelines, review rounds, deliverables matrix | advertising-production-pipeline-brief-to-delivery |
| Client process, proposal sections, contract clauses, usage rights, buyouts, AI clauses, payment milestones | advertising-client-process-quotes-contracts-rights |
| How much to charge; quote in Hebrew; sales call | ai-ad-pricing-and-selling |
| Finding clients, business setup | ai-business-starter |
| Strategy, truth gate, hooks, formats, packshot, credit budget | ai-advertising-director |
| Which format | ai-video-formats-catalog |
| Which tool or model and its price | creative-request-advisor-tools-models-prices-then-teach-steps -> ai-video-tools-and-prices |
| Releases, AI labels, copyright, spec ads | ai-video-legal-consent-labels |
| Music and SFX licences for ads | ad-music-licensing-stock-libraries-and-sfx-sources-verified |
| Where to learn advertising craft | video-teacher (and the learning list kept with the pipeline branch) |

## Where the source knowledge lives
Repository folder `advertising-knowledge/knowledge/` (one topic per file, every fact with source, date and tag; `15-verification-log.md` shows what passed re-checking). Raw reports: `advertising-knowledge/research-raw/`.

## Open questions - verify before use
1. Print advertising specs were not researched (no branch owns them yet).
2. Israeli broadcasters' technical delivery specs were not found on any public page.

## Lessons learned
- 21 Nov 2026: organic social formats stay in video-marketing-distribution; this family covers paid media and broadcast only, to avoid two owners.
