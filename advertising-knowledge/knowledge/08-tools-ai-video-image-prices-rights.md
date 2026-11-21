# 08 - AI video and image tools: plans, prices, rights, rankings

Read: 20-21 Nov 2026. STATUS: DRAFT - NOT YET VERIFIED. Do not copy any number into a skill until `15-verification-log.md` shows it PASS.
Tags per fact: OFFICIAL / VENDOR / COMMUNITY / INFERENCE / UNKNOWN. "SNIPPET ONLY" = seen in a search result, page not opened.
Origin: sub-agent report `research-raw/R4a-tools-ai-video-image-prices-rights.md`, reformatted only (no fact added or removed by the main agent).

R4a REPORT - AI video / image tools: plans, prices, rights, rankings. Pages read 20 Nov 2026 (terms-clause batch 20-21 Nov). Method: headless Playwright Chromium on each official page. WebFetch failed DNS for nearly every host; WebSearch was not used. Several sites show Black Friday promos, so "promo" prices are temporary.

Coverage is partial. Not obtained: Higgsfield prices, Adobe Firefly, OpenAI/ChatGPT, Ideogram, Leonardo, LMArena, Hailuo and Dreamina plan tables, Google Flow per-model credit costs. Details in section 3.

## 1. FINDINGS

### 1a. Video platforms - plans (USD as shown)
| Platform | Plans: monthly / annual-billing price per month; credits | Free tier | Tag | URL |
|---|---|---|---|---|
| Runway | Standard $15 / $12, 625 cr/mo. Pro $35 / $28, 2250 cr/mo. Max $95 / $76, 9500 cr/mo, credits roll over 1 mo. Yearly "-20% off". Min top-up 1,000 credits | Free $0, 125 one-time credits, 5GB. "No watermarks" is listed from Standard | VENDOR | runway.com/pricing (runwayml.com redirects) |
| Kling | Monthly tab, "Limited-Time 35% Off" first 3 months: Standard $6.5 (list $10, then $8.8/mo), 660 cr/mo. Pro $24 (list $37, then $32.56), 3000 cr. Premier $135 (list $207, then $181.99), 18000 cr (slider 8K-38K). Ultra+ $402 (list $619, then $544.99), 57000 cr. Yearly tab "Limited-Time 50% Off" not read | Not shown on plan page: UNKNOWN | VENDOR | kling.ai/app/membership/membership-plan |
| Luma | Plus $30/month, 10,000 cr. Pro $90, 40,000 cr. Ultra $300, 150,000 cr. "Save up to 20% with yearly" (yearly figures not read). Team/Enterprise: contact | No free plan shown on page | VENDOR | lumalabs.ai/pricing |
| Pika | Starter $10 / $8, 600 cr. Creator $35 / $28, 2,600 cr. Fancy $95-$880 / $76-$704, 8,550 cr and up (slider to 79k). Team: $35 or $95 per seat, 2-seat minimum | Free: "0 · credit packs only", all models, "No watermark", Commercial license "No" | VENDOR | pika.art/pricing |
| Google AI (Flow / Veo / Gemini) | AI Plus $4.99/mo. AI Pro $19.99/mo. AI Ultra "From $99.99/mo". Extra Flow credits per month: Plus 200, Pro 1,000, "Ultra $100" 10,000, "Ultra $200" 25,000 | 50 Flow credits/day with or without subscription; non-subscribers may be unable to generate video at peak hours (about 2-5 PM UTC) | OFFICIAL | one.google.com/about/google-ai-plans/ ; support.google.com/flow/answer/16526234 |
| Midjourney (image + video) | Basic $10 / $96 yr ($8/mo), 3.3 hr fast GPU. Standard $30 / $288 ($24), 15 hr. Pro $60 / $576 ($48), 30 hr. Mega $120 / $1,152 ($96), 60 hr. Extra GPU $4/hr | None listed | OFFICIAL | docs.midjourney.com/hc/en-us/articles/27870484040333 |
| LTX Studio | Lite $15 / $12 (billed yearly $144), 8,000 cr/mo. Standard $35 / $28 ($336), 28,000. Pro $125 / $100 ($1,200), 110,000 | Free $0, 800 credits one time, "Personal use license". "No watermarking" listed from Lite | VENDOR | ltx.io/studio/pricing (ltx.studio redirects) |
| OpenArt | Starter $14 / $11, 4,000 cr. Plus $34 / $24, 12,000. Pro $56 / $36, 24,000. Wonder $240 / $144, 106,000. Annual shown under "up to 40% off" promo | "Start for Free"; details not read | VENDOR | openart.ai/pricing |
| Krea | Basic $9 / $5 yearly, 5,000 units. Pro $42 / $21 ($252 billed yearly), 20,000. Max $140 / $42 ($504), 60,000 (slider 40k-100k). Business $200 / $96, 80k units, up to 50 seats. Yearly shown as "70% off" promo | Free $0, 100 units/day | VENDOR | krea.ai/pricing |
| Freepik (redirects to magnific.com) | Premium $20 / $14.50, 240K credits/year. Plus $45 / $33.75, 600K/yr. Pro $110 / $82.50, 1.5M/yr (4M option). Credits valid 1 year. Prices exclude VAT | Not read | VENDOR | magnific.com/pricing |
| Wan (Alibaba) | Pro US$10 monthly / US$5 billed yearly, 300 cr/mo ("up to 1200 images or 60 videos"). Premium US$40 / US$20, 1200 cr/mo. Web-app only; API bought separately | Free US$0, 1 concurrent job, daily check-in credits. Watermark-free download, 1080p and 10-30s clips listed only on paid | VENDOR | create.wan.video/pricing |
| Grok Imagine | Plus $8/month, Premium $30, Super $100, Ultra $200. Annual toggle rendered the same figures as "/year" (likely a display glitch). Image/video creation listed from Premium | Not shown | VENDOR | grok.com/plans |
| HeyGen | Creator $29/mo, 600 credits, 1080p. Pro $49/mo, 1,000 credits, 4K, Seedance 2.5 and Veo 3.1 access. "Yearly 2 months free" | Free: 3 videos/month, watermarked, up to 1 minute each | VENDOR | heygen.com/pricing |
| Synthesia | Starter $19 / $14 ($168 billed yearly), 15,000 credits/year. Pro $89 / $59 ($708), 72,000/year | Basic $0, 500 credits/month, Synthesia watermark, 10 min video/month | VENDOR | synthesia.io/pricing |
| Kolbo.ai | Lite $27/mo ($21.60 first month), 2,500 cr. Standard $45 ($36), 4,500. Professional $89 ($53.40), 9,500 (multipliers to "Max"). Credits roll over up to 3x. Annual prices not read | Free $0, 50 monthly credits, "Includes ads" | VENDOR | app.kolbo.ai/pricing |
| Higgsfield | Prices not readable (page rendered navigation only). Help centre: individual plans plus Team/Scale/Enterprise, monthly or annual; page metadata names "Basic Pro Ultimate Creator" | Free: $0, no monthly credits, limited models (e.g. Nano Banana Pro, FLUX.2 Pro), one generation at a time, "can carry a visible Higgsfield watermark"; Credit Packs need a subscription | OFFICIAL | higgsfield.ai/creator-hub/help-center/plans/what-does-the-free-plan-include (dated Nov 11, 2026) |
| MiniMax Hailuo | Home page only: "From $9.99/mo" | New users get free credits (amount not read) | VENDOR | hailuoai.video |
| Dreamina (ByteDance) | Plan table not reachable. Home shows Seedream 5.0 Pro at "12/image", "16/image" credits | UNKNOWN | VENDOR | dreamina.capcut.com |

