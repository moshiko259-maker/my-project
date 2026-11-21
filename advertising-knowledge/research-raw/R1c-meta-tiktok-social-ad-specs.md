<!-- RAW sub-agent report, UNVERIFIED. Saved by the main agent on 20 Nov 2026. Do not copy into a skill before the verifier pass. -->

R1c REPORT - paid ad creative specs (read 20-21 Nov 2026)

Method note: WebFetch could not resolve these hosts in this session; every OFFICIAL row below was read in full in my own headless Playwright Chromium (not logged in). Rows marked SNIPPET ONLY come from WebSearch result summaries, page not opened. Meta Ads Guide pages show no update date (footer "© 2026 Meta").

## 1. Findings

### 1A. Meta Ads Guide - VIDEO ads (all OFFICIAL; URL = https://www.facebook.com/business/ads-guide/update/video/<slug>)
All: max file size 4GB; captions "Optional, but recommended" unless noted; settings "H.264 compression, square pixels, fixed frame rate, progressive scan and stereo AAC audio compression at 128kbps+".

| Placement (slug) | File type | Ratio | Resolution | Duration | Text limits | Other |
|---|---|---|---|---|---|---|
| Facebook Feed (facebook-feed) | MP4, MOV or GIF | 4:5 | 1440 x 1800 | 1 second to 241 minutes | Primary 50-150 chars; Headline 27 | Min width/height 120 px |
| Facebook Stories (facebook-story) | MP4, MOV or GIF | 9:16 | 1440 x 2560 | 1 second to 3 minutes | Primary 125; Headline 40 | Min width 250 px; ratio tolerance 1%; safe zone below |
| Facebook Reels (facebook-facebook-reels) | MP4, MOV, GIF | 9:16 (recommended) | 1440 x 2560 | "No maximum limit." | Primary 40; Headline 55 | "Support for auto captioning: No"; sound "strongly recommended" |
| Ads on Facebook Reels / overlay (facebook-facebook-reels-overlay) | MP4, MOV | 1:1 (recommended) | 1440 x 1440 | Min 4 seconds, Max 15 seconds | Primary 60 | |
| Facebook in-stream (facebook-instream-video) | MP4, MOV or GIF | 16:9 or 1:1 | At least 1080 x 1080 | Desktop 5 seconds to 15 seconds; Mobile 5 seconds to 10 minutes ("may vary by objective") | Primary 125; Headline 40 | |
| Facebook Marketplace (facebook-marketplace) | MP4, MOV or GIF | 1:1 | At least 1080 x 1080 | 1 second to 241 minutes | Headline 25 | Min 120 x 120 px |
| Facebook Search results (facebook-search) | MP4, MOV or GIF | 1:1 | At least 1080 x 1080 | 1 second to 241 minutes | Primary 125; Headline 40; Description 30 | |
| Facebook right column (facebook-right-hand-column) | MP4, MOV or GIF | 1:1 (desktop or mobile) or 4:5 (mobile only) | 1440 x 1440 / 1440 x 1800 | 1 second to 241 minutes | Primary 50-150; Headline 27 | |
| Facebook Business Explore (facebook-biz-disco-feed) | MP4, MOV or GIF | 1:1 or 4:5 (mobile only) | At least 1080 x 1080 | 1 second to 241 minutes | Primary 125; Headline 27; Description 27 | |
| Instagram Feed (instagram-feed) | MP4, MOV or GIF | 9:16 | 1080 x 1920 | 1 second to 60 minutes | Primary 125; max 30 hashtags | Min width 250 px; tolerance 1% |
| Instagram Stories (instagram-story) | MP4, MOV or GIF | 9:16 | 1440 x 2560 | 1 second to 60 minutes | Primary 125 | Min width 250 px |
| Instagram Reels (instagram-reels) | MP4, MOV | 9:16 | 1440 x 2560 | 0 seconds to 15 minutes | Primary 44 | Min width 250 px (<30 s), 500 px (30 s or longer); sound "strongly recommended" |
| Instagram Explore home (instagram-explore-home) | MP4, MOV or GIF | 9:16 | 1080 x 1920 | 1 second to 60 minutes | Primary 125 | |
| Messenger Stories (messenger-story) | MP4, MOV or GIF | 9:16 | 1080 x 1920 | 1 second to 60 seconds | Primary 125; Headline 40 | Min width 500 px |
| Audience Network native (audience-network-native) | MP4, MOV or GIF | 9:16 | At least 1080 x 1080 | 1 second to 2 minutes | Primary 125; Headline 40; Description 30 | Captions "Not supported" |
| Audience Network rewarded (audience-network-rewarded-video) | MP4, MOV or GIF | 9:16 | At least 1080 x 1080 | 3 seconds to 61 seconds | same | Captions "Not supported" |

