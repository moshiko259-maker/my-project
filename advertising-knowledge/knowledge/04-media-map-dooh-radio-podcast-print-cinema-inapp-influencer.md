# 04 - Outdoor/DOOH, radio, podcast, print, cinema, in-app, influencer

Read: 20-21 Nov 2026. STATUS: DRAFT - NOT YET VERIFIED. Do not copy any number into a skill until `15-verification-log.md` shows it PASS.
Tags per fact: OFFICIAL / VENDOR / COMMUNITY / INFERENCE / UNKNOWN. "SNIPPET ONLY" = seen in a search result, page not opened.
Origin: sub-agent report `research-raw/R1d-dooh-radio-podcast-print-cinema-inapp-influencer.md`, reformatted only (no fact added or removed by the main agent).

R1d REPORT - specs for outdoor/DOOH, radio, podcast/streaming audio, print, cinema, in-app, influencer. Read 20-21 Nov 2026. Reading stopped early on the coordinator's instruction, so print, IAB DOOH/MRAID, SAWA/TASA and Israeli owners are mostly under UNKNOWN.
Access note: WebFetch could not resolve any host in this session; pages were read with curl (browser UA) or Playwright. "SNIPPET" = seen only in a WebSearch result summary, page not opened by me.

## 1. FINDINGS