### 1b. Per-second / per-clip costs published on the pages
| Where | Model and setting | Cost | Tag |
|---|---|---|---|
| Runway | Gen-4.5 | 12 credits/second (60 credits/5s) | VENDOR |
| Runway | Aleph 2.0 | 140 credits/5s | VENDOR |
| Runway | Kling 4.0 1080p | 118 credits/5s (89 with 25% off until November 30) | VENDOR |
| Runway | Seedance 2.0 Pro 1080p | 160 credits/4s | VENDOR |
| Runway | Gen-4 Image 1080p / Nano Banana Pro 2K | 8 / 20 credits per image | VENDOR |
| Luma | Ray3.2 text/image-to-video | 360p 20, 540p 50, 720p 100, 1080p 400 credits per 5 sec (10 sec: 60/150/300/1200). HDR 2x, HDR+EXR 3x | VENDOR |
| Luma | Seedance 2.5 | 480p 36, 720p 78, 1080p 191 credits/sec | VENDOR |
| Luma | Kling 4.0 | 720p 53, 1080p 79 credits/sec | VENDOR |
| Luma | Veo 3.1 | 140 credits/sec (720p or 1080p) | VENDOR |
| Luma | Kling 3.0 / Seedance 2.0 at 4K | 147 / 261 credits/sec | VENDOR |
| Pika | Pika H3 Flex 768p 5s | 10 credits | VENDOR |
| Pika | Seedance 2.5 5s | 480p 54, 720p 122, 1080p 299 credits | VENDOR |
| Kolbo | Seedance 2.5, clips 4-30s | 4s: 480p 92, 720p 196, 1080p 440, 4k 732 credits. 30s 720p: 1,470 | VENDOR |
| Magnific | Kling 2.5 720p / Wan 3.0 720p | 140 credits/5s / 200 credits/2s | VENDOR |
| Midjourney | Video GPU cost, batch 1 | SD 2 mins, HD 7 mins (batch 4: 8 / 26 mins). Starts at 5 s, extend +4 s up to 4 times, max 21 s. SD = 480p | OFFICIAL |
| fal.ai | Seedance 2.5 text-to-video | 480p $0.2205, 720p $0.4730, 1080p $1.164, 4K $1.840 per second; "up to 30 seconds" | VENDOR |
| fal.ai | Kling v3 Pro / Kling 2.5 turbo pro | $0.14 / $0.07 per second | VENDOR |
| fal.ai | MiniMax H3 Max / H3 Max Turbo | $0.03 / $0.015 per second | VENDOR |
| fal.ai | Nano Banana 2 / Nano Banana Pro | $0.08 / $0.15 per image | VENDOR |
| Replicate | wan-2.1-i2v 480p / 720p (only video rows read) | $0.09 / $0.25 per second | VENDOR |
| BFL API | FLUX 3 Image | 1K $0.048, 2K $0.10, 4K $0.607 per image | VENDOR |
| BFL API | FLUX 3 Image Klein | 1K $0.009 per image | VENDOR |