Instagram Reels ads "should not contain" (OFFICIAL, same Reels page): "Licensed music. We recommend using original audio or royalty-free music available in our Meta Sound Collection instead"; face or camera effect; GIF; product tags; edit lists or special boxes; Reels published before October 15, 2021.

### 1B. Meta - IMAGE ads (OFFICIAL; .../ads-guide/update/image/<slug>; max file 30MB, JPG or PNG)
| Placement | Ratio | Resolution | Text | Min size |
|---|---|---|---|---|
| Facebook Feed | 4:5 | 1440 x 1800 | Primary 50-150; Headline 27 | width 600 px; height 750 px (4:5); tolerance 3% |
| Facebook Stories | 9:16 | 1440 x 2560 | Primary 125; Headline 40 | width 500 px |
| Facebook Reels | 9:16 | 1440 x 2560 | Primary 40; Headline 55 | 600 x 600 px |
| Facebook right column | 1:1 | At least 1080 x 1080 | Headline 40 | 254 x 133 px |
| Facebook Search / in-stream | 1.91:1 to 1:1 | At least 1080 x 1080 | Primary 125; Headline 40; Description 30 | 600 x 600 px |
| Facebook Marketplace | 1:1 | At least 1080 x 1080 | Primary 125; Headline 40; Description 30 | - |
| Facebook video feeds | 1.91:1 to 4:5 | 1440 x 1440 / 1440 x 1800 | Primary 50-150; Headline 27 | width 600 px |
| Instagram Feed / Explore home | 4:5 | 1440 x 1800 | Primary 125; Headline 40; 30 hashtags | width 500 px; ratio range 400 x 500 to 191 x 100 |
| Instagram Stories | 9:16 | 1440 x 2560 | Primary 125 | width 500 px |
| Instagram Reels | 9:16 | 1440 x 2560 | Primary 44 | width 500 px |

### 1C. Meta - CAROUSEL and COLLECTION (OFFICIAL; .../carousel/<slug>, .../collection/<slug>)
| Item | Value |
|---|---|
| Carousel, Facebook Feed | 2 to 10 cards; 1:1; at least 1080 x 1080; Primary 80, Headline 20, Description 18; video 1 second to 240 minutes; image 30MB, video 4GB; landing page URL required |
| Carousel, Instagram Feed | 2 to 10 cards; "4:5 for carousels containing only images"; "for carousels containing videos, only 1:1 is supported"; Primary 125; video 1 second to 2 minutes |
| Carousel, Instagram Stories | 2 to 10 cards; 9:16; at least 1080 x 1920; Primary 125, Headline 40; video 1 second to 15 seconds |
| Collection, Facebook Feed / Instagram Feed | cover = first asset of the Instant Experience; ratio 1.91:1 to 1:1; at least 1080 x 1080; Primary 125, Headline 40; "Instant Experience: Required"; IG min 500 x 500 px |
| Collection, Instagram Stories | 1.91:1 to 1:1; Primary 125; Instant Experience required |
| Collection, Facebook Reels | 9:16 to 1:1; Primary 72; Headline 10; Instant Experience required |

