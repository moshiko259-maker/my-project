<!-- VERIFIER report V1, saved by the main agent 21 Nov 2026. Independent re-read of files 01-04. -->

VERIFIER V1 REPORT - files 01-04 re-read against live pages, 21 Nov 2026. Method: curl (browser UA) + headless Playwright Chromium; PDFs via pdftotext; accordions clicked (Netflix); YouTube safe-zone SVGs rendered and read visually. No logins, no MCP web tools. Temp cache in scratchpad deleted; no project file written.

Overall: 0 FAIL in 185 fact groups re-read. Two source URLs now redirect (values unchanged). "same" = page text matches the draft exactly.

## File 01 - TV / streaming / CTV
URL keys: NF advertising.netflix.com/en-us/creative-specs | AMZ advertising.amazon.com/resources/ad-specs/dsp/video/streaming-tv-prime-video-ads | DIS products.disneyadvertising.com/video-commercial/ | ROKU help.ads.roku.com/en/articles/7154647-creative-guidelines | RG docs.roku.com/published/advertisingguidelines/en/us | PAR adsmanager.paramount.com/resources/tech-specs | SAM help.dsp.samsungads.com/docs/video | CLK help.clearcast.co.uk/en/article/how-do-i-create-a-clock-number-and-slate | LIB Clearcast Library PDF | DPP DPP012 PDF (4sales) | XR helpcenter.xr.global article 5758928813332 | IAB IAB DV-CTV PDF | COM Comcast Lite PDF | CAPE cape.io/news/deliver-ads-in-the-uk-ireland | CAPE2 help-advancedtv.cape.io UK-Overview | ATSC atsc.org A/85 page

