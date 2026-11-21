---
name: "advertising-social-media-specs-and-formats"
description: "PAID ad specs for social and Google platforms: Meta (Facebook, Instagram, Messenger, Threads, Audience Network), TikTok, YouTube ads and Google Ads campaign types, Pinterest, LinkedIn - ratios, resolution, lengths, file limits, text limits, safe zones in percent and pixels, music rules, and each platform's AI-content label rule for ads, with official links. Use when planning, exporting or checking a paid social or YouTube ad. Not for organic posting formats and label toggles (video-marketing-distribution) or TV and streaming specs. Hebrew triggers: מפרט מודעה, מודעה באינסטגרם, מודעת טיקטוק, מודעת יוטיוב, אזור בטוח, רילס ממומן, גוגל אדס."
---

# Social and Google paid ad specs and formats

Built 21 Nov 2026. All numbers were read on the official page on 20-21 Nov 2026 and re-read by a separate verifier on 21 Nov 2026 unless a row says otherwise. Platform specs change often: before delivery re-open the source link and say so to Moshe.
Branch of `advertising-and-media-hub`.

## Output rules for Moshe (hard)
- Answer in Hebrew, every message. Hebrew and English never on the same line: every English name, number label, path or link on its own line or in a code block.
- Never invent facts, prices, specs or rules; unverified -> say so.
- Never spend credits or buy anything without first stating in writing what and how much, and getting his explicit yes.
- Paid tools are never ruled out in advance: present them with cost, pros, cons, free alternative and a recommendation, and act only after his explicit approval.
- Never tell him "see section X": paste the text he needs. Do not end a reply with a question or an offer.
- Teach: define a new term once, the why in one sentence, numbered steps.

## Scope and routing
Owns: paid placements. Organic formats, upload toggles, organic AI labels -> `video-marketing-distribution`. Hooks, formats that sell, variants -> `ai-advertising-director`. Legal gate -> `ai-video-legal-consent-labels`. TV / streaming -> `advertising-tv-and-streaming-specs-israel-and-global`.

## 1. Meta video ads (Meta Ads Guide; max file 4 GB; MP4 or MOV; captions optional but recommended)
| Placement | Ratio | Resolution | Length | Text limits |
|---|---|---|---|---|
| Facebook Feed | 4:5 | 1440x1800 | 1 second to 241 minutes | primary 50-150, headline 27 |
| Facebook Stories | 9:16 | 1440x2560 | 1 second to 3 minutes | primary 125, headline 40 |
| Facebook Reels | 9:16 | 1440x2560 | no maximum | primary 40, headline 55 |
| Facebook in-stream | 16:9 or 1:1 | at least 1080x1080 | desktop 5-15 seconds; mobile 5 seconds to 10 minutes | primary 125, headline 40 |
| Instagram Feed | 9:16 | 1080x1920 | 1 second to 60 minutes | primary 125, up to 30 hashtags |
| Instagram Stories | 9:16 | 1440x2560 | 1 second to 60 minutes | primary 125 |
| Instagram Reels | 9:16 | 1440x2560 | up to 15 minutes | primary 44 |
| Messenger Stories | 9:16 | 1080x1920 | 1 to 60 seconds | primary 125, headline 40 |
| Audience Network rewarded | 9:16 | at least 1080x1080 | 3 to 61 seconds | captions not supported |
Image ads: JPG or PNG, max 30 MB; Feed 4:5 at 1440x1800; Stories and Reels 9:16 at 1440x2560.
Carousel: 2 to 10 cards; Facebook Feed 1:1; Instagram Feed 4:5 for images only, video carousels 1:1; Instagram Stories video cards 1 to 15 seconds.
Threads ads: video up to 500 seconds, 1440x1800 recommended, taller than 4:5 is cropped; captions not supported; carousel images only.
Source pattern: facebook.com/business/ads-guide/update/video/<placement> ; Threads: facebook.com/business/help/655859553779869