### 1A. Outdoor / DOOH
| Fact | Value | Tag | Source | Page date |
|---|---|---|---|---|
| OAAA digital art sizes | Bulletin 14'x48' and 10'6"x36' = 7:2, 400 x 1400 px; 20'x60' = 3:1, 600 x 1800; Poster and Junior Poster = 21:10, 400 x 840; Digital taxi top, in-store, street furniture horizontal = 16:9, 1920 x 1080; street furniture vertical = 9:16, 1080 x 1920; height/width tolerance +/- 3% | OFFICIAL | https://oaaa.org/wp-content/uploads/2022/09/DOC-Digital-Aspect-Ratios-.pdf | upload path 2022/09 |
| OAAA digital billboard basics | "Ad messages change every six to eight seconds"; typically six to eight advertisers per location; preferred files ".psd, jpg, tiff, or bmp saved at 72ppi in RGB color mode"; design at actual pixel size | OFFICIAL | https://oaaa.org/resources/digital-billboards/ | Published September 12, 2022 |
| OAAA print production (static) | Bulletin wrap 14'x48': finished 15'x49', target 18-20, scale 1"=1", mechanical 15"x49", 216-240 ppi; 20'x60': mechanical 10.5"x30.5" at 1/2"=1", 432-480 ppi; "Bulletin wraps generally require 6" of bleed around all four sides"; poster 10'5"x22'8": 1/10 scale, 180-200; transit shelter 68.5"x47.5": 1/2 scale, 160-200 | OFFICIAL | https://oaaa.org/wp-content/uploads/2022/09/OOH-Print-Production-Specifications-Cheat-Sheet.pdf | footer "2016" |
| OAAA design best practice (blog post by an industry author) | bold sans serif fonts; white text on vibrant backgrounds; one idea; "USE SEVEN WORDS OR LESS" | OFFICIAL (OAAA blog, not a formal standard) | https://oaaa.org/blog-posts/billboardsthatsparkjoy/ | not shown |
| Lamar design tips | "exposure time is typically four to five seconds ... say it in seven words or less"; "high-color contrast can improve outdoor advertising recall by 38%" | VENDOR | https://lamar.com/en/advertising-resources/design-tips | not shown |
| Lamar programmatic DOOH | "changing every 6-10 seconds depending on location"; "over 90% of Lamar screens with two specs: 1400x400 and 840x400"; "QR codes can NOT be used on Lamar DOOH" | VENDOR | https://lamar.com/en/products/programmatic/media-formats | not shown |
| Lamar file format | 1400 by 400 px at 72 ppi; RGB; JPG, BMP or GIF; no animated GIFs | VENDOR, SNIPPET | https://resources.lamar.com/SMCoreServices/public/materials/pdf/reports/specsheet/30/80011 | - |
| Bauer Media Outdoor UK (formerly Clear Channel UK) - Adshel Live static | 1080px x 1920px portrait; 72 DPI; JPG, PNG; RGB ("CMYK will not display correctly"); 1MB or less / 20MB or less for programmatic | VENDOR | https://www.bauermediaoutdoor.co.uk/resources/specifications/adshel-live-specification | not shown |
| Same - subtle animation | MPEG4, MOV; H264; 25fps; 8mbit/s; 25MB or less / 20MB programmatic; standard slot 10 seconds; static backup also required; "Full-motion video content is not permitted"; "Screens do not emit sound" | VENDOR | same | - |
| Same - road-safety and local limits | must not distract motorists or pedestrians "through contrasting content or use of traffic signs/lights"; subtle animation not permitted in Aberdeen, Bristol, Leeds, Liverpool, Norwich, Sheffield, Westminster (static required there) | VENDOR | same | - |
| Same - extra creative charge | more than 10 creatives: £100 (NET) per additional creative | VENDOR | same | - |
| JCDecaux UK roadside D48 (National Drive) | "Static content ONLY"; JPEG; w612 x h306 pixels; landscape; standard length 12s | VENDOR | https://www.jcdecaux.co.uk/technical-specifications/national-drive-48-sheet-poster-d48 | not shown |
| JCDecaux UK copy deadlines | 1 piece of copy: due 3 hours before playout; 2 to 10: 1 day; 11 to 30: 3 days; 31 to 80: 5 days (working time); dynamic campaigns: allow 20 working days | VENDOR | https://www.jcdecaux.co.uk/jcdecaux/download-file?url=public%3A//blocks/downloadable_file/2025-10/Digital%20Copy%20Management%20Policy%20Updated_2.pdf | path 2025-10 |
| JCDecaux UK airport/mall motion | 1080 x 1920 portrait, 10s, 25fps, JPEG/MP4 | VENDOR, SNIPPET | https://www.jcdecaux.co.uk/technical-specifications | - |
| OUTFRONT (US) | static and digital copy due "at least ten working days before the estimated start date"; a digital spot = "the purchased time increment (e.g., 8 or 15 seconds) within a rotating content loop"; wrong aspect ratio, resolution, format or encoding may bring delays and processing fees | VENDOR | https://outfront.com/posting-standards | not shown |
| NCM restaurant DOOH (US) | full-screen video ad: "NO AUDIO"; MP4; aspect ratios 8:5 and 128:75; submission lead time 3 business days | VENDOR | https://www.ncm.com/_files/ugd/20be08_44c944fbf50a4f479c5832ee9383723f.pdf | "Digital: Local 2023" |
| OpenRTB 2.6 | spec contains "3.2.31 - Object: Qty" and "3.2.32 - Object: DOOH" (table of contents read; field text not extracted) | OFFICIAL | https://raw.githubusercontent.com/InteractiveAdvertisingBureau/openrtb2.x/main/2.6.md | - |
| Qty multiplier meaning | billable-events multiplier, e.g. one DOOH play = 14.2 impressions | COMMUNITY, SNIPPET | https://developers-brand.verve.com/docs/brand-openrtb-specifications | - |