### 1D. Meta - safe zones (OFFICIAL)
| Fact | Value | URL |
|---|---|---|
| 9:16 Stories/Reels (IG Reels, IG Stories, FB Stories, FB Reels collection) | leave "14% of the top, 35% of the bottom, and 6% on each side" free of text, logos, key elements | Ads Guide pages above |
| Reels ads with disclaimers | "leave the bottom 40% of your ad free from text, logos and other key creative elements" | https://www.facebook.com/business/help/980593475366490 |
| 9:16 video in Instagram Feed | "use the same safe zone guidance as Reels and Stories" | same |
| Non-9:16 Instagram Feed (1:1, 4:5) | keep bottom and side edges free | same |
| Taller-than-9:16 screens | creative may be zoomed (cropping outside safe zone) or shown with black background | same |
| Messenger Stories | "Leave roughly 14% (250 pixels) of the top and bottom of the video free from text and logos" | .../video/messenger-story |
| Tool | "Safe zone guardrail" toggle in Ads Manager (yellow overlay) | help/980593475366490 |

### 1E. Threads ads (OFFICIAL; https://www.facebook.com/business/help/655859553779869; no date)
| Fact | Value |
|---|---|
| Ads exist | Threads feed placement; default in Advantage+ placements; manual needs pairing with Instagram feed or Facebook feed |
| Image | JPG or PNG; 1.91:1 to 9:16 supported, taller than 4:5 cropped to 4:5; 1440 x 1440 recommended; min width 500 px |
| Video | MP4, MOV and GIF; 1.91:1 to 9:16, taller than 4:5 cropped to 4:5; 1440 x 1800 recommended; "Maximum video length: 500 seconds"; "Video captions are not supported" |
| Text | Primary 80 to 160 chars recommended, maximum 2,200; up to 30 hashtags; Headline 40; URLs not supported in primary text |
| Carousel | 2 to 10 cards; "limited to images only at this time" |
| Not delivered on Threads | Partnership ads, Collection, Instant Experience, dynamic creative, boosted Instagram posts; Advantage+ creative enhancements not applied (original creative used) |
| Change | "Starting in September 2026, matching usernames between Threads and Instagram profiles will no longer be required" |
| Label | ads previously labelled "Sponsored" now show "Ad" |

### 1F. Meta - AI disclosure, branded content, special categories (OFFICIAL)
| Fact | Value | URL / date |
|---|---|---|
| AI info label, scope | Meta labels "ad images created or significantly edited using our generative AI creative features or ad images created or edited using third-party AI tools with AI info"; significant edits "include background generation and image generation"; no label for "minor changes ... like image resizing or color correction" | https://www.meta.com/help/artificial-intelligence/355108217670024/ ("Updated: 4 days ago") |
| Where shown | "About this ad" screen in the ad's top-right menu; "Sometimes ... also appears next to the Sponsored label" | same |
| Third-party AI detection | Meta "will also begin automatically detecting ads created or edited using third-party AI tools through industry-standard signals"; label placed in About this ad | https://about.fb.com/news/2025/02/gen-ai-transparency-metas-ads-products/ (3 Feb 2025, updated June 1, 2026) |
| Commercial ads: advertiser self-disclosure duty | none stated on these pages for non-political ads (labelling is applied by Meta) | INFERENCE from the two pages above |
| Political/social issue ads | advertiser "must also disclose" photorealistic image/video or realistic audio "created or edited using third-party generative AI tools" that depicts a real person saying/doing what they did not, a realistic non-existent person or event, altered real footage, or a fake recording of an alleged event; non-disclosure = ad rejected, repeated = penalties | https://transparency.meta.com/policies/ad-standards/SIEP-advertising/SIEP/ (change log latest "Jul 2, 2026") |
| Same, automation | "beginning June 1, 2026, Meta will also use automated detection" and apply "AI Info" in About this Ad | same |
| Political ads | need authorization and verified "Paid for by" disclaimer; not allowed in the European Union (narrow election-authority exception); Israel listed among countries where ads must not discourage voting or question election legitimacy | same |
| Special Ad Categories | must be declared at campaign level: financial products and services (replaced Credit; required for US-based or US-targeted from January 21, 2025), employment, housing, social issues/elections/politics | https://www.facebook.com/business/help/298000447747885 |
| Targeting limits | for US-based/US-reaching, Canada and certain European countries: age, gender, ZIP/postal code, exclusions, lookalikes, saved audiences limited or unavailable | same |
| Political ads archive | entered into public Ad Library "for seven years" | same |
| Branded content | must be posted with the branded content tool, tagging the business partner with prior permission; creators cannot be paid to post content they do not feature in or did not help create | https://www.facebook.com/business/help/221149188908254 |
| Branded content prohibited | tobacco/vapes, drugs, unsafe supplements, weapons, adult products (except family planning), payday loans, multilevel marketing, ICOs/binary options/CFDs, state lotteries | same |
| Pre-authorization needed | dating, real money gambling, pharmacies, prescription drugs, cryptocurrency, drug and alcohol treatment centers, government/elections/politics | same |