| # | Fact | Draft | Page today | Verdict | URL | Note |
|---|---|---|---|---|---|---|
| 1 | Netflix SVOD durations | pre :10/:15/:20/:30; mid adds :45/:60/:75 | same | PASS | NF | accordion |
| 2 | Netflix Live durations | :15s, :30s | same | PASS | NF | |
| 3 | Netflix resolution/aspect | 1920x1080 rec; 1280x720, 3840x2160; 16:9; progressive | same | PASS | NF | |
| 4 | Netflix frame rates | 23.976-60 list; constant | same | PASS | NF | |
| 5 | Netflix HDR | SDR only | "All content must be SDR. HDR is not supported." | PASS | NF | |
| 6 | Netflix H.264 bitrate | rec 8/12/20; acc 2/6/8 Mbps | same | PASS | NF | |
| 7 | Netflix ProRes bitrate | rec 42/80/120; acc 40/60/100 | same | PASS | NF | |
| 8 | Netflix file weight, format | 1GB or less; MP4, MOV | same; "MOV (not accepted on Amazon DSP)" | PASS | NF | |
| 9 | Netflix audio | PCM rec / AAC-LC 192kbps min; stereo; 48kHz; 16/24 bit; 500 ms | same | PASS | NF | |
| 10 | Netflix loudness | -24LKFS ±2; TP not above -2 dBFS | same | PASS | NF | |
| 11 | Netflix boxing | never exceed 37% | same | PASS | NF | |
| 12 | Netflix approval | 72 hours; restricted up to five days | same | PASS | NF | |
| 13 | Netflix pause ad | min 1728 x 1440 (rec 2592 x 2160) | same | PASS | NF | |
| 14 | Amazon file/frame | 500MB; 16:9; 1920x1080 | same | PASS | AMZ | |
| 15 | Amazon bitrate | PV 15mbps; others 8mbps; rec 50mbps | same | PASS | AMZ | |
| 16 | Amazon fps, audio | 23.976 rec, 24, 25, 29.97; 192kbps; 44.1/48kHz; 2 ch | same | PASS | AMZ | |
| 17 | Prime Video lengths by country | US/CA 15,30,45,60; UK etc 10-60; MX/AU; JP 15,30 | same | PASS | AMZ | |
| 18 | 3P STV apps lengths | 06s...90s | same | PASS | AMZ | Fire TV Channels column exists, not in draft |
| 19 | Amazon tags | Inline VAST 2.0/3.0; no VPAID/wrappers | same | PASS | AMZ | |
| 20 | Disney resolution | 1920 x 1080 pref; 1280 x 720; 16:9; no boxing | same | PASS | DIS | |
| 21 | Disney bitrate / file | CBR 10-40 Mbps; 1.9 GB / 250 MB | same | PASS | DIS | |
| 22 | Disney audio | 2 ch; 128 Kbps min CBR; 44.1/48 kHz | same | PASS | DIS | |
| 23 | Disney turnaround, leaders | 5 business days; no slates | same | PASS | DIS | |
| 24 | Roku Ads Manager | 1 GB; 6-92 seconds; 16:9; 23.98/25.00/29.97; min 6 Mbps; 96 kbps; 48 kHz | same; dated September 23, 2025 | PASS | ROKU | |
| 25 | Roku Guidelines | ":15 or :30... :60"; under 30 fps not permitted | same | PASS | RG | |
| 26 | Paramount video | :15 or :30; 1280x720 min; 6 Mbps; 10 GB max; fps list | same | PASS (URL CHANGED) | PAR | /creative-center/tech-specs now redirects to /resources/tech-specs |
| 27 | Paramount loudness | -24 LUFS +/- 2 LUFS; "Never excess -6db" | same | PASS | PAR | |
| 28 | Paramount budget | $500 - $260,000, CPM | same (FAQ) | PASS | PAR | |
| 29 | Samsung CTV | max 50 MB (rec 30); 5-90 s; 5-10 Mbps; 1280 x 720 min; 30 fps | same; "Updated on Mar 6, 2025" | PASS | SAM | |
| 30 | Clock number formats | AAA/BBBB123/456; long AAA/BBBB12/3456; SSI SABC/ABCD001/10, max 60 s | same | PASS | CLK | |
| 31 | Slate timing | clock 09:59:50:00-09:59:56:24; black 09:59:57:00-09:59:59:24; ad 10:00:00:00 | same | PASS | CLK | |
| 32 | Clearcast Library layout | 10 second clock slate; 0 or 5 second freeze; 6 frames silence | same | PASS | LIB | cover says v1.5 |
| 33 | Clearcast QC | BT.709; R103; BT.1702; -23 LUFS; -1dbTP | same | PASS | LIB | |
| 34 | Clearcast XDCAM 50 / rough cut | 50 Mbit/s, 1920 x 1080, 25 FPS interlaced; MP4 15 Mbit/s | same | PASS | LIB | "ProRes 422 HQ" block does print AVC 114 Mbit/s |
| 35 | DPP012 loudness | -23.0 LUFS ±0.2LU; rec -3dBTP, fail above -1dBTP; short-term -18.0 LUFS | same | PASS | DPP | doc date found: "V2.0 17-05-2025" |
| 36 | DPP012 safe area | 80% width, 90% height; 191-1726; 55-1026 | same | PASS | DPP | |
| 37 | DPP012 text / clock | 30 TV lines, 26 on solid background; clock 7 seconds; SOM 10:00:00:00 | same | PASS | DPP | |
| 38 | XR layout | 5-second slate, 2 s black; frame 168 / 210; fades max 10 frames | same; "Updated 7 months ago" | PASS | XR | |
| 39 | XR file | XDCAM HD 422 50 Mbps / ProRes 422 HQ; 1920 x 1080 23.98; MP4 AVC 20 Mbps, AAC 224 Kbps | same | PASS | XR | |
| 40 | XR audio | -24 LKFS; TP below -2 dB TP; rec below -6 | same | PASS | XR | |
| 41 | XR title safe / ad code | 90%, up to 93%; ABC/ESPN 13, NBC 15, DIRECTV 16, CBS 20, FOX/Discovery 25 | same | PASS | XR | |
| 42 | IAB durations | 6, 15, 30; bumper 3-10; 60 | same | PASS | IAB | "Released August 2022" |
| 43 | IAB audio levels | -24 LKFS (+/- 2.0 dB) US; -23 LUFS (+/- 1.0) EU; peak -6 db true peak | same | PASS | IAB | |
| 44 | IAB bitrates | 500-700 / 700-1500 / 1500-2500 kbps (720p) | same; page also has 2500-3500 kbps for 1080p | PASS | IAB | |
| 45 | Comcast lengths | 15 sec/450 ... 5 min/8992 frames; no slate | same | PASS | COM | |
| 46 | Comcast audio | -8dBFS; -10dBFS; 48KHz | same | PASS | COM | |
| 47 | Cape lead times | 2 working days; Adsmart 7; BVOD 5; Finecast 10 | same | PASS | CAPE | CAPE2 says "VOD & Sky Adsmart require 5 days" |
| 48 | Cape slate | 10" pre-roll = 7" + 3" black; 6 frames mute | same | PASS | CAPE2 | |
| 49 | ATSC A/85 | A/85:2026-07, approved 8 July 2026 | same | PASS | ATSC | |
| 50 | NBCU/Peacock specs | snippet | - | COULD NOT OPEN | scrollhelp.site | proxy refuses host |
| 51 | EBU R128 landing page | not opened | 403 | COULD NOT OPEN | tech.ebu.ch/publications/r128 | r128s1.pdf opens, see file 04 #18 |