### 1B. Radio
| Fact | Value | Tag | Source | Page date |
|---|---|---|---|---|
| UK spot lengths | "most common spot lengths are 30 and 40 seconds"; any length in "10 second increments up to 60 seconds or even longer" | OFFICIAL (trade body) | https://www.radiocentre.org/how-to-do-it/planning-your-campaign/using-spot-advertising/ | not shown |
| Radiocentre Clearance | pre-vets scripts only ("you do not need to supply audio"); aims to clear within 24 hours in office hours; 2-hour Fast Track: £400 + VAT at 20% (£480) non-members, £100 + VAT (£120) full members; all special-category broadcast radio ads must be pre-vetted | OFFICIAL | https://www.radiocentre.org/clearance/ and https://www.radiocentre.org/faqs/ | not shown |
| Special categories (start of list) | consumer credit / investment / complex financial; gambling; alcohol; medical, health and beauty; food and supplements; slimming; 18+ films and games; dating; personal advice services; environmental claims; political / public controversy; religious; charitable (list continues on page) | OFFICIAL | https://www.radiocentre.org/clearance/ | - |
| Bauer Media UK delivery | "16 bit, 44.1kHz, stereo -12dBFS Wav"; duration tolerance 0.2 of a second (30s ad = 29.8 to 30.2); audio + instructions by 1pm the day before start (1pm Friday for Sat/Sun/Mon starts); RCC number required for all ads; PRS details if music | VENDOR | https://www.bauermedia.co.uk/audio-specifications/ | not shown |
| RAB (US) | no word cap found; recall data: 30 sec average recall 15.2, 60 sec 19; typical 4-5 brand mentions | OFFICIAL (trade body) | https://www.rab.com/whyradio/faq/faqprint.cfm?id=35208 | not shown |
| Script word count | Spotify: "no more than 65 words for a 30-second ad"; "100 words for a 60-second ad" | OFFICIAL (platform) | https://ads.spotify.com/en-US/ad-specs/audio-ad-specs/ | © 2026 |
| EBU R128 s1 (short-form / ads) | programme loudness -23 LUFS; max short-term -18 LUFS; max true peak -1 dBTP | SNIPPET | https://tech.ebu.ch/docs/r/r128s1.pdf | - |

### 1C. Podcasts / streaming audio
| Fact | Value | Tag | Source | Page date |
|---|---|---|---|---|
| Spotify audio ad length | music ads max 30s (long-form up to 60s in select markets, Direct only, skippable after 30s); podcast ads (streaming ad insertion) max 30s | OFFICIAL | https://ads.spotify.com/en-US/ad-specs/audio-ad-specs/ | © 2026 |
| Spotify audio file | MP3, WAV or OGG; 50 MB maximum; 44.1kHz; 192 kbps minimum, 320 kbps maximum; "-16 LUFS (+/- 1.5 LUFS)"; stereo | OFFICIAL | same | - |
| Spotify companion / text | companion 1x1, minimum 600x600, 200KB max, JPEG/PNG; advertiser name max 25 characters; tagline 40 characters; podcast CTA card image 640x640 JPG 200 KB, advertiser name 30, description 40 characters | OFFICIAL | same | - |
| Spotify Canvas (optional) | 9:16, 720 x 1280, MP4 or MOV, "200KB max" (as printed), 3-8 seconds | OFFICIAL | same | - |
| Spotify in-stream video | up to 30 seconds; 9:16 or 16:9; .MOV, MP4; max 500 MB; 720x1280 / 1280x720 or similar; audio "RMS normalized to -14 dBFS", peak -0.2 dBFS; bit rate "198 kbps ... maximum of 320 kbps"; no black bars; must include sound | OFFICIAL | https://ads.spotify.com/en-US/ad-specs/in-stream-video-ad-specs/ | © 2026 |
| Spotify host-read | "custom podcast sponsorships (such as host-read ads), contact your Spotify representative"; Direct IO only | OFFICIAL | https://ads.spotify.com/en-GB/ad-specs/podcast-ad-specs/ | - |
| Apple Podcasts loudness | "around -16 dB LKFS, with a +/- 1 dB tolerance"; true peak not above -1 dB FS; measured per ITU-R BS.1770-5; apply before encoding | OFFICIAL | https://podcasters.apple.com/support/893-audio-requirements | not shown |
| Apple RSS audio | MP3 or AAC; 44.1/48 kHz mono 64-128 kbps, stereo 128-256 kbps | OFFICIAL | same | - |
| Megaphone (Spotify) | required: MP3, 44.1khz or higher, ads match episode stereo/mono; recommended: -16 LUFS, "1db True Peak", range 6-9db; no bitrate specified | OFFICIAL (platform) | https://support.megaphone.fm/en/articles/1561164-audio-specs-and-standards | April 22, 2024 |
| Acast | ads encoded at 128kbps MP3; episode audio should match | SNIPPET | https://learn.acast.com/en/articles/2609662-optimize-audio-files-for-podcast-delivery | - |
| IAB podcast measurement | download counts after header plus one minute of content; 24-hour window; v2.2 and a v2.3 (covering video) reported | COMMUNITY, SNIPPET | https://www.iab.com/guidelines/podcast-ad-metrics-guidelines/ | - |