### 1G. TikTok Ads (OFFICIAL; ads.tiktok.com/help/article/<slug> redirects to /resources/help/article/<slug>)
| Format | Spec | Slug / page date |
|---|---|---|
| Auction In-Feed, Non-Spark | 9:16 (recommended) ≥540*960px; 16:9 ≥960*540px; 1:1 ≥640*640px; .mp4, .mov, .mpeg, .3gp, .avi; "up to 10 minutes"; ≤500 MB; bitrate ≥516 kbps; captions: no clickable links, @ or hashtags | tiktok-auction-in-feed-ads / June 2026 |
| Auction In-Feed, Spark (Pull) | caption taken from organic post, max 4 lines displayed; .mp4 or .mov; duration "No restrictions" | same |
| Account name | one line, max 10 characters (Chinese, Japanese, Korean) or 20 characters other languages | same |
| Profile photo | 98x98px, 1:1; .jpg, .jpeg, .png; less than 50 KB; key element within central 66px*66px | same |
| Safe zone | no percentages published; downloadable zip templates (LTR standard; RTL "Arabic Version"); size depends on dimension, caption length, add-ons | same |
| Reservation In-Feed / Reach & Frequency | same three dimensions; .mp4, .mov, .mpeg, .3gp; "5-60s, recommend 9-15s"; ≤500 MB; bitrate ≥2,500kbps; longer caption = smaller safe zone | tiktok-reservation-in-feed-ads-reach-frequency / July 2025 |
| TopView | 9:16 ≥540*960px only; .mp4, .mov, .mpeg, .3gp; "5-60s, recommend 9-15s"; ≤500 MB; ≥2,500kbps; creatives need pre-approval; review within 2 days; same creative cannot run in other placements the same day; two safe zone files (open screen and in-feed; in-feed more restrictive) | tiktok-reservation-topview / October 2026 |
| Spark Ads | no restrictions on ratio, resolution, file type, duration, bitrate, file size; "10 minute maximum on videos that can be sparked"; display name and text not editable; max 10,000 Spark Ads per account; needs creator authorization code | spark-ads / June 2026 |
| Carousel (Standard) | 2 to 35 images; JPG/JPEG or PNG; ≤100 KB suggested; 1200*628px, 640*640px or 720*1280px; music mandatory (≥2s, .mp3, upload up to 10M or CML); one caption, one CTA, one URL | specifications-for-carousel-ads / September 2026 |
| Carousel (VSA / catalog) | 2 to 20 images shown; uploaded music only; per-product links | same |
| TikTok Ad Network (formerly Pangle) | video up to 10 minutes, 1280x720 / 720x1280 / 720x720, .mp4 .mov .mpeg .avi, 500MB; carousel up to 50 images, 100MB; playable .zip 5MB; image 1200x628 / 640x640 / 720x1280, 100MB | specifications-for-pangle-ad-assets / September 2026 |
| Branded Mission | advertiser name 24 English characters; mission name 70 (recommended 18); icon 240 x 240px, 500KB or less, PNG/JPG/JPEG; description up to 300 (recommended under 150) | branded-mission-ad-specs / July 2025 |
| Music | "Businesses cannot use the general music library for commercial usage"; must use Commercial Music Library (pre-cleared, "1 million songs", free) for organic business content, video ads, branded content; CML is not available on Ad Network carousel placements | commercial-music-library / July 2025; carousel page |
| AI-generated content | significantly edited media and AIGC allowed only if you "Apply the AIGC label, or ... a clear disclaimer, caption, watermark, or sticker of your own"; significant = fully AI-generated image/video/audio, subject shown doing or saying what they did not (incl. AI voice-cloning); insignificant = lighting/color, background removal, denoising; "If we identify AI-generated content that has not been disclosed, your ad will be rejected or restricted" | tiktok-ads-policy-misleading-and-false-content / November 2026 |
| Misleading claims | no promised or exaggerated results; no absolute terms ("Number 1 ... on TikTok"); no before-and-after effect comparisons; ad and landing page must match on price/discount; no fake play/close/CTA buttons; no use of a public figure's likeness without permission | same |
| Creator disclosure | commercial content disclosure setting must be turned on for posts promoting a brand, product or service | about-the-content-disclosure-setting-for-creators / April 2026 |
| Ads Manager AIGC toggle | "This ad contains AI-generated content" toggle; cannot be unselected after submission unless media changes; Symphony Creative Studio output auto-labelled | SNIPPET ONLY - https://ads.tiktok.com/business/library/AI_Safety_Essentials_for_Advertisers_on_TikTok.pdf |