Sources: runway.com/pricing, lumalabs.ai/pricing, pika.art/pricing, app.kolbo.ai/pricing, magnific.com/pricing, docs.midjourney.com/hc/en-us/articles/37460773864589-Video, fal.ai/pricing, fal.ai/models/bytedance/seedance-2.5/text-to-video, replicate.com/pricing, bfl.ai/pricing.

Google Flow (OFFICIAL, support.google.com/flow/answer/16352836):
- Current models are Omni Flash 1.2 and Veo 3.1 Lite. Veo 3.1 Lite is 720p, clips of 4s/6s/8s.
- Omni 360p costs one-third the credits of 720p.
- "On December 5, 2026, Veo 3.1 Fast, Veo 3.1 Quality, and Omni Flash 1.1 will be retired."
- Veo Extend was retired November 5, 2026; extending now needs a subscription and Omni Flash 1.2.

### 1c. Image-only plans
| Platform | Plans | Free tier | Tag | URL |
|---|---|---|---|---|
| Recraft | Basic $10/mo billed annually ($120; Black Friday $6.00 / $72.00), 1,000 cr/mo. Pro $16 ($192; BF $9.60), 2,000 cr (slider to 16k), adds video. Teams $17.58 per seat. Monthly-billing prices not read. Excl. VAT. Promo "Ends Dec 1" | "Personal use only", "No commercial use", "All images are public", 3 generations per style per day | VENDOR | recraft.ai/pricing |
| Canva | Pro US$18/month (US$9 for first 3 months promo). Business US$25 per person (US$12.50 promo). Yearly "Save from 16%" | Free US$0, "Limited access to Standard and Premium AI" | VENDOR | canva.com/pricing/ |
| FLUX (BFL) | API pay-per-image (see 1b). Open-weights licences: Builder 10K images/month, Platform 100K, prices not read | - | VENDOR | bfl.ai/pricing |
| Midjourney, Krea, Magnific, Google, Grok | See 1a | | | |

