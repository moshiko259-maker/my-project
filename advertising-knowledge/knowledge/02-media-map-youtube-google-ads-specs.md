# 02 - YouTube ads and Google Ads creative specs

Read: 20-21 Nov 2026. STATUS: DRAFT - NOT YET VERIFIED. Do not copy any number into a skill until `15-verification-log.md` shows it PASS.
Tags per fact: OFFICIAL / VENDOR / COMMUNITY / INFERENCE / UNKNOWN. "SNIPPET ONLY" = seen in a search result, page not opened.
Origin: sub-agent report `research-raw/R1b-youtube-google-ads-specs.md`, reformatted only (no fact added or removed by the main agent).

R1b REPORT - YouTube ads / Google Ads official creative specs. All pages read 20 Nov 2026 by direct fetch (curl, full page text), tag OFFICIAL unless stated. Google Help pages (support.google.com) show NO visible "last updated" date; dates given only where the page shows one. G = https://support.google.com
Process note: I cached fetched pages in a temp folder inside the session scratchpad while reading, then deleted it; nothing remains on disk.

## 1. Findings

### 1a. Universal YouTube video ad specs — G/google-ads/answer/13547298 ("About video ad specs")
| Fact | Value |
|---|---|
| Resolution recommended | 1080p: 1920x1080 (horizontal), 1080x1920 (vertical), 1080x1080 (square) |
| Also accepted | 720p min 1280x720 / 720x1280 / 480x480; SD min 640x480 / 480x640 / 480x480 ("we don't recommend using SD") |
| Aspect ratio | Recommended 16:9, 9:16, 1:1; also accepts 4:3 (SD), 2:3 vertical, 4:5 vertical |
| File format | Recommended .MPG (MPEG-2 or MPEG-4); also .WMV, .AVI, .MOV, .FLV, .MPEG-1, .MP4, .MPEGPS, 3GPP, WebM, DNxHR, ProRes, CineForm, HEVC (h265). No audio files (MP3, WAV, PCM) |
| File size | ≤256 GB |
| Thumbnail | 1280x720 (min 1280x640), 16:9, .JPG/.GIF/.PNG, <2MB for videos, <10MB for podcasts |
| Companion banner (desktop only) | 300 x 60, JPEG/GIF/PNG, 150kb maximum |
| Must be hosted on YouTube | "Your video must be uploaded to YouTube and set as public or unlisted to use in an ad" (G/google-ads/answer/6055025). Unlisted ads won't display channel logo/name. "video ad content must be hosted on YouTube" (G/google-ads/answer/2375464) |
| Vertical safe zone (1080x1920; read from the page's SVG diagram) | margins: top 288 px, bottom 672 px, left 48 px, right 192 px |
| Horizontal safe zone (1920x1080; SVG diagram) | left 38, right 162, bottom 387, top 38 in the centre; top-left notch 496 wide x 183 high, top-right notch 475 wide x 133 high |
| Safe-zone PNG templates | services.google.com/fh/files/misc/youtubesafezoneoverlay_vertical_final.png ; .../fh/files/blogs/ytsafezoneoverlay-horizontal.png ; .../fh/files/misc/youtubesafezoneoverlay-square.png (square margins not read) |

### 1b. Formats — overview G/google-ads/answer/2375464 ("About video ad formats")
Formats listed: skippable in-stream, non-skippable in-stream, in-feed, bumper, Masthead, YouTube Shorts ads. Page notes: since October 2025 "Views" is called "TrueView views"; objective renamed "YouTube reach, views, and engagements".
| Format | Length / rules | Source |
|---|---|---|
| Skippable in-stream | Skip after 5 seconds. "No max length (<3 min recommended)". Accepted "Any length. No minimum or maximum." Best practice: Awareness :15-:20, Consideration 2:00-3:00, Action :15-:20. Views count to public view count only if video >:10. Reservation: min 12 seconds, max 6 minutes. Headline "≤15 characters", CTA "≤10 characters". CPV view = 30 s or full video if shorter, or interaction | 2375464; G/google-ads/answer/6055025 |
| Non-skippable in-stream | Three sub-formats: Bumper up to 6 s; Standard 7 to 15 s; 30-second (CTV) 16-30 s, shown on Connected TV. "your ad should be 30 seconds (or shorter)". Recommended :15 and :30 CTV. "30-second video assets must be horizontal. Square or vertical assets will not be able to run." ≤:06 runs as Bumper. Headline ≤15 chars, CTA ≤10. tCPM only | G/google-ads/answer/11462260 |
| Non-skippable policy limit | Not allowed: "longer than 30 seconds in the auction and 60 seconds in reservation campaigns" | G/adspolicy/answer/2679940 |
| Bumper | "6 seconds (>=5 seconds minimum)"; "lasting between 5 and 6 seconds"; non-skippable. Campaigns: VRC, Reservations, App installs | 2375464 |
| In-feed | Any length; best practice Awareness 15-20 s, Consideration 2-3 min; view count needs ≥10 s; remarketing lists/Analytics need 12+ s. Recommended ratios 16:9, 1:1 (9:16 only "accepted"). Headline up to 2 lines x 40 chars (>25 may be shortened); description 2 lines x 35 chars; description not shown on desktop watch page or TV | G/google-ads/answer/6227733 |
| Shorts ads | Vertical 9:16 recommended; horizontal serves with blurred top and bottom. "up to 3 minutes long, though only the first 60 seconds will play on the Shorts feed, with an overlay appearing at 50 seconds"; recommended <60 s. Description limited to 90 chars; truncated beyond 1 line mobile / 2 lines desktop+TV. CTA button appears at 3 s (PMax, App, Demand Gen) and 10 s (VVC, VRC). Recommended 40-char headline + 90-char description for the CTA overlay card. Action ads: 10-30 s vertical; 6-60 s for VRC; 10-60 s other types. Sound "increase conversions by over 20%"; "consider using text overlays" | G/google-ads/answer/16041697 |
| Masthead | Reservation only (CPM or CPH). 16:9, 1920x1080 or higher, public or unlisted. "No max length (Recommend greater than 10 seconds)". Desktop autoplay up to 30 seconds. Recommended text: headline ≤40, description ≤60, CTA ≤15 chars. No CTA on TV. 2 companion videos optional (desktop). Captions may be auto-added when muted | G/google-ads/answer/9709826; G/google-ads/answer/17091270 |
| YouTube audio ads | Max 30 seconds; ≤15 s serves non-skippable, 16-30 s skippable. Max file size 128GB. 16:9. Resolutions 240p-2160p. Still image or simple animation; uploaded as a YouTube video. "For a 30 second ad, aim for 60-80 words" | G/google-ads/answer/10227746 |
| YouTube TV (US only) | Non-skip lengths: :06 or shorter, :15 or shorter, :30, :60. 30 s and 60 s ads must be within 1 second of length (30 s = :29 to :31) or they won't serve | G/google-ads/answer/14442864; G/google-ads/answer/10651730 |

### 1c. Campaign types
| Campaign | Specs | Source |
|---|---|---|
| Video reach (VRC) | Options: Efficient reach, Non-skippable reach, Target frequency. Headline max 90, description max 90, display URL max 255, CTA max 10 chars + optional 30-char headline. Efficient reach best practice: horizontal :15, horizontal :06, vertical :06-:60. Non-skip reach: 15-second ads :07-:15, 30-second (CTV) :16-:30, bumper ≤:06. Target frequency non-skip: horizontal :07-:20. "Vertical videos won't serve on in-feed inventory". Video enhancements (auto 9:16 versions) on by default | G/google-ads/answer/10581234 |
| Video view (VVC) | Skippable in-stream + in-feed + Shorts; up to 5 videos. Recommended: one horizontal :60-3:00, one horizontal :15, one vertical :10-:60. Accepted: in-stream ≥:05 horizontal, in-feed ≥:05 | G/google-ads/answer/13982458 |
| "Video action campaigns" (still on specs page) | ≥10 seconds; headline 30, long headline 90, description 90, CTA 10 chars | G/google-ads/answer/17091270 |
| Demand Gen video | 1-5 videos per ad. Ratios 16:9 (1920x1080), 1:1 (1080x1080), 4:5 (1080x1350), 9:16 (1080x1920, recommended for Shorts). Min 5 seconds; under 10 s can't serve on YouTube In-stream. Recommended 10-60 s; ">15 seconds" to maximise reach. Max 256 GB. Headline 40 (at least one ≤30 to serve on Display), long headline 90, description 90, business name 25, final URL 2,048. CTA automated. Square logo min 144x144, rec 1200x1200, max 150 KB. Sound defaults: Shorts sound on; Discover, Home feed, Gmail, GDN muted | G/google-ads/answer/17141078; G/google-ads/answer/13704860; G/google-ads/answer/17091672 |
| Demand Gen images | 1.91:1 1200x628 (min 600x314); 1:1 1200x1200 (min 300x300); 4:5 960x1200 (min 480x600); 9:16 1080x1920 (min 600x1067). .jpg/.png, max 5 MB. 1-20 images | 13704860; 17091672 |
| Performance Max | Headlines 30 chars (3-15; one ≤15 chars); long headlines 90 (1-5); descriptions 90 (2-5); business name 25; display path 15 each. Images: 1.91:1 1200x628 (min 600x314); 1:1 1200x1200 (min 300x300); 4:5 960x1200 (min 480x600); up to 20 each; 5120 KB max; .jpg/.png max 5MB. Logos: 1:1 1200x1200 (min 128x128), 4:1 1200x300 (min 512x128), up to 5. Videos: horizontal, square, vertical; "10 seconds or more"; up to 15; auto-generated if none uploaded. No custom companion banner | G/google-ads/answer/17091269; G/google-ads/answer/6293542 |
| App campaigns | Headlines 30 (1-5), descriptions 90 (1-5). Images max 20, .jpg/.png max 5MB: 1.91:1 1200x628 (min 600x314), 4:5 1200x1500 (min 320x400), 1:1 1200x1200 (min 200x200). Videos max 20; 16:9, 9:16, 1:1; 10-60 seconds; "must be uploaded to YouTube" | G/google-ads/answer/17091671 |
| Responsive display ads | Headlines 30 (1-5), long headline 90 (1), descriptions 90 (1-5), business name 25. Images: 1.91:1 1200x628 (min 600x314), 1-15; square 600x600 (min 300x300), 1-15. Logos 1:1 1200x1200 (min 128x128), 4:1 1200x300 (min 512x128). Videos 1-5, 16:9 / 1:1 / 2:3, any length, preferred 30 seconds | G/google-ads/answer/17090561 |
| Uploaded display ads | GIF/JPG/PNG, max 150KB. Sizes: 200x200, 240x400, 250x250, 250x360, 300x250, 336x280, 580x400, 120x600, 160x600, 300x600, 300x1050, 468x60, 728x90, 930x180, 970x90, 970x250, 980x120, 300x50, 320x50, 320x100. Animated GIF ≤30 seconds, slower than 5 FPS. HTML5 access needs account open >90 days and >$9,000 USD lifetime spend | G/google-ads/answer/1722096 |
| Search RSA | Up to 15 headlines x 30 chars (min 3 to create), up to 4 descriptions x 90, paths 15 each, final URL 2,048. Double-width characters count as 2. Business name 25; logo 1:1 1200x1200 (min 128x128) | G/google-ads/answer/7684791; G/google-ads/answer/17092074 |
| Companion banner detail | 300px x 60px, JPEG/GIF/PNG, max 150 KB, GIF under 5 frames per second; supported on skippable, non-skippable and bumper; desktop only; a click counts as a view | G/google-ads/answer/6293542 |

### 1d. Captions and loudness
| Fact | Tag | Source |
|---|---|---|
| No Google Ads Help page found that requires or specifies captions for video ads | UNKNOWN (2 site searches + all pages above) | — |
| In-feed autoplay in YouTube app plays "with the sound off and captions enabled" | OFFICIAL | G/google-ads/answer/6227733 |
| Shorts: "Use sound (music, voiceover, or both)"; "consider using text overlays". ABCD: "Support the story with audio and supers" | OFFICIAL | 16041697; G/google-ads/answer/14783551 |
| No loudness figure on any Google Ads / YouTube ads spec page | UNKNOWN | — |
| DV360 video creative guideline: "Loudness aligned with IAB US spec of -24LKFS +/- 2LKFS (Campaign Manager 360 will normalize to target loudness of -24 LKFS)"; audio PCM (preferred) or AAC, at least 192 Kbps; video H.264, 23.98 or 29.97, at least 20 Mbps | OFFICIAL (DV360, not Google Ads) | G/displayvideo/answer/3129957 |

### 1e. Policies
| Fact | Source |
|---|---|
| Video ads must include "a name or logo that clearly represents the advertiser, product, or service" (Unclear content); must be publicly available; max 3 tracking pixels per event | G/adspolicy/answer/2679940 |
| Video quality: not allowed "illegible text, poor sound quality, or blurry, unclear, or unrecognizable visuals" | G/adspolicy/answer/6021546 |
| Misrepresentation covers clickbait, misleading ad design, manipulated media, unreliable claims. Manipulated media: "Manipulating media to deceive, defraud, or mislead others is not allowed"; warning at least 7 days before suspension | G/adspolicy/answer/6020955; G/adspolicy/answer/15939579 |
| YouTube + Discover extra rules: no clickbait / exaggerated claims, no shock or negative-event imagery | G/adspolicy/answer/10249050 |
| AI labels: "Starting in July of 2026, Google permits adding text or visual labels directly within image and video ad creatives" made or modified with AI; not a text-overlay/watermark violation. Page date: "Posted on July 9, 2026" | G/adspolicy/answer/17257106 |
| AI label setting: advertiser marks an asset "created or edited with AI"; disclosure shows in "How this ad was made" in My Ad Center (global). Visible on-ad overlay for campaigns targeting European Union, India, New York, California, South Korea, Vietnam. Google-applied labels cannot be overwritten. Google AI tools embed SynthID + C2PA. Setting "doesn't guarantee your compliance" | G/google-ads/answer/17140115; G/My-Ad-Center-Help/answer/17196133; blog.google/products/ads-commerce/google-ads-ai-transparency-labels/ (published 2026-07-09) |
| Election ads: must tick "Altered or synthetic content" checkbox for synthetic content depicting real or realistic people/events. Google generates the in-ad disclosure for Feeds on mobile, Shorts on mobile, In-stream (computer, mobile, mobile web, TV); other formats need the advertiser's own prominent disclosure. Inconsequential edits (resize, crop, colour) out of scope | G/adspolicy/answer/6014595 |
| YouTube "AI use" disclosure (creator uploads): required for realistic content that makes a real person appear to say/do something, alters real event/place footage, generates a realistic scene, or AI music as main focus. Page does not mention ads | G/youtube/answer/14328491 |
| Link to ads: "If you upload a video to YouTube from within Google Ads, you will be asked whether AI was used... to comply with YouTube's AI disclosure policies for organic videos" | G/google-ads/answer/17140115 |
| Whether the YouTube viewer-facing label shows on a video when served as a paid ad | UNKNOWN - not stated on either page. INFERENCE: ad videos are YouTube uploads, so the upload-time disclosure applies to the video itself |

### 1f. AdMob in-app formats
| Fact | Source |
|---|---|
| Formats: Banner, Interstitial, Rewarded interstitial (Beta), Rewarded, Native advanced, App open | G/admob/answer/6128738 |
| Fixed banner sizes (dp): 320x50 Banner, 320x100 Large banner, 300x250 IAB medium rectangle, 468x60 full-size banner (tablets), 728x90 leaderboard (tablets). Anchored adaptive banner is the default guide. Page: "Last updated 2026-11-18 UTC" | developers.google.com/admob/android/banner/fixed-size ; developers.google.com/admob/android/banner |
| Native: video aspect ratio 4:3, 16:9, 1:1, 3:4 or 9:16; at least 256 px on longer side; max video file 512 MB; max image 1 MB; MediaView at least 120x120dp; title 25 chars, body 90 chars without truncation; "Ad" badge min 15px | G/admob/answer/6329638 |
| Interstitial: up to 5-second delay before close option; high-engagement video up to 12-second | G/admob/answer/6066980 |
| App open: up to 2-second delay before close (5-second with high-engagement); ad times out after four hours | G/admob/answer/9341964; developers.google.com/admob/android/app-open |
| Rewarded: no direct monetary rewards; discount rewards for physical items max 25% of item value; ad pods = 2 back-to-back videos. Rewarded interstitial needs intro screen with skip option | G/admob/answer/7313578; G/admob/answer/6128738; developers.google.com/admob/android/rewarded-interstitial |
| Rewarded / interstitial video length for the advertiser's creative | UNKNOWN on AdMob pages; advertiser side uses App campaign assets (10-60 seconds, section 1c) |

### 1g. ABCD
| Fact | Source |
|---|---|
| Attention, Branding, Connection, Direction. Core: jump in; audio and supers; bright high-contrast visuals; brand early and often; audio brand mentions; feature people; focus the message; include a CTA and reinforce it with voice-over. Shorts order: Connection, Attention, Branding, Direction. Claim: "as much as a 30% lift in short-term sales likelihood and a 17% lift in long-term brand contribution" (Google/Kantar, Apr 2021) | G/google-ads/answer/14783551 |
| Think with Google article, dated April 2022: "On average, the ABCDs deliver a 30% lift..." | thinkwithgoogle.com/future-of-marketing/creativity/youtube-video-ad-creative/ |
| Vertical video stats (Google internal data, Global 2024): Demand Gen +35% conversions on Shorts; VVC +40% VTR on Shorts; VRC +45% viewability | G/google-ads/answer/9128498 |

## 2. Conflicts (all between official pages)
1. Non-skippable max length: "15-60 seconds (depending on the campaign subtype)" / "60 seconds or shorter" (2375464) vs "30 seconds (or shorter)" (11462260) vs policy "30 seconds in the auction and 60 seconds in reservation" (adspolicy 2679940). The policy page reconciles the other two.
2. Bumper minimum: "between 5 and 6 seconds" (2375464) vs "Any length ≤:06" (10581234).
3. Shorts ads over 60 s: "only the first 60 seconds will play... overlay appearing at 50 seconds" (16041697) vs FAQ "played until the 180-second mark then loop... overlay at the 170-second mark" (G/google-ads/answer/16041383).
4. In-feed headline: "100 characters max" (asset table) vs "2 lines, 40 characters per line" (spec table), both on 6227733.
5. In-stream headline: "≤15 characters" (6055025, 11462260) vs VRC "Max 90 characters" (10581234) vs Demand Gen 40.
6. AI-label regions: EU, India, New York (adspolicy 17257106, July 2026) vs six regions incl. California, South Korea, Vietnam (17140115, 13547298).
7. Demand Gen logo minimum: 144x144 (13704860, 17091672) vs 128x128 in the first table of 17141078.
8. Search "Ad assets" headlines "25 characters, 1-20 headlines" vs RSA 30 characters, 1-15 (same page 17092074).
9. Audio ads max file "128GB" (10227746) vs ≤256 GB general.
10. RDA square image recommended 600x600 (17090561) vs 1200x1200 on PMax/Demand Gen.
11. Aspect 4:5 for YouTube video: accepted on 13547298 and Demand Gen; absent from skippable / non-skippable / in-feed / VRC tables.

## 3. Could not open / UNKNOWN
- No dedicated "About bumper ads" help page found (guessed IDs 404); bumper facts come from the formats, non-skippable and VRC pages.
- Captions requirement and loudness for Google Ads: UNKNOWN (see 1d).
- Square safe-zone pixel values: not read. TV/tablet/desktop safe-zone diagrams on 13547298 not read.
- Masthead exact text limits: page defers to the Masthead Preview Tool (not opened); ≤40/≤60/≤15 are "recommended" from 17091270.
- ABCDs Playbook download, Google TV Masthead (G/google-ads/answer/14078207), HTML5/playable specs (G/google-ads/answer/9981650): not read in detail.
- iOS AdMob docs not opened (Android only).
- PMax maximum video length: not stated on 17091269.

## 4. Top 10 URLs to re-verify
1. https://support.google.com/google-ads/answer/13547298
2. https://support.google.com/google-ads/answer/2375464
3. https://support.google.com/google-ads/answer/11462260
4. https://support.google.com/adspolicy/answer/2679940
5. https://support.google.com/google-ads/answer/17091270
6. https://support.google.com/google-ads/answer/16041697 (and FAQ /16041383)
7. https://support.google.com/google-ads/answer/17091269
8. https://support.google.com/google-ads/answer/17141078
9. https://support.google.com/google-ads/answer/17140115 (and adspolicy /17257106, /6014595)
10. https://support.google.com/google-ads/answer/10581234