### 1D. Cinema
| Fact | Value | Tag | Source | Page date |
|---|---|---|---|---|
| DCM (UK) picture | DCM builds the DCP itself from a TIFF sequence: 4K 3996 x 2160 (1.85), UHD 3840 x 2160, 2K 1998 x 1080, FullHD 1920 x 1080; title safety 1798 x 972 (2K), 1605 x 903 (FullHD); 8-16 bit; rec709; 24fps or 25fps (25 is slowed to 24, runs 4% longer); progressive; no clock, no black frames; QuickTime NOT accepted | VENDOR | https://www.dcm.co.uk/uploads/files/Production/DCM-Cinema-Production-Requirements-2026.pdf | 2026 |
| DCM audio | Immersive (IAB .mxf) and/or 5.1 required; a 5.1 is always required; six mono WAV (L, R, C, LFE, Ls, Rs); 48 kHz, 24 bit, 24 fps; fail if "Leq(m) exceeds 82 dB as measured in accordance with ISO 21727, BS 5550-7.4.2, and SAWA Standards and Recommendations of 2000"; LR-only stereo fails | VENDOR | same | 2026 |
| DCM supers | minimum text height 16 pixels, recommended 18 (at 1998x1080 / 1920x1080); 32 / 36 at 4K/UHD | VENDOR | same | - |
| DCM clearance and timing | CAA final approval required for all ads; BBFC also for charity / public information, government, film and TV content; CAA lead time approximately 24 hours, contentious copy to a Friday copy panel; allow at least 48 hours for assets and 24 hours for clearance | VENDOR | same | - |
| Pearl & Dean Ireland | DPX / TIFF sequence; 1998 x 1080; 24fps progressive; 5.1 as 6 x mono WAV, "48hz & 24bit" (as printed); reference -20dbfs; max 82 Leq(M); lead time 5 working days (ROI), 10 working days (NI); CAA fee €180 (ROI), stg £216 inc VAT (NI); alcohol ads cleared by CCCI | VENDOR | https://pearlanddean.ie/wp-content/uploads/2026/03/PAD-Cinema-Ad-Specs-2026-02.pdf | 2026-02 |
| Screenvision (US) standard pre-show | MOV, Apple ProRes 422 HQ; 1920x1080p; 24fps (23.98 accepted); FLAT; stereo or 5.1 (5.1 must also carry LT/RT on ch 7-8); "Audio Level: 78 Leq(m)"; title safe 10%, image safe 5% | VENDOR | https://screenvisionmedia.com/wp-content/uploads/2024/08/SV-National-Commerical-Delivery-Specs-2024-updated.pdf | 2024 |
| Screenvision trailer positioning | both Flat 1998 x 1080 (1.85) and Scope 2048 x 858 (2.39) required; 24fps; 5.1; "Audio Level: 82 Leq(m)" | VENDOR | same | 2024 |
| Screenvision lobby | 1920 x 1080 and 1080 x 1920, ProRes 422 HQ, 24fps | VENDOR | same | - |
| NCM (US) | preferred .mov 1920 x 1080, 23.976 (23.98 / 24), ProRes 422 HQ (Mac) / DNxHD (PC), 5.1 + Lt/Rt PCM 48kHz/24-bit; also accepts 1998 x 1080, 2048 x 1080, 2048 x 858; action safe 1728 x 972; every ad must have audio; no Dolby-certified mix required | VENDOR | https://www.ncm.com/_files/ugd/20be08_bd2e6551da7c4626af6e93213ee43faf.pdf | 2024 |
| NCM loudness guidance | "does not exceed -10 dBFS peaks ... should not exceed -24 LKFS"; VO starts no sooner than :01 and ends no later than :01 before the end | VENDOR | https://www.ncm.com/_files/ugd/20be08_30b6fbed19a34ecc81475f0f61c5fbcb.pdf | 2023 |
| Trailers 85 Leq(m) (TASA) | 85 dB Leq(m) for trailers, 82 for commercials | COMMUNITY, SNIPPET | no official TASA/SAWA page opened | - |