### Meta safe zones (9:16 Stories and Reels)
Keep text, logos and key elements out of: top 14%, bottom 35%, 6% on each side. Reels ads that carry disclaimers: keep the bottom 40% clear. Messenger Stories: about 14% (250 pixels) top and bottom. Source: facebook.com/business/help/980593475366490
### Meta rules that bite
- Instagram Reels ads should not contain licensed music (use original audio or the Meta Sound Collection), face effects, GIFs or product tags.
- AI label: Meta itself labels ad images made or significantly edited with AI ("AI info" in the ad's menu, sometimes next to the ad label); minor edits such as resizing or colour correction are not labelled; from 1 June 2026 it also detects third-party AI tools by industry signals. No advertiser self-disclosure duty is stated for ordinary commercial ads (INFERENCE from the two pages); political and social-issue ads MUST disclose realistic AI content.
- Special Ad Categories (financial products, employment, housing, social issues / politics) must be declared and limit targeting.

## 2. TikTok ads (ads.tiktok.com/help)
| Format | Spec |
|---|---|
| Auction in-feed (non-Spark) | 9:16 recommended (min 540x960), also 16:9 and 1:1; .mp4 .mov .mpeg .3gp .avi; up to 10 minutes; max 500 MB; bitrate at least 516 kbps |
| Reach and Frequency in-feed, TopView | 5-60 seconds, 9-15 recommended; max 500 MB; at least 2,500 kbps; TopView is 9:16 only and needs pre-approval (review within 2 days) |
| Spark Ads (boosting a creator's or brand's organic post) | no spec limits, the organic post must be 10 minutes or less; needs the creator's authorization code; caption comes from the post (4 lines shown) |
| Carousel | 2 to 35 images, JPG or PNG; music is mandatory |
| Profile | account name max 20 characters; photo 98x98 px under 50 KB |
Safe zone: TikTok publishes no percentages - only downloadable templates, including a right-to-left version; the zone shrinks as the caption gets longer.
Music: a business may not use the general music library; use the Commercial Music Library (pre-cleared, free).
AI content: significantly edited or AI-generated media is allowed only with the AIGC label or a clear disclaimer, caption, watermark or sticker; undisclosed AI content gets the ad "rejected or restricted" (policy page dated November 2026).
Claims: no promised or exaggerated results, no "Number 1" absolutes, no before-and-after comparisons, price must match the landing page.

## 3. YouTube ads (support.google.com/google-ads/answer/13547298 and 2375464)
General: the video must be uploaded to YouTube as public or unlisted; 1080p recommended (1920x1080, 1080x1920, 1080x1080); ratios 16:9, 9:16, 1:1 (4:5 accepted); max 256 GB; companion banner 300x60, max 150 KB, desktop only.
| Format | Length rule |
|---|---|
| Skippable in-stream | skip after 5 seconds; no maximum (under 3 minutes recommended); awareness :15-:20 |
| Non-skippable in-stream | 7 to 15 seconds; 16-30 seconds on connected TV only and horizontal only; policy limit 30 seconds in auction, 60 in reservation |
| Bumper | up to 6 seconds |
| In-feed | any length; 16:9 or 1:1 recommended; headline 2 lines of 40 characters, description 2 lines of 35 |
| Shorts ads | 9:16; keep under 60 seconds (Google's two pages disagree about longer ads); description 90 characters; call-to-action button appears at 3 or 10 seconds depending on campaign type |
| Masthead | reservation only; 16:9 at 1920x1080 or higher |
| YouTube TV (US) | :06, :15, :30, :60; a 30 must be :29 to :31 |
Vertical safe zone on 1080x1920: keep clear 288 px at the top, 672 px at the bottom, 48 px left, 192 px right. Horizontal 1920x1080: 38 px left and top, 162 px right, 387 px bottom.
Google's creative guideline (ABCD): Attention - jump in, tight framing, high contrast; Branding - early and often, in picture and in sound; Connection - people, feeling; Direction - one clear call to action, also spoken. Google also advises: online viewers drop after five seconds, so start high and keep several peaks; people watch at about half screen brightness.
AI label: since July 2026 Google lets advertisers add an AI label inside the creative; the advertiser can mark an asset as created or edited with AI, shown in "How this ad was made"; a visible on-ad label appears for campaigns targeting the European Union, India, New York, California, South Korea and Vietnam. Israel is not on that list. Loudness: no figure on Google Ads pages (UNKNOWN). Captions: no stated requirement (UNKNOWN).

## 4. Google Ads campaign assets
| Campaign | Key limits |
|---|---|
| Demand Gen video | 1-5 videos; min 5 seconds (under 10 cannot serve in-stream); 16:9, 1:1, 4:5, 9:16; headline 40, long headline 90, description 90; logo at least 144x144 |
| Demand Gen / Performance Max images | 1.91:1 1200x628; 1:1 1200x1200; 4:5 960x1200; 9:16 1080x1920 (Demand Gen); JPG or PNG max 5 MB |
| Performance Max | headlines 30 characters (one of 15 or less), long headlines 90, descriptions 90; videos 10 seconds or more, up to 15 |
| App campaigns | videos 10-60 seconds, 16:9 / 9:16 / 1:1, uploaded to YouTube |
| Uploaded display banners | GIF / JPG / PNG max 150 KB; common sizes 300x250, 336x280, 728x90, 300x600, 320x50, 320x100 |

## 5. Pinterest and LinkedIn
- Pinterest: image 2:3 at 1000x1500, title up to 100 characters; video MP4 / MOV / M4V up to 2 GB, 4 seconds to 15 minutes, 6-15 seconds recommended.
- LinkedIn video: MP4, 75 KB to 500 MB, 3 seconds to 30 minutes (15-30 seconds recommended), under 30 fps; 4:5 recommended; captions as SRT.
- Snapchat, X, Reddit: only search snippets were seen - UNVERIFIED, open the official page before use.

## 6. Export set for one campaign (INFERENCE from the tables)
1. 9:16 at 1080x1920 with text inside the Meta safe zone (the strictest percentages) - serves Reels, Stories, TikTok, Shorts.
2. 4:5 at 1440x1800 for Facebook and Instagram feeds.
3. 16:9 at 1920x1080 for YouTube in-stream and connected TV.
4. 1:1 at 1080x1080 for carousels and in-stream.
5. A 6-second and a 15-second cut next to the main length.

## General rule - recommend then teach
For any creative request first run `creative-request-advisor-tools-models-prices-then-teach-steps`: show the tool and model options (cheapest, most expensive, best quality, best value, free alternative) with live prices, commercial rights and one pick; wait for Moshe's choice; then guide him with the exact tool, settings and numbered steps from this skill.

## Open questions - verify before use
1. TikTok in-feed caption character limit and safe zone in pixels.
2. Snapchat, X and Reddit specs.
3. Whether YouTube's viewer-facing AI label appears on a video served as a paid ad.

## Lessons learned
- 21 Nov 2026: official pages of the same platform contradict each other (YouTube non-skippable length, Shorts over 60 seconds, AI-label regions); the policy page and the newest dated page win.
