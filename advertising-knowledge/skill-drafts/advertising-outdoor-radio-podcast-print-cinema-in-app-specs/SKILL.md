---
name: "advertising-outdoor-radio-podcast-print-cinema-in-app-specs"
description: "Specs and rules for ad media outside TV and social: outdoor billboards and digital screens, radio spots, podcast and Spotify audio ads, cinema ads, in-app and playable ads, and influencer disclosure rules - sizes, lengths, file formats, loudness, lead times and design rules, with the official source per item. Print is listed as not researched. Use when the ad will run on a billboard, radio, a podcast, in a cinema, inside an app, or through a creator. Not for TV, streaming or social feed ads. Hebrew triggers: שלט חוצות, מסך דיגיטלי, תשדיר רדיו, פרסומת בפודקאסט, ספוטיפיי, פרסומת בקולנוע, מודעה בתוך אפליקציה, משפיענים, גילוי נאות."
---

# Outdoor, radio, podcast, cinema, in-app and influencer specs

Built 21 Nov 2026. Numbers were read on the source on 20-21 Nov 2026 and re-read by a separate verifier on 21 Nov 2026 unless a row says otherwise. Media owners differ: always get the spec sheet of the specific screen, station or cinema chain. Sources here are US and UK bodies and owners - Israeli owners' specs are UNKNOWN (not searched).
Branch of `advertising-and-media-hub`.

## Output rules for Moshe (hard)
- Answer in Hebrew, every message. Hebrew and English never on the same line: every English name, number label, path or link on its own line or in a code block.
- Never invent facts, prices, specs or rules; unverified -> say so.
- Never spend credits or buy anything without first stating in writing what and how much, and getting his explicit yes.
- Paid tools are never ruled out in advance: present them with cost, pros, cons, free alternative and a recommendation, and act only after his explicit approval.
- Never tell him "see section X": paste the text he needs. Do not end a reply with a question or an offer.
- Teach: define a new term once, the why in one sentence, numbered steps.

## Scope and routing
Owns: the media below. Israeli law on outdoor signs, alcohol on billboards, radio approvals -> `advertising-israel-broadcast-approvals-and-ad-law-basics`. Radio and podcast production (voice, music, mix) -> `suno-and-ai-sound-hub`, `voice-audio-music`, `jingles-and-ad-songs-writing-method-with-suno`. AI influencers -> `ai-avatars-and-presenters`. Releases and labels -> `ai-video-legal-consent-labels`.

## 1. Outdoor and digital outdoor (DOOH)
Design rules: the driver sees a board for four to five seconds, so "seven words or less"; bold type, high contrast, one idea (Lamar design tips, VENDOR; OAAA blog).
| Item | Value | Source |
|---|---|---|
| US digital sizes (OAAA) | bulletin 7:2 = 400x1400 px; 3:1 = 600x1800; poster 21:10 = 400x840; street furniture 16:9 = 1920x1080 or 9:16 = 1080x1920; tolerance 3% | oaaa.org Digital Aspect Ratios PDF |
| Rotation | digital billboards change every six to eight seconds, six to eight advertisers per screen | oaaa.org/resources/digital-billboards |
| Lamar programmatic (US) | 6-10 seconds; most screens 1400x400 or 840x400; no QR codes | lamar.com programmatic media formats (VENDOR) |
| Bauer Media Outdoor UK street screens | static 1080x1920 portrait, 72 dpi, JPG / PNG, RGB, 1 MB; subtle animation only: MP4 / MOV H.264, 25 fps, 8 Mbit/s, 25 MB, 10-second slot, static backup required; no full-motion video; no sound; some cities static only | bauermediaoutdoor.co.uk Adshel Live specification (VENDOR) |
| JCDecaux UK roadside 48-sheet | static only, JPEG 612x306 px, 12 seconds; copy due 3 hours (1 file) to 5 working days (31-80 files) before playout | jcdecaux.co.uk (VENDOR) |
| OUTFRONT (US) | copy due at least ten working days before the start | outfront.com/posting-standards (VENDOR) |
| Printed billboard (OAAA cheat sheet, 2016) | 14'x48' bulletin: finished 15'x49', about 6 inches of bleed on all sides, artwork at 1 inch = 1 foot scale and 216-240 ppi | oaaa.org print cheat sheet |
Rules of thumb (INFERENCE from the rows): no sound, almost no motion near roads, RGB for screens, design at the screen's exact pixel size, and ask for the owner's deadline.