### 1H. Other platforms
| Platform | Key numbers | Tag | URL / date |
|---|---|---|---|
| Pinterest standard image ad | .PNG or .JPEG; max 20 MB desktop, 32 MB in-app; 2:3, 1000 x 1500; title up to 100 chars (first 40 may show); description up to 800 | OFFICIAL | https://help.pinterest.com/en/business/article/pinterest-product-specs (no date) |
| Pinterest video ad (standard width) | .MP4, .MOV or .M4V; H.264 or H.265; up to 2GB; 4 seconds to 15 minutes, recommended 6 to 15 seconds; 1:1 or vertical (2:3, 4:5, 9:16) | OFFICIAL | same |
| Pinterest max. width video | paid only; cannot exceed height of 1:1; same file limits | OFFICIAL | same |
| LinkedIn video ads | MP4; H.264 or VP8; 75 KB to 500 MB; three seconds to 30 minutes (15-30 seconds recommended; in-stream up to 90 seconds); less than 30 FPS; 16:9 640 x 360 to 1920 x 1080; 1:1 360 x 360 to 1920 x 1920; 4:5 (recommended) 360 x 450 to 1080 x 1350; 9:16 360 x 640 to 1080 x 1920; captions SRT; thumbnail JPG/PNG max 2 MB | OFFICIAL | https://www.linkedin.com/help/lms/answer/a424737 ("Last updated: 4 months ago") |
| Snapchat single image/video | 1080px x 1920px, 9:16; 3-180 seconds; .mp4, .mov, .jpg, .png; brand up to 25 chars, headline up to 34 chars (from Story Ads page) | SNIPPET ONLY | https://businesshelp.snapchat.com/s/article/top-snap-specs ; https://forbusiness.snapchat.com/en-US/resources/advertising-guides/ad-specs |
| X video ads | max file 1GB ("strongly recommend ... under 30 MB"); recommended 15 seconds or less, max 2 minutes and 20 seconds; 9:16 for vertical, also 1:1, 4:5, 2:3, 16:9, 1.91:1 | SNIPPET ONLY | https://business.x.com/en/help/campaign-setup/creative-ad-specifications |
| Reddit video ads | MP4 or MOV (ProRes not supported); 1 GB; 30 FPS max; 2 seconds to 15 minutes, recommended 5-30 seconds; 1:1 1200x1200, 4:5 1200x1500, 16:9 1920x1080; headline 300 chars (recommended ≤ 100); Max campaigns video 100 MB | SNIPPET ONLY | https://business.reddithelp.com/s/article/video-ad-specifications |