### 1E. In-app / mobile game ads
| Fact | Value | Tag | Source | Page date |
|---|---|---|---|---|
| Unity Ads video | 60 seconds or less (30 to 60 s is a beta); H.264 MP4; 16:9 or 9:16; recommended 10 MB, maximum 100 MB; end card mandatory | OFFICIAL | https://docs.unity.com/en-us/grow/acquire/creatives/video/specifications | "Last updated 4 months ago" |
| Unity playable | single minified index.html, less than 5 MB, all assets inlined as base64, no network requests; Android 5+ / iOS 13+; one responsive build for portrait and landscape; full-screen MRAID only; start after MRAID ready when viewable; store opens via mraid.open only after gameplay and a player tap | OFFICIAL | https://docs.unity.com/en-us/grow/acquire/creatives/playable/specifications | "Last updated 23 days ago" |
| Unity MRAID version / end-card images | MRAID 3.0; end cards 800 x 600, 600 x 800, 800 x 800; JPG/PNG/GIF up to 5 MB | SNIPPET | https://docs.unity.com/en-us/user-acquisition/creatives/creative-specifications | - |
| AppLovin playable | 5 MB or smaller; single HTML file, resources embedded base64 or base122; both orientations; no redirect on first tap; audio muted until first interaction; no external calls; "must support MRAID v2.0"; click-through via mraid.open() | OFFICIAL | https://support.axon.ai/en/app-discovery/creatives/best-practices-and-guidelines | © 2026 |
| AppLovin video / image | MP4, MOV; 9:16 (Portrait); max 1 GB; max 60 s. Images GIF/JPEG/PNG max 10 MB; endcard 9:16 (min 270x480); banner 32:5 (min 320x50); MREC 6:5 (min 300x250) | OFFICIAL | same | - |
| Meta playable (incl. Audience Network) | single HTML5 file max 5MB, or ZIP total max 5MB with at most 100 files and index.html at root; "Must work without mraid.js"; no external network calls; portrait and responsive; FbPlayableAd.onCTAClick() strongly recommended; JS redirects not allowed | OFFICIAL | https://www.facebook.com/business/help/412951382532338 | not shown |
| Meta playable placements | Facebook Stories, Newsfeed, Audience Network Interstitial and Rewarded, Instagram Feed/Stories; lead-in videos not shown on Audience Network; only lead-in video shown on Instagram; App Installs objective only | OFFICIAL | https://developers.facebook.com/docs/app-ads/formats/playable-ad | not shown |
| ironSource Ads | platform renders timer and close button; keep 30x30 px corners clear | SNIPPET | https://docs.unity.com/grow/is-ads/user-acquisition/creatives/interactive-requirements (redirected to a generic page when opened) | - |