Totals 01: PASS 49, FAIL 0, COULD NOT OPEN 2. Not re-read (no verdict): Disney duration/loudness snippets (not on the page text), Netflix safe-zone percentages beyond the text shown (they match: ~5-10%, ~25-30%), ARPP, ITU, Ad-ID.

## File 02 - YouTube / Google Ads
G = support.google.com/google-ads/answer/ ; P = support.google.com/adspolicy/answer/

| # | Fact | Draft | Page today | Verdict | URL | Note |
|---|---|---|---|---|---|---|
| 1 | Recommended resolution | 1920x1080 / 1080x1920 / 1080x1080 | same | PASS | G13547298 | |
| 2 | Minimums | 1280x720, 720x1280, 480x480; SD 640x480, 480x640 | same | PASS | G13547298 | |
| 3 | Aspect ratios | 16:9, 9:16, 1:1; also 4:3, 2:3, 4:5 | same | PASS | G13547298 | |
| 4 | File size | ≤256 GB | same | PASS | G13547298 | |
| 5 | Thumbnail | 1280x720 (min 1280x640); <2MB / <10MB | same | PASS | G13547298 | |
| 6 | Companion banner | 300 x 60; 150kb | same | PASS | G13547298 | |
| 7 | Vertical safe zone 1080x1920 | top 288, bottom 672, left 48, right 192 | same | PASS | G13547298 (SVG) | rendered and read |
| 8 | Horizontal safe zone 1920x1080 | 38 / 162 / 387 / 38; notches 496x183, 475x133 | same | PASS | G13547298 (SVG) | |
| 9 | Skippable | skip after 5 seconds; "No max length (<3 min recommended)" | same | PASS | G2375464 | |
| 10 | Skippable lengths | :15-:20 / 2:00-3:00 / :15-:20; reservation 12 s - 6 min; >:10 for view count | same | PASS | G6055025 | |
| 11 | In-stream headline/CTA | ≤15 / ≤10 characters | same | PASS | G6055025, G11462260 | |
| 12 | Non-skippable sub-formats | bumper up to 6; 7 to 15; 16-30 (CTV) | same | PASS | G11462260 | |
| 13 | Non-skip rule | "30 seconds (or shorter)"; 30-second assets must be horizontal | same | PASS | G11462260 | |
| 14 | Policy limit | 30 seconds auction, 60 seconds reservation | same | PASS | P2679940 | |
| 15 | Bumper | "6 seconds (>=5 seconds minimum)"; "between 5 and 6 seconds" | same | PASS | G2375464 | |
| 16 | Non-skip overview wording | "15-60 seconds (depending on the campaign subtype)"; "60 seconds or shorter" | same | PASS | G2375464 | |
| 17 | In-feed | any length; ≥ 10 s for view count; 12+ s remarketing | same | PASS | G6227733 | |
| 18 | In-feed text | 2 lines x 40; 2 lines x 35; also "100 characters max" | same (both on page) | PASS | G6227733 | |
| 19 | Shorts length | up to 3 minutes; first 60 seconds; overlay at 50 seconds | same | PASS | G16041697 | |
| 20 | Shorts text / CTA | 90 characters; CTA at 3 s (PMax, App, Demand Gen), 10 s (VVC, VRC) | same | PASS | G16041697 | |
| 21 | Shorts FAQ | 180-second mark; overlay at 170 | same | PASS | G16041383 | |
| 22 | Masthead | no max length; autoplay up to 30 seconds; 1920 x 1080 | same | PASS | G9709826, G2375464 | |
| 23 | Masthead text | ≤40 / ≤60 / ≤15 | same | PASS | G17091270 | |
| 24 | Audio ads | max 30 s; ≤15 non-skip; 128GB; 60-80 words | same | PASS | G10227746 | |
| 25 | YouTube TV | :06, :15, :30, :60; within 1 second | same | PASS | G14442864 | |
| 26 | VRC text | 90 / 90 / 255 / 10 | same | PASS | G10581234 | |
| 27 | VRC lengths | :07-:15; :16-:30; ≤:06; target frequency :07-:20; no vertical on in-feed | same | PASS | G10581234 | |
| 28 | VVC | up to 5 videos; :60-3:00, :15, vertical :10-:60; ≥:05 | same | PASS | G13982458 | |
| 29 | Demand Gen video | 1-5 videos; min 5 s; <10 s no in-stream; >15 s; 256 GB | same | PASS | G17141078 | |
| 30 | Demand Gen logo | 144x144 vs 128x128 | both present on G17141078 | PASS | G17141078, G13704860 | |
| 31 | Demand Gen images | min 600x314, 300x300, 480x600, 600x1067; 5 MB | same | PASS | G13704860 | |
| 32 | PMax text | 30 (one ≤15); 90; 90; 25; path 15 | same | PASS | G17091269 | |
| 33 | PMax images/logos/video | 5120 KB; up to 20; logos up to 5; "10 seconds or more"; up to 15 videos | same | PASS | G17091269 | |
| 34 | App campaigns | 30 / 90; 20 images; 5MB; 10-60 seconds; 20 videos | same | PASS | G17091671 | |
| 35 | Uploaded display | 150KB; GIF 30 s, slower than 5 FPS; 90 days, $9,000 | same | PASS | G1722096 | |
| 36 | DV360 loudness | -24LKFS +/- 2LKFS; 192 Kbps; 20 Mbps | same | PASS | displayvideo/answer/3129957 | |
| 37 | Video policy | name or logo; max 3 tracking pixels per event | same | PASS | P2679940 | |
| 38 | AI label notice | "Starting in July of 2026..."; Posted July 9, 2026; EU, India, New York | same | PASS | P17257106 | |
| 39 | AI label setting | six regions; "How this ad was made"; cannot be overwritten; SynthID + C2PA | same | PASS | G17140115 | |
| 40 | Election ads | checkbox; Feeds/Shorts mobile, In-stream all screens | same | PASS | P6014595 | |
| 41 | AdMob native | ratios; 256 px; 512 MB; 1 MB; 120x120dp; 25 / 90 chars; 15px | same | PASS | admob/answer/6329638 | |