## 2. Conflicts
- Meta Reels bottom safe zone: 35% (Ads Guide pages) vs 40% when the ad carries disclaimers (help/980593475366490). Both official; different cases.
- Meta 9:16 safe zone: 14% top / 35% bottom / 6% sides (Stories, Reels) vs Messenger Stories "14% (250 pixels) of the top and bottom" (.../video/messenger-story).
- Meta label name: AI help page and newsroom still say "Sponsored" label; Business Help pages say it now displays "Ad".
- TikTok bitrate: auction in-feed ≥516 kbps (tiktok-auction-in-feed-ads, June 2026) vs reservation/TopView ≥2,500kbps (July 2025 / October 2026).
- TikTok duration: auction non-Spark "up to 10 minutes" vs reservation and TopView "5-60s".
- TikTok Spark: "no restrictions on ... video duration" and "10 minute maximum" on the same page (spark-ads).
- TikTok Spark caption: "maximum of 4 lines can be displayed" (auction page) vs "no caption limit" (reservation/TopView pages).
- Snapchat brand name: 25 chars (Story Ads page) vs 32 chars (Story Ad specs page); video file size 1 GB vs other figures - SNIPPET ONLY, unresolved.

## 3. Could not open / UNKNOWN
- businesshelp.snapchat.com (top-snap-specs): page rendered empty in headless browser, twice (8 s and 20 s waits).
- business.reddithelp.com (Reddit-Ads-Specs): rendered only "Need Help?".
- business.x.com creative-ad-specifications: Cloudflare bot check; curl returned 403.
- Meta Ads Guide: no spec block rendered for carousel/instagram-reels, carousel/facebook-facebook-reels, carousel/facebook-story, collection/instagram-reels. Threads has no Ads Guide slug (specs are in the help article).
- UNKNOWN: Meta "About partnership ads" help article (guessed ID 404; search did not surface it) - only the Branded Content Policies page was read. Instant Experience component specs (https://en-gb.facebook.com/business/help/303060313519917 found, not opened). Advantage+ creative help page not read (only the Threads note).
- UNKNOWN: TikTok in-feed ad caption character limit (not stated on the pages read); TikTok safe zone in pixels/percent (only zip downloads, not opened); TikTok Shop ads / GMV Max creative specs (guessed slug 404); TikTok Ads Manager AIGC toggle help article (guessed slug 404, PDF not opened); Branded Mission video specs beyond profile fields (page text truncated at 2,200 chars).
- Meta in-stream page date and all Ads Guide dates: not shown.

## 4. Top 10 URLs for the verifier
1. https://www.facebook.com/business/ads-guide/update/video/instagram-reels
2. https://www.facebook.com/business/ads-guide/update/video/facebook-feed
3. https://www.facebook.com/business/help/980593475366490
4. https://www.facebook.com/business/help/655859553779869
5. https://www.meta.com/help/artificial-intelligence/355108217670024/
6. https://transparency.meta.com/policies/ad-standards/SIEP-advertising/SIEP/
7. https://ads.tiktok.com/help/article/tiktok-auction-in-feed-ads
8. https://ads.tiktok.com/help/article/tiktok-ads-policy-misleading-and-false-content
9. https://ads.tiktok.com/help/article/tiktok-reservation-topview
10. https://help.pinterest.com/en/business/article/pinterest-product-specs
(also: https://www.linkedin.com/help/lms/answer/a424737 ; https://www.facebook.com/business/help/298000447747885)