### 1F. Influencer marketing
| Fact | Value | Tag | Source | Page date |
|---|---|---|---|---|
| FTC Endorsement Guides, 16 CFR 255 | endorser "could be or appear to be an individual, group, or institution"; preamble: the new language is not limited to virtual influencers and also covers fake-review writers and non-existent entities | OFFICIAL | https://www.govinfo.gov/content/pkg/FR-2023-07-26/html/2023-14795.htm | 88 FR 48092, July 26, 2023 |
| FTC "clear and conspicuous" | "difficult to miss (i.e., easily noticeable) and easily understandable by ordinary consumers" | OFFICIAL (opening words read; rest SNIPPET) | same | - |
| ASA/CAP + CMA influencer guide (UK) | fourth edition, dated 23 Oct 2026; an influencer "includes any human, animal or virtually produced persona"; recommended labels #Ad, #Advert, #Advertising, #Advertisement, #AdvertisementFeature; advises against "Sponsorship / Sponsored / Spon / Sp" and brand-tag-only; a platform label may be sufficient if upfront and prominent; affiliate links and codes count as advertising | OFFICIAL | https://www.asa.org.uk/advice-online/influencers-guide.html ; PDF https://www.asa.org.uk/static/17cf70a4-f904-4684-a68c8310ba7700e1/Influencers-guide-to-making-clear-that-ads-are-ads.pdf | 23 Oct 2026 |
| ASA on AI disclosure | "no blanket legal requirement in the UK to disclose the use of AI in ads"; no AI-specific Code rules, existing rules apply; test: would the audience be misled without disclosure | OFFICIAL | https://www.asa.org.uk/news/disclosure-of-ai-in-advertising-striking-the-balance-between-creativity-and-responsibility.html | 29 May 2025 |
| EU | advertising incl. brand partnerships, content in exchange for products or services, and affiliate marketing "must be disclosed"; Hub reflects the CPC Network's 5 Key Principles | OFFICIAL | https://commission.europa.eu/influencer-legal-hub_en | brief dated 11 October 2023 |
| EU AI Act Art. 50 | transparency duties applied from 2 August 2026; realistic synthetic people must be labelled; fines up to EUR 15 million or 3% | COMMUNITY, SNIPPET (law-firm pages) | official text not opened | - |
| Instagram | branded content policies "require that you use the paid partnership label to tag the brand"; available in Feed, Stories, Broadcast Channels, Live, Reels, videos; brand must approve the tag | OFFICIAL | https://help.instagram.com/1109894795810258 | not shown |
| TikTok | "you must turn on the commercial content disclosure setting"; adds a Paid partnership label | OFFICIAL | https://ads.tiktok.com/help/article/about-the-content-disclosure-setting-for-creators | Last updated: April 2026 |
| TikTok Spark Ads (usage rights) | brand runs a creator's organic post "with their authorization"; duration of the authorization code is customizable; engagement is credited to the original post | OFFICIAL | https://ads.tiktok.com/help/article/spark-ads | not shown |
| YouTube | must select the paid promotion option in video details; adds a disclosure label at the start of the video | OFFICIAL | https://support.google.com/youtube/answer/154235 | not shown |

## 2. CONFLICTS
1. Spotify audio loudness: -16 LUFS (+/- 1.5) on the current audio page vs "RMS normalized to -14 dBFS" on the in-stream video page and (SNIPPET) an older Help Center audio page. Both on ads.spotify.com.
2. Spotify audio file size: 50 MB (current en-US page, opened) vs 1MB for Direct IO / Ad Studio (SNIPPET, regional or older pages).
3. Cinema ad loudness: 82 Leq(m) at DCM and Pearl & Dean vs 78 Leq(m) for Screenvision standard pre-show (82 only for trailer positioning) vs NCM's -24 LKFS / -10 dBFS guidance.
4. Playable MRAID: Unity 3.0 (SNIPPET), AppLovin "MRAID v2.0", Meta "must work without mraid.js". One build cannot serve all three unchanged (INFERENCE from the three pages).
5. Digital billboard dwell: OAAA "six to eight seconds"; Lamar "6-10 seconds"; JCDecaux UK D48 12s; Bauer UK 10 seconds; OUTFRONT 8 or 15 seconds.
6. Unity video length: 60 seconds or less (current) vs 30 seconds in old SDK 3.x docs (SNIPPET).
7. Clear Channel UK spec links now live on bauermediaoutdoor.co.uk; clearchannel.co.uk did not connect from this session.