### 1d. Commercial use, watermark, training, indemnity
| Platform | Rule as shown | Tag | URL / page date |
|---|---|---|---|
| Runway | "The Company does not claim ownership of any of your Inputs or Outputs. Subject to your compliance with the Agreement, the Company does not restrict your commercial use of your Outputs." No tier distinction in this clause. Also: "Inputs and Outputs may be used by the Company to train and improve its AI models" | OFFICIAL | runway.com/terms-of-use, last updated October 23, 2026 |
| Luma | Customer may not "use the Services or Output for commercial purposes, unless permitted to do so under Section 4.9". Trial output "only ... for your internal evaluation". "If you use any Output that identifies or resembles a person, you will publicly identify that such Output was AI generated." Pricing page lists "Commercial use" from Plus | OFFICIAL | lumalabs.ai/legal/terms-of-service, last updated May 14, 2026 |
| Midjourney | "If you have subscribed at any point, you are free to use your images/videos in just about any way you want. You must purchase the Pro or Mega plan if you are a company making more than $1,000,000 USD in gross revenue per year." Stealth Mode only on Pro and Mega | OFFICIAL | docs.midjourney.com/hc/en-us/articles/27870484040333 |
| Kling | All four paid plans list "Generated content is for commercial use" and "Brand watermark removal". Free tier: UNKNOWN | VENDOR | kling.ai membership page |
| Pika | Commercial license: Free "No"; Starter, Creator, Fancy "Yes" | VENDOR | pika.art/pricing |
| LTX Studio | Free "Personal use license". "Commercial use license" appears first under Standard, not Lite | VENDOR | ltx.io/studio/pricing |
| OpenArt | "Commercial use rights" listed on Plus, Pro, Wonder; not on Starter. "Watermark-free" on all paid | VENDOR | openart.ai/pricing |
| Krea | "Commercial license" from Basic. "Indemnification" listed on Business and Enterprise only | VENDOR | krea.ai/pricing |
| Magnific/Freepik | "Commercial AI license" and "No model training on your data" on Premium; Plus and Pro add "music rights" | VENDOR | magnific.com/pricing |
| Recraft | Free "No commercial use"; Basic "Commercial rights and private generations" | VENDOR | recraft.ai/pricing |
| Higgsfield | Terms last updated October 23, 2026; has sections "4.4 User Inputs and Outputs", "5.5 AI Disclosure", "6.4 Provenance and Watermarking". Clause text not extracted: UNKNOWN | OFFICIAL | higgsfield.ai/terms-of-use-agreement |
| Google | Generative AI Prohibited Use Policy bars content that "Violates the rights of others, including privacy and intellectual property rights" | OFFICIAL | policies.google.com/terms/generative-ai/use-policy, last modified December 17, 2024 |
| HeyGen / Synthesia | Free outputs watermarked; removal on paid. Commercial clause not read | VENDOR | pricing pages |

### 1e. Rankings - Artificial Analysis arenas (COMMUNITY: independent site, Elo from human preference votes)
No page date is printed. Benchmark version "v2.1"; newest listed models are dated Nov 2026. Price column is AA's figure for the creator's API.