Totals 02: PASS 41, FAIL 0, COULD NOT OPEN 0. Not re-read: RDA, RSA, AdMob interstitial/app-open/rewarded, ABCD, YouTube creator AI page, companion detail page.

## File 03 - Meta / TikTok / social
M = facebook.com/business/ads-guide/update/ ; H = facebook.com/business/help/ ; T = ads.tiktok.com/help/article/

| # | Fact | Draft | Page today | Verdict | URL | Note |
|---|---|---|---|---|---|---|
| 1 | FB Feed video | 4:5; 1440 x 1800; 1 second to 241 minutes; 4GB; 50-150 / 27 | same | PASS | M video/facebook-feed | |
| 2 | FB Stories video | 9:16; 1440 x 2560; 1 second to 3 minutes; 125 / 40; min 250 px | same | PASS | M video/facebook-story | |
| 3 | FB Reels | 9:16; 1440 x 2560; "No maximum limit."; 40 / 55; auto captioning No | same | PASS | M video/facebook-facebook-reels | |
| 4 | FB Reels overlay | 1:1; 1440 x 1440; 4-15 seconds; 60 | same | PASS | M ...reels-overlay | |
| 5 | FB in-stream | desktop 5-15 seconds; mobile 5 seconds to 10 minutes | same | PASS | M video/facebook-instream-video | |
| 6 | FB Marketplace | 1:1; 1 second to 241 minutes; headline 25 | same | PASS | M video/facebook-marketplace | |
| 7 | IG Feed video | 9:16; 1080 x 1920; 1 second to 60 minutes; 125; 30 hashtags | same | PASS | M video/instagram-feed | |
| 8 | IG Stories video | 9:16; 1440 x 2560; 1 second to 60 minutes; 125 | same | PASS | M video/instagram-story | |
| 9 | IG Reels | 1440 x 2560; 0 seconds to 15 minutes; 44; 250 px / 500 px | same | PASS | M video/instagram-reels | |
| 10 | IG Reels "should not contain" | licensed music, effects, GIF, product tags, pre-October 15, 2021 | same | PASS | same | |
| 11 | IG Explore home | 1080 x 1920; 1 second to 60 minutes | same | PASS | M video/instagram-explore-home | |
| 12 | Messenger Stories | 1 second to 60 seconds; min 500 px; "14% (250 pixels)" top and bottom | same | PASS | M video/messenger-story | |
| 13 | Audience Network native | 1 second to 2 minutes; captions not supported | same | PASS | M video/audience-network-native | |
| 14 | Audience Network rewarded | 3 seconds to 61 seconds | same | PASS | M ...rewarded-video | |
| 15 | FB Feed image | 4:5; 1440 x 1800; 30MB; 600 px; 750 px; 3% | same | PASS | M image/facebook-feed | |
| 16 | IG Feed image | 4:5; 500 px; 400 x 500 to 191 x 100 | same | PASS | M image/instagram-feed | |
| 17 | Carousel FB Feed | 2 to 10; 1:1; 80/20/18; 1 second to 240 minutes | same | PASS | M carousel/facebook-feed | |
| 18 | Carousel IG Feed | 4:5 images only; video only 1:1; 1 second to 2 minutes | same; plus "For Boost, video carousels are supported in 1:1 or 4:5" | PASS | M carousel/instagram-feed | |
| 19 | Carousel IG Stories | 9:16; 1080 x 1920; 1 second to 15 seconds | same | PASS | M carousel/instagram-story | |
| 20 | 9:16 safe zone | 14% top, 35% bottom, 6% each side | same | PASS | Reels, Stories pages | |
| 21 | Reels with disclaimers | bottom 40% | same | PASS | H980593475366490 | |
| 22 | Other safe-zone rules | IG Feed 9:16 same as Reels; taller screens zoom/black; guardrail | same | PASS | same | |
| 23 | Threads video | 1440 x 1800; "Maximum video length: 500 seconds"; no captions | same | PASS | H655859553779869 | |
| 24 | Threads text | 80 to 160; max 2,200; 30 hashtags; headline 40 | same | PASS | same | |
| 25 | Threads notes | carousel images only; September 2026 username change; "Ad" label | same | PASS | same | |
| 26 | Meta AI info label | scope, significant edits, About this ad | same | PASS | meta.com/help/artificial-intelligence/355108217670024 | |
| 27 | Third-party AI detection | newsroom 3 Feb 2025, updated June 1, 2026 | same | PASS | about.fb.com/news/2025/02/... | |
| 28 | Political ads | "must also disclose"; June 1, 2026; EU ban; Israel listed; Jul 2, 2026 | same | PASS | transparency.meta.com SIEP | |
| 29 | Special Ad Categories | January 21, 2025; targeting limits; seven years | same | PASS | H298000447747885 | |
| 30 | TikTok auction non-Spark | 540*960 / 960*540 / 640*640; up to 10 minutes; 500 MB; 516 kbps | same; "Last updated: June 2026" | PASS | T tiktok-auction-in-feed-ads | |
| 31 | TikTok Spark caption | max 4 lines; duration "No restrictions" | same | PASS | same | |
| 32 | TikTok name/photo | 10 / 20 characters; 98x98px; <50 KB; 66px*66px | same | PASS | same | |
| 33 | TikTok safe zone | no percentages; LTR and RTL "Arabic Version" files | same | PASS | same | |
| 34 | TikTok R&F | "5-60s, recommend 9-15s"; ≤500 MB; ≥2,500kbps | same; July 2025 | PASS | T tiktok-reservation-in-feed-ads-reach-frequency | |
| 35 | TopView | 9:16 ≥540*960px; 5-60s; pre-approval; 2 days; same-day rule | same; October 2026 | PASS | T tiktok-reservation-topview | |
| 36 | Spark Ads | no restrictions; 10 minute maximum; 10,000 | same; June 2026 | PASS | T spark-ads | |
| 37 | TikTok carousel | 2-35 images; ≤100 KB; 3 sizes; music ≥2s .mp3 10M | same; September 2026 | PASS | T specifications-for-carousel-ads | |
| 38 | TikTok AIGC rule | label or own disclaimer; significant/insignificant lists; "rejected or restricted" | same; November 2026 | PASS | T tiktok-ads-policy-misleading-and-false-content | |
| 39 | TikTok misleading claims | "Number 1 ... on TikTok"; before-and-after | same | PASS | same | |
| 40 | TikTok disclosure setting | "you must turn on..." | same; April 2026 | PASS | T about-the-content-disclosure-setting-for-creators | |
| 41 | Pinterest image | 20 MB / 32 MB; 2:3, 1000 x 1500; 100 / 800 | same | PASS | help.pinterest.com ...pinterest-product-specs | |
| 42 | Pinterest video | MP4/MOV/M4V; H.264 or H.265; 2GB; 4 s - 15 min; 6 to 15 | same | PASS | same | |
| 43 | LinkedIn video | 75 KB-500 MB; three seconds to 30 minutes; 15-30; in-stream 90 s; <30 FPS; SRT; 2 MB | same; "Last updated: 4 months ago" | PASS | linkedin.com/help/lms/answer/a424737 | |