## 3. COULD NOT OPEN / UNKNOWN
- www.ftc.gov (FAQ "What People Are Asking"): 403 bot block in curl and Playwright. Virtual/AI-influencer FAQ wording UNKNOWN; only the Federal Register text was read.
- clearchannel.co.uk, oceanoutdoor.com (spec page 404), dpaaglobal.com: no connection or not found. Ocean Outdoor specs UNKNOWN.
- tech.ebu.ch (403) and knowledgehub.ebu.ch (returned HTML, not the PDF): EBU R128 s1/s2 figures are SNIPPET only.
- lamar.com/howtoadvertise/Specs: 404.
- iab.com New Ad Portfolio and MRAID pages loaded with no usable body text; IAB/DPAA/OAAA/WOO programmatic DOOH creative guideline not found. IAB DOOH Measurement Guide (July 2025) seen as SNIPPET only: https://www.iab.com/wp-content/uploads/2025/07/IAB_DOOH_Measurement_Guide_July_2025.pdf
- SAWA and TASA official loudness pages: not found.
- Print (PDF/X-1a / PDF/X-4, 300 dpi, 3 mm / 0.125 in bleed, total ink limits, ISO 12647, SWOP, ad unit names): NOT RESEARCHED. Only confirmed that Fogra lists characterisation data FOGRA39 to FOGRA60 and FOGRA51/52 (V1.0, 23.09.2020) at https://www.fogra.org/en/downloads/work-tools/characterisation-data ; iso.org returned nothing.
- Radio words-per-second from Radiocentre or RAB: none found. EU or US legal-disclaimer practice for radio: not researched.
- Acast official ad spec page, IAB podcast guideline text (v2.2 / v2.3), pre/mid/post-roll definitions, YouTube audio ads: not opened.
- ironSource / LevelPlay creative specs, Meta Audience Network rewarded-video lengths, IAB MRAID 3.0 text: not confirmed.
- Meta partnership ads (whitelisting) page, EU AI Act official text, typical deliverables and usage-rights terms: not opened.
- Israeli outdoor or cinema media-owner spec pages: not searched.
- JCDecaux UK motion formats (Digital 6-sheet, Westfield): pages rendered but the spec block was not captured.

## 4. TOP 10 URLS FOR THE VERIFIER
1. https://www.dcm.co.uk/uploads/files/Production/DCM-Cinema-Production-Requirements-2026.pdf
2. https://ads.spotify.com/en-US/ad-specs/audio-ad-specs/
3. https://ads.spotify.com/en-US/ad-specs/in-stream-video-ad-specs/
4. https://oaaa.org/wp-content/uploads/2022/09/DOC-Digital-Aspect-Ratios-.pdf
5. https://oaaa.org/wp-content/uploads/2022/09/OOH-Print-Production-Specifications-Cheat-Sheet.pdf
6. https://www.bauermediaoutdoor.co.uk/resources/specifications/adshel-live-specification
7. https://docs.unity.com/en-us/grow/acquire/creatives/playable/specifications
8. https://www.facebook.com/business/help/412951382532338
9. https://www.asa.org.uk/static/17cf70a4-f904-4684-a68c8310ba7700e1/Influencers-guide-to-making-clear-that-ads-are-ads.pdf
10. https://www.govinfo.gov/content/pkg/FR-2023-07-26/html/2023-14795.htm
Also worth a pass: https://screenvisionmedia.com/wp-content/uploads/2024/08/SV-National-Commerical-Delivery-Specs-2024-updated.pdf ; https://podcasters.apple.com/support/893-audio-requirements ; https://support.axon.ai/en/app-discovery/creatives/best-practices-and-guidelines ; https://www.bauermedia.co.uk/audio-specifications/