| # | Text-to-Video (Elo, price) | Image-to-Video (Elo, price) | Text-to-Image (Elo, price) |
|---|---|---|---|
| 1 | Wan 3.0, 1176, $12.00/min | Dreamina Seedance 2.5, 1161, $34.12/min | GPT Image 2.6 Sunburst (max), 1261, $210.72/1k imgs |
| 2 | Utopai X, 1170, no API | Utopai X, 1151, no API | GPT Image 2.5 Sunburst (max), 1230, $210.72 |
| 3 | MiniMax H3 (768p), 1161, $4.80/min | Boreal-H3, 1148, $2.42/min | GPT Image 2.6 Flare (max), 1227, $210.72 |
| 4 | Dreamina Seedance 2.5, 1157, $34.12/min | Dreamina Seedance 2.0, 1141, $22.45/min | MAI-Image-2.7, 1215, $34.82 |
| 5 | Hyperflow H3, 1155, coming soon | MiniMax H3 (768p), 1134, $4.80/min | GPT Image 2.5 Flare (max), 1211, $210.72 |
| 6 | Gemini Omni Flash 1.2, 1154, $6.26/min | SkyReels V4, 1125, $21.00/min | GPT Image 2 (high), 1193, $211.00 |
| 7 | FLUX 3 Max, 1150, $8.70/min | HeyGen Video 1, 1124, $2.40/min | Kling Image 4.0, 1181, $63.00 |
| 8 | HeyGen Video 1, 1148, $2.40/min | Hyperflow H3, 1119, $9.00/min | Nano Banana 2.1, 1177, $33.60 |
| 9 | MiniMax H3 Max, 1145, $9.60/min | P-Video-2-Pro, 1117, $5.70/min | MAI-Image-2.6, 1168, $38.91 |
| 10 | FLUX 3, 1138, $14.40/min | MiniMax H3 Max, 1116, $9.60/min | Grok Imagine Image 2.0, 1167, $60.00 |

- Confidence intervals are about ±12-18, so ranks 1-4 overlap on both video boards.
- Lower down, T2V: Grok Imagine Video 1.5 1050; Kling 3.0 1080p (Pro) 1000 (anchor); Veo 3.1 963; LTX-2.5 Pro 937.
- Lower down, T2I: Seedream 5.5 1134; Nano Banana Pro 1119; FLUX 3 Image 1116; Recraft V4.1 Utility 1027; Ideogram 4.0 (Quality) 1026.
- Kling 4.0 video and Midjourney do not appear in the rows read.
- URLs: artificialanalysis.ai/video/leaderboard/text-to-video ; .../video/leaderboard/image-to-video ; .../image/leaderboard/text-to-image

## 2. CONFLICTS
| Item | Value A | Value B |
|---|---|---|
| Seedance 2.5 API price | AA: $34.12/min (about $0.569/s), "1080p where offered" | fal.ai: 720p $0.4730/s, 1080p $1.164/s |
| Google AI Ultra price | one.google.com: "From $99.99/mo" | support.google.com/flow: "Ultra $100" and "Ultra $200" tiers |
| Seedance 2.5 720p cost through resellers | Luma 78 credits/sec on $30 per 10,000 credits | Pika 122 credits per 5s on $35 per 2,600; Kolbo 196 credits per 4s on $27 per 2,500 |
| Freepik brand | Task names Freepik | freepik.com/pricing redirects to magnific.com/pricing |
| Grok annual price | Monthly tab: $8 / $30 / $100 / $200 per month | Annual tab rendered the same numbers as "/year" |
| Kling 4.0 in Runway | 118 credits/5s list | 89 credits/5s promo until November 30 |

## 3. COULD NOT OPEN / UNKNOWN
- Adobe Firefly (www.adobe.com/products/firefly/plans.html, helpx.adobe.com, firefly.adobe.com/plans): "Access Denied" or blank. Plans, credits and indemnity UNKNOWN.
- OpenAI (openai.com/chatgpt/pricing, chatgpt.com/pricing, help.openai.com): blank render. ChatGPT plans, GPT Image limits, Sora, indemnity UNKNOWN.
- Ideogram, Leonardo (pricing pages) and LMArena (redirects to arena.ai; three leaderboards): Cloudflare bot check. UNKNOWN.
- Higgsfield pricing: page rendered navigation only, even with a 20 s wait. Plan prices, credits, per-model cost and commercial clause UNKNOWN.
- Kling terms and free tier; Pika terms (login wall); Midjourney ToS (404 at /terms-of-service); Kolbo terms (empty render); Krea terms (commercial clause not located).
- Hailuo and Dreamina/CapCut plan tables (redirect to home).
- Google Flow per-model credit costs; Veo / Gemini API price; Google indemnity terms.
- x.ai returned 403. fal.ai Kling 4.0 model page rendered blank. Replicate prices for current top models not read.
- Not researched: Seedream plans, Stable Diffusion / ComfyUI licence, Luma yearly prices, Kling yearly prices, Kolbo annual prices.
- A free reader proxy (r.jina.ai) was blocked by the session's permission system.