## 2. Radio
| Item | Value | Source |
|---|---|---|
| UK lengths | most common 30 and 40 seconds; any length in 10-second steps | radiocentre.org |
| UK clearance | scripts are pre-vetted by Radiocentre (audio not needed), usually within 24 hours; special categories (finance, gambling, alcohol, health, food claims, environmental claims and more) must be cleared | radiocentre.org/clearance |
| Delivery example (Bauer UK) | WAV 16 bit, 44.1 kHz, stereo, -12 dBFS; a 30-second spot must be 29.8 to 30.2 seconds; due 1 pm the day before | bauermedia.co.uk/audio-specifications (VENDOR) |
| Script length | Spotify's guidance: no more than 65 words for 30 seconds, 100 words for 60 seconds | ads.spotify.com audio ad specs |
| Broadcast loudness (EBU R128 s1, short form) | -23.0 LUFS, max short-term -18.0 LUFS, max true peak -1 dBTP | tech.ebu.ch/docs/r/r128s1.pdf |
Israel: radio ads on regional stations and Kan follow the Israeli rules in the Israel branch; station delivery specs UNKNOWN.

## 3. Podcast and streaming audio
| Item | Value | Source |
|---|---|---|
| Spotify audio ad | max 30 seconds (music and podcast); MP3, WAV or OGG; max 50 MB; 44.1 kHz; 192-320 kbps; stereo; -16 LUFS (+/-1.5) | ads.spotify.com/en-US/ad-specs/audio-ad-specs |
| Spotify companion | square image min 600x600, 200 KB; advertiser name 25 characters, tagline 40 | same |
| Spotify video ad | up to 30 seconds; 9:16 or 16:9; MOV or MP4; max 500 MB; audio RMS -14 dBFS, peak -0.2 dBFS; must have sound | ads.spotify.com in-stream video specs |
| Host-read ads | arranged through a Spotify representative | ads.spotify.com podcast specs |
| Apple Podcasts loudness | about -16 dB LKFS (+/-1 dB), true peak not above -1 dB FS | podcasters.apple.com/support/893-audio-requirements |
| Megaphone | MP3, 44.1 kHz or higher, -16 LUFS recommended, ads match the episode's stereo / mono | support.megaphone.fm article 1561164 |
| Acast | 30-second advertiser-made audio ads; all ads normalised to -18 LUFS; host-read sponsorship messages are not normalised | learn.acast.com glossary (21 Sep 2026) |
| Ad types (IAB Podcast Measurement v2.3, September 2026) | integrated = host-read or static, baked into the episode, everyone gets the same ad; dynamically inserted = targeted and inserted when the episode is requested | iabtechlab.com podcast measurement guidelines |
Note: broadcast radio (-23 LUFS) and podcast (-16 LUFS) need two different mixes.

## 4. Cinema
| Item | Value | Source |
|---|---|---|
| DCM (UK) picture | supply a TIFF image sequence, not QuickTime: 1998x1080 (2K flat) or 1920x1080, also 4K; 24 fps (25 is slowed to 24 and runs 4% longer); Rec.709; no clock, no black frames; title safety 1798x972 at 2K | DCM Cinema Production Requirements 2026 (VENDOR) |
| DCM sound | a 5.1 mix is always required (six mono WAV, 48 kHz, 24 bit); fails above 82 dB Leq(m); stereo-only fails | same |
| DCM text and clearance | minimum text height 16 pixels (18 recommended); Cinema Advertising Association approval for every ad, about 24 hours; allow 48 hours for assets | same |
| Pearl and Dean Ireland | 1998x1080, 24 fps, 5.1, max 82 Leq(m), lead time 5-10 working days | pearlanddean.ie spec 2026 (VENDOR) |
| Screenvision (US) pre-show | ProRes 422 HQ, 1920x1080, 24 fps, stereo or 5.1, 78 Leq(m); trailer position 82 Leq(m) and both flat 1998x1080 and scope 2048x858 | Screenvision 2024 spec (VENDOR) |
| NCM (US) | ProRes 422 HQ 1920x1080 at 23.976, 5.1; not above -24 LKFS, peaks not above -10 dBFS | ncm.com spec PDFs (VENDOR) |
Trailers have a separate limit: 85 Leq(m) (TASA). Ads: 82 Leq(m), cited by two cinema ad sellers from the SAWA standard (the SAWA document itself was not opened).
Meaning: cinema needs a 24 fps master, a real 5.1 mix and its own loudness measure (Leq(m)) - plan it before the mix, not after.