Totals 03: PASS 43, FAIL 0, COULD NOT OPEN 0. Not re-read: FB search/right column/Business Explore, other image placements, collections, branded content page, TikTok Ad Network, Branded Mission, CML, Snapchat/X/Reddit rows (still SNIPPET ONLY).

## File 04 - DOOH / radio / podcast / cinema / in-app / influencer
| # | Fact | Draft | Page today | Verdict | URL | Note |
|---|---|---|---|---|---|---|
| 1 | OAAA digital sizes | 7:2 400 x 1400; 3:1 600 x 1800; 21:10 400 x 840; 16:9; 9:16; +/- 3% | same | PASS | OAAA Digital Aspect Ratios PDF | |
| 2 | OAAA digital billboards | change every six to eight seconds; six to eight advertisers | same; Published September 12, 2022 | PASS | oaaa.org/resources/digital-billboards/ | file-type sentence not re-read |
| 3 | OAAA print | 15'x49', 18-20, 216-240 ppi; 20'x60' 432-480; 6" bleed; poster 180-200; shelter 160-200 | same; footer 2016 | PASS | OAAA Cheat Sheet PDF | |
| 4 | Lamar tips | four to five seconds; seven words or less; 38% | same | PASS | lamar.com/en/advertising-resources/design-tips | |
| 5 | Lamar programmatic | 6-10 seconds; 90% with 1400x400 and 840x400; no QR | same | PASS | lamar.com/en/products/programmatic/media-formats | |
| 6 | Bauer Adshel static | 1080px x 1920px; 72 DPI; JPG, PNG; RGB; 1MB / 20MB | same | PASS | bauermediaoutdoor.co.uk adshel-live-specification | |
| 7 | Bauer animation | MPEG4, MOV; H264; 25fps; 8mbit/s; 25MB; 10 seconds; no full motion; no sound | same | PASS | same | |
| 8 | Bauer limits / charge | seven cities static; £100 (NET) above 10 creatives | same | PASS | same | |
| 9 | JCDecaux D48 | static only; JPEG; w612 x h306; 12s | same | PASS | jcdecaux.co.uk ...d48 | |
| 10 | JCDecaux deadlines | 3 hours / 1 day / 3 days / 5 days; dynamic 20 working days | same | PASS | JCDecaux policy PDF | |
| 11 | OUTFRONT | ten working days; processing fees | same | PASS | outfront.com/posting-standards | "8 or 15 seconds" phrase not re-read |
| 12 | NCM restaurant DOOH | NO AUDIO; MP4; 8:5 and 128:75; 3 business days | same | PASS | ncm.com ...44c944 PDF | an "AUDIO*" (stereo) variant also exists |
| 13 | UK radio spot lengths | 30 and 40 seconds; 10 second increments | same | PASS | radiocentre.org using-spot-advertising | |
| 14 | Radiocentre Clearance | scripts only; 24 hours; £400 + VAT (£480); £100 + VAT (£120) | same | PASS | radiocentre.org/clearance/, /faqs/ | |
| 15 | Bauer radio delivery | 16 bit, 44.1kHz, stereo -12dBFS Wav; 0.2 s; 1pm; RCC; PRS | same | PASS | bauermedia.co.uk/audio-specifications/ | |
| 16 | Spotify script | 65 words / 30 s; 100 words / 60 s | same | PASS | ads.spotify.com audio-ad-specs | |
| 17 | Spotify audio length | music 30s (60s select markets, skippable after 30s); podcast 30s | same | PASS | same | |
| 18 | EBU R128 s1 | -23 LUFS; -18 LUFS; -1 dBTP (SNIPPET) | "−23.0 LUFS"; "−18.0 LUFS (+5.0 LU...)"; "−1 dBTP" | PASS | tech.ebu.ch/docs/r/r128s1.pdf | PDF opened; V3 August 2020; now OFFICIAL |
| 19 | Spotify audio file | MP3, WAV or OGG; 50 MB; 44.1kHz; 192-320 kbps; -16 LUFS (+/- 1.5 LUFS); stereo | same | PASS | audio-ad-specs | |
| 20 | Spotify companion/text | 600x600; 200KB; name 25; tagline 40; CTA card 640x640, 30 / 40 | same | PASS | same | |
| 21 | Spotify Canvas | 9:16; 720 x 1280; MP4 or MOV; "200KB max"; 3-8 seconds | same | PASS | same | |
| 22 | Spotify video | 30 seconds; .MOV, MP4; 500 MB; -14 dBFS RMS; -0.2 dBFS; 198-320 kbps | same; a second block lists square 1:1 too | PASS | in-stream-video-ad-specs | |
| 23 | Apple Podcasts loudness | -16 dB LKFS +/- 1 dB; -1 dB FS; BS.1770-5 | same | PASS | podcasters.apple.com/support/893 | |
| 24 | Apple RSS audio | mono 64-128, stereo 128-256 kbps at 44.1/48 kHz | same | PASS | same | |
| 25 | Megaphone | MP3; 44.1khz; -16 LUFS; "1db True Peak"; 6-9db | same; April 22, 2024 | PASS | support.megaphone.fm 1561164 | |
| 26 | DCM picture | 3996 x 2160, 3840 x 2160, 1998 x 1080, 1920 x 1080; safety 1798 x 972, 1605 x 903; 8-16 bit; rec709; 24/25fps; 4%; no QuickTime | same; 4K/UHD safety 3596 x 1944 / 3210 x 1806 | PASS | DCM 2026 PDF | |
| 27 | DCM audio | 5.1 always needed; 48 kHz, 24 bit; fail above Leq(m) 82 dB; LR-only fails | same | PASS | same | |
| 28 | DCM supers | 16 / 18 pixels; 32 / 36 at 4K | same | PASS | same | |
| 29 | DCM clearance | CAA; about 24 hours; Friday panel; 48 h + 24 h | same | PASS | same | |
| 30 | Pearl & Dean IE | 1998 x 1080; 24fps; "48hz & 24bit"; -20dbfs; 82 Leq(M); 5 / 10 working days; €180 / £216; CCCI | same | PASS | pearlanddean.ie PDF | |
| 31 | Screenvision pre-show | ProRes 422 HQ; 1920x1080p; 24fps; 78 Leq(m); title safe 10%, image safe 5% | same | PASS | Screenvision PDF | |
| 32 | Screenvision trailer / lobby | 1998 x 1080 and 2048 x 858; 82 Leq(m); lobby 1920 x 1080 and 1080 x 1920 | same | PASS | same | |
| 33 | NCM cinema | 1920 x 1080, 23.976, ProRes 422 HQ / DNxHD; 48kHz/24-bit; action safe 1728 x 972; audio required; no Dolby mix | same | PASS | ncm.com ...bd2e65 PDF | |
| 34 | NCM loudness | -10 dBFS peaks; -24 LKFS; VO :01 | same | PASS | ncm.com ...30b6fb PDF | |
| 35 | Unity video | 60 seconds or less; 30-60 beta; H.264 MP4; 10 MB / 100 MB | same; "Last updated 4 months ago" | PASS | docs.unity.com ...video/specifications | |
| 36 | Unity playable | single index.html < 5 MB; base64; no network; Android 5 / iOS 13 | same; "Last updated 24 days ago" | PASS | docs.unity.com ...playable/specifications | |
| 37 | Unity MRAID version | MRAID 3.0 (SNIPPET) | "Playables must support ... (MRAID) 3.0" | PASS | same | now read on the official page |
| 38 | AppLovin playable | 5 MB; single HTML; base64/base122; both orientations; MRAID v2.0; mraid.open() | same | PASS (URL CHANGED) | support.axon.ai link redirects to support.applovin.com/en/growth/promoting-your-apps/welcome-to-applovin/creative-specs-and-guidelines | read via curl; Playwright shows app error |
| 39 | AppLovin video/image | MP4, MOV; 9:16; 1 GB; 60 s; images 10 MB; endcard 270x480; banner 320x50 | same | PASS | same | MREC min size not re-read |
| 40 | Meta playable | 5MB; ZIP max 100 files; index.html at root; no mraid.js; onCTAClick | same | PASS | H412951382532338 | |
| 41 | Meta playable placements | Stories, AN interstitial/rewarded, IG; App Installs only | same | PASS | developers.facebook.com ...playable-ad | |
| 42 | FTC Guides | "could be or appear to be an individual, group, or institution"; "difficult to miss..." | same; pages 48092-48112 | PASS | govinfo.gov FR-2023-07-26 | |
| 43 | ASA/CMA guide | fourth edition; 23 Oct 2026; "human, animal or virtually..."; label list; Sponsored/Spon/Sp insufficient | same | PASS | asa.org.uk guide page + PDF | |
| 44 | ASA on AI | "no blanket legal requirement..."; 29 May 2025 | same | PASS | asa.org.uk news | |
| 45 | EU hub | "must be disclosed"; 5 Key Principles; 11 October 2023 | same | PASS | commission.europa.eu/influencer-legal-hub_en | |
| 46 | Instagram label | paid partnership label; Feed, Stories, Broadcast Channels, Live, Reels | same | PASS | help.instagram.com/1109894795810258 | |
| 47 | TikTok disclosure / Spark | must turn on; authorization; engagement to original post | same | PASS | T pages above | |
| 48 | YouTube paid promotion | select paid promotion; label at start | same | PASS | support.google.com/youtube/answer/154235 | |