## 4. TOP 10 URLS FOR THE VERIFIER
1. artificialanalysis.ai/video/leaderboard/text-to-video
2. artificialanalysis.ai/video/leaderboard/image-to-video
3. artificialanalysis.ai/image/leaderboard/text-to-image
4. runway.com/pricing and runway.com/terms-of-use
5. lumalabs.ai/pricing and lumalabs.ai/legal/terms-of-service
6. kling.ai/app/membership/membership-plan
7. pika.art/pricing
8. support.google.com/flow/answer/16526234 and one.google.com/about/google-ai-plans/
9. docs.midjourney.com/hc/en-us/articles/27870484040333-Comparing-Midjourney-Plans
10. fal.ai/models/bytedance/seedance-2.5/text-to-video and fal.ai/pricing

## 5. SUMMARY TABLES (from the findings above only)

A. Cheapest paid entry per category (list monthly-billing price unless noted)
| Category | Plan | Price | Commercial use per page |
|---|---|---|---|
| Video, multi-model | Google AI Plus | $4.99/mo (200 Flow credits) | Not stated on page |
| Video, multi-model | Krea Basic | $9/mo ($5 yearly promo) | "Commercial license" |
| Video, single vendor | Kling Standard | $10 list ($6.5 promo) | "for commercial use" |
| Video, single vendor | Pika Starter | $10 | "Commercial license" |
| Video, single vendor | Wan Pro | US$10 (US$5 yearly) | Not stated |
| Image | Midjourney Basic | $10 ($8 annual) | General Commercial Terms |
| Image | Recraft Basic | $10/mo billed annually ($6.00 BF) | "Commercial rights" |
| Avatar | Synthesia Starter | $19 ($14 yearly) | Not read |
| Avatar | HeyGen Creator | $29 | Not read |

B. Most expensive individual tier seen
| Platform | Tier | Price |
|---|---|---|
| Pika | Fancy, top of slider | $880/mo ($704 annual) |
| Kling | Ultra+ | $619 list ($402 promo, then $544.99) |
| Luma | Ultra | $300/month |
| OpenArt | Wonder | $240 ($144 annual promo) |
| Grok / Google | Ultra | $200 |

C. Top-ranked model today (Artificial Analysis, COMMUNITY)
| Board | #1 | Elo |
|---|---|---|
| Text-to-video | Wan 3.0 | 1176 ±12 |
| Image-to-video | Dreamina Seedance 2.5 | 1161 ±15 |
| Text-to-image | GPT Image 2.6 Sunburst (max) | 1261 ±14 |

D. INFERENCE - "best value" candidate: Seedance 2.5 at 720p (ranked #1 image-to-video, #4 text-to-video)
| Route | Arithmetic | Cost per second |
|---|---|---|
| Luma Plus | $30 / 10,000 credits = $0.003 per credit; x 78 credits/sec | about $0.234 |
| Pika Creator | $35 / 2,600 = $0.01346 per credit; x 122 credits / 5 s | about $0.328 |
| Pika Starter | $10 / 600 = $0.01667 per credit; x 122 / 5 s | about $0.407 |
| fal.ai API | published rate | $0.4730 |
| Kolbo Lite | $27 / 2,500 = $0.0108 per credit; x 196 credits / 4 s | about $0.529 |

- Candidate: Luma Plus, at list price, with "Commercial use" shown on the plan.
- Caveats: Luma's own "Cost Per Video Generation" table and plan credits are the only inputs. Krea and OpenArt advertise temporary Seedance discounts whose per-second cost could not be computed, and Higgsfield and Dreamina prices are unknown, so this is not a full-market comparison.
- Lower-cost alternative with a native model: Runway Max annual, $76 / 791 s of Gen-4.5 = about $0.096 per second (Standard annual: $12 / 52 s = about $0.231). Gen-4.5 does not appear in the leaderboard rows read.