## 5. In-app and playable ads
| Network | Video | Playable |
|---|---|---|
| Unity Ads | 60 seconds or less; H.264 MP4; 16:9 or 9:16; 10 MB recommended, 100 MB max; end card mandatory | one index.html under 5 MB, all assets inlined, no network requests, MRAID 3.0 |
| AppLovin | MP4 / MOV, 9:16, max 60 seconds, max 1 GB | single HTML file, 5 MB or smaller, MRAID v2.0, muted until first interaction |
| Meta (incl. Audience Network) | rewarded video 3 to 61 seconds | single HTML max 5 MB or ZIP of at most 100 files; must work WITHOUT mraid.js |
| Google AdMob | app campaign videos 10-60 seconds | - |
A playable needs three separate builds for Unity, AppLovin and Meta. Sources: docs.unity.com grow / acquire creatives; support.applovin.com creative specs and guidelines; facebook.com/business/help/412951382532338.

## 6. Influencer and creator campaigns - disclosure
| Where | Rule | Source |
|---|---|---|
| UK (ASA / CAP and CMA guide, 4th edition, 23 Oct 2026) | an influencer includes "any human, animal or virtually produced persona"; use a clear upfront label such as #Ad; "Sponsored", "Spon", "Sp" or only tagging the brand is not enough; affiliate links count as advertising | asa.org.uk influencers guide |
| UK on AI | "no blanket legal requirement in the UK to disclose the use of AI in ads"; the test is whether the audience would be misled | asa.org.uk, 29 May 2025 |
| US (FTC Endorsement Guides, 2023) | an endorser may "be or appear to be an individual, group, or institution" - covers virtual influencers; disclosure must be "difficult to miss" | Federal Register 88 FR 48092 |
| EU | brand partnerships, free products and affiliate marketing must be disclosed | commission.europa.eu influencer legal hub |
| EU AI Act Article 50 (official text on eur-lex; applies from 2 August 2026) | whoever deploys AI content that is a deep fake - content that resembles existing persons, objects, places or events and would falsely appear authentic - must disclose that it was artificially generated or manipulated; for evidently artistic, creative or fictional work the disclosure may be made in a way that does not hamper the work. Fines up to EUR 15 million or 3% of turnover. Relevant only when people in the EU see the ad; details -> ai-video-legal-consent-labels | Regulation (EU) 2024/1689, Art. 3(60), 50, 99 |
| Platform tools | Instagram: paid partnership label; TikTok: commercial content disclosure setting; YouTube: paid promotion box | platform help pages |
| TikTok Spark Ads | the brand runs the creator's post with the creator's authorization code; agree the code's duration in the contract | ads.tiktok.com/help/article/spark-ads |
Israel: a publication that looks like editorial content without a clear advertisement mark is deemed misleading (Consumer Protection Law s.7, read on a community copy of the law).

## 7. Print - basics (read 21 Nov 2026 by a gap-fill researcher; not re-read by a verifier)
| Item | Value | Source |
|---|---|---|
| File standard | PDF/X-1a (ISO 15930-1 and -4): CMYK only, no transparency. PDF/X-4 (ISO 15930-7): colour-managed, transparency allowed | US Library of Congress format pages |
| Bleed | 3 mm outside the trim line (UK) / 0.125 inch (US) | one printer's two country sites |
| Total ink limit | coated offset Europe (FOGRA51) 300%; GRACoL 320%; SWOP 300%; newsprint 240% | ICC profile registry |
| Resolution | magazines: photos 300 dpi at actual size, line art 600 dpi; newspapers: 200-300 dpi depending on the publisher | single publishers' spec sheets |
| Colour | CMYK; the profile is named by the publication | same |
Always ask the publication or printer for its own sheet: profile, ink limit, resolution and ad sizes differ. Standard ad unit names: no standards list was found.

## General rule - recommend then teach
For any creative request first run `creative-request-advisor-tools-models-prices-then-teach-steps`: show the tool and model options (cheapest, most expensive, best quality, best value, free alternative) with live prices, commercial rights and one pick; wait for Moshe's choice; then guide him with the exact tool, settings and numbered steps from this skill.

## Open questions - verify before use
1. Israeli outdoor, radio and cinema media owners' specs.
2. Print rows rest on single publishers and one printer; standard ad unit names not found.
3. Talent and voice-over usage fees: union rate sheets exist for the US only; no Israeli equivalent found.

## Lessons learned
- 21 Nov 2026: each medium has its own loudness measure (LUFS for broadcast and podcast, Leq(m) for cinema); a single mix cannot serve all.