Totals 04: PASS 48, FAIL 0, COULD NOT OPEN 0. Not re-read: OpenRTB, RAB, Lamar spec sheet, JCDecaux airport snippet, Spotify host-read, Acast, IAB podcast, ironSource, EU AI Act.

## FAILS
None. No draft value contradicted by the page.

## Changes / additions found
1. Paramount URL: /creative-center/tech-specs redirects to https://adsmanager.paramount.com/resources/tech-specs.
2. AppLovin URL: support.axon.ai link redirects to https://support.applovin.com/en/growth/promoting-your-apps/welcome-to-applovin/creative-specs-and-guidelines.
3. DPP012 date (draft: not captured): "V2.0 17-05-2025".
4. EBU R128 s1 and Unity MRAID 3.0 can be upgraded from SNIPPET to OFFICIAL.
5. New vendor conflict: Cape news page "Sky Adsmart needs 7 working days" vs Cape UK Overview "Deliveries to VOD & Sky Adsmart require 5 days".
6. Unity playable page relative date now "24 days ago" (draft 23).

## Conflicts resolved (both pages read)
- UK slate (01): same layout. Clearcast page: 7 seconds of clock + 3 seconds black = 10 s before 10:00:00:00; DPP's "7 seconds" is the clock part only.
- True peak (01): by destination. UK: aim -3 dBTP, hard fail above -1 dBTP (DPP, Clearcast, EBU s1). US broadcast via XR: below -2, recommended below -6. Netflix -2 dBFS. Paramount and IAB -6.
- Loudness tolerance: DPP ±0.2 LU (UK TV); IAB EU ±1.0; US platforms -24 ±2.
- Roku: Ads Manager (self-serve upload) accepts 6-92 seconds; the Advertising Guidelines (":15 or :30") are the general policy document. Both current.
- Comcast "-2 dBTP": printed in the PDF's third audio column, not an extraction artefact.
- Clearcast "ProRes 422 HQ" block: PDF really prints "Format: AVC ... 114 Mbit/s" (source error stands).
- IAB date: PDF "Released August 2022"; landing page "Released September 2022", last updated January 15, 2024.
- Non-skippable length (02): policy page governs - 30 seconds auction, 60 seconds reservation; format page 7-15 standard, 16-30 CTV only.
- Bumper: up to 6 seconds; overview says 5-6, VRC table "Any length ≤:06".
- Shorts over 60 s: both texts live. Specs page: first 60 seconds, overlay at 50. FAQ item 6: plays to 180, overlay at 170. Unresolved by Google; under 60 s avoids it.
- AI-label regions: current help pages list six (EU, India, New York, California, South Korea, Vietnam); the three-region text is the dated 9 July 2026 notice. Use six.
- Demand Gen logo: both 128x128 and 144x144 appear on G17141078; 144x144 is the safe minimum.
- Meta bottom safe zone: 35% standard; 40% only when the Reels ad carries disclaimers. Messenger Stories: 14% (250 pixels) top and bottom.
- TikTok bitrate/duration: auction non-Spark ≥516 kbps, up to 10 minutes; reservation and TopView ≥2,500kbps, 5-60s.
- TikTok Spark: no spec limits, but organic post must be 10 minutes or less; caption shows max 4 lines (auction page).
- Spotify loudness (04): audio ads -16 LUFS (+/- 1.5 LUFS); video ads RMS -14 dBFS, peak -0.2 dBFS. Different formats.
- Cinema loudness: DCM and Pearl & Dean 82 Leq(m); Screenvision 78 pre-show, 82 trailer position; NCM -24 LKFS / -10 dBFS.
- MRAID: Unity 3.0, AppLovin v2.0, Meta no mraid.js - three separate builds confirmed.
Not settled: Netflix vs Mountain blog, Disney vs Vibe, Snapchat (community/snippet side not opened); Spotify 1MB (old page not found).

## Could not open
- https://nbcuniversal-creative-guidelines.scrollhelp.site/nbcuadspecs/nbcuniversal-standard-digital-video-guidelines (proxy refuses host)
- https://tech.ebu.ch/publications/r128 (403; the s1 PDF does open)
- Disney+ duration and loudness: not present in the page text; platform tabs not expanded - still unverified.
