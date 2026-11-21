# 01 - TV, cable, streaming and connected-TV ad delivery specs (global)

Read: 20-21 Nov 2026. STATUS: DRAFT - NOT YET VERIFIED. Do not copy any number into a skill until `15-verification-log.md` shows it PASS.
Tags per fact: OFFICIAL / VENDOR / COMMUNITY / INFERENCE / UNKNOWN. "SNIPPET ONLY" = seen in a search result, page not opened.
Origin: sub-agent report `research-raw/R1a-tv-streaming-ctv-specs.md`, reformatted only (no fact added or removed by the main agent).

R1a REPORT - TV / cable / streaming-CTV ad delivery specs (global, ex-Israel). All pages read 20-21 Nov 2026. Environment note: built-in WebFetch could not resolve any host in this session; everything below was read with curl or headless Playwright Chromium unless marked SNIPPET ONLY (WebSearch result text only).

## 1. FINDINGS

### 1A. Streaming / CTV platforms (official spec pages)

**Netflix Ads** - OFFICIAL - https://advertising.netflix.com/en-us/creative-specs (no page date; footer (c) 2026; old partnerhelp/backlothelp "Ad Creative Source Specification" URL now redirects here)
| Fact | Value |
|---|---|
| Durations (SVOD) | Pre-roll :10s, :15s, :20s, :30s; Mid-roll :10s, :15s, :20s, :30s, :45s, :60s, :75s |
| Durations (Live) | :15s, :30s (others via account rep) |
| Container | MP4, MOV ("MOV not accepted on Amazon DSP") |
| Codec | Recommended Apple ProRes in MOV (422 HQ, 422, 422 LT); accepted H.264 in MP4 or MOV |
| Resolution / aspect | Recommended 1920x1080; accepted 1280x720, 3840x2160; 16:9; progressive |
| Frame rate | 23.976, 24, 25, 29.97, 30, 50, 59.94, 60; constant |
| Colour | BT.709 recommended; "All content must be SDR. HDR is not supported." |
| Bitrate H.264 | Recommended at least 8Mbps 720p, 12Mbps 1080p, 20Mbps 2160p; accepted at least 2 / 6 / 8 Mbps |
| Bitrate ProRes | Recommended at least 42 / 80 / 120 Mbps; accepted at least 40 / 60 / 100 Mbps |
| File weight | "1GB or less files are recommended" |
| Audio | PCM recommended, AAC-LC accepted (192kbps minimum); 2 channel stereo; 48kHz; 16 or 24 bit; exactly 1 video + 1 audio track, durations match within 500 ms |
| Loudness | "-24LKFS ±2"; "True peak does not exceed -2 dBFS" |
| Letter/pillar box | Permitted, not recommended; black only; "Must never exceed 37% of the viewable area" |
| Safe zone | Avoid top-right (ad timer), outer ~5-10% margins, bottom-right ~25-30% when QR present |
| QR | No advertiser QR/linkouts; Netflix overlays its own generated QR |
| Tags | VAST 2.0 & 3.0 preferred; allow at least 72 hours pre-registration; restricted categories up to five days |
| Live delivery | Recommended vendor for Live video ad delivery: Extreme Reach |
| Pause ad | PNG or JPEG, minimum 1728 x 1440 (recommended 2592 x 2160 or higher) |

**Amazon Ads - Streaming TV & Prime Video** - OFFICIAL - https://advertising.amazon.com/resources/ad-specs/dsp/video/streaming-tv-prime-video-ads (no date)
| Fact | Value |
|---|---|
| Max file size | 500MB |
| Aspect / min frame | 16:9; 1920x1080 |
| Min video bitrate | Prime Video: 15mbps; Twitch, Fire TV Channels, 3P Apps, 3P Exchanges: 8mbps; recommended 50mbps (Prime Video campaigns) |
| Frame rate | 23.976 (recommended), 24, 25, or 29.97; constant |
| Formats | Video H.264, MPEG-2 or MPEG-4; audio AAC; site serving requires MP4 |
| Audio | Min 192kbps; 44.1kHz or 48kHz; minimum 2 channels. No loudness figure on the page |
| Prime Video lengths (s) | US, CA: 15, 30, 45, 60. UK, DE, AT, FR, IT, ES, BR, IN: 10, 15, 20, 30, 40, 60. MX, AU: 15, 20, 30, 40, 60. JP: 15, 30 |
| Twitch lengths | US/CA 15, 30; UK/DE/MX/JP 15, 20, 30 |
| 3P STV apps | 06s, 10s, 15s, 20s, 30s, 45s, 60s, 75s and 90s |
| Boxing | Strongly discouraged; pillarbox or letterbox permitted "provided they are not in the same ad" |
| 3rd-party tags | Inline VAST 2.0 or 3.0; no VPAID, no wrapper tags |
| Other | No click-style CTA buttons; downloadable Action Safe template on page |

**Disney+ / Hulu "Video Commercial"** - OFFICIAL - https://products.disneyadvertising.com/video-commercial/ (no date; old disneyadvertising.com/ad-specs/ returns 404)
| Fact | Value |
|---|---|
| Resolution | Preferred 1920 x 1080; accepted 1280 x 720; 16:9 required (1:1 or 9:16 rejected) |
| Boxing | Letterboxing and pillarboxing not allowed (exception via rep) |
| Video | "Constant bitrate (CBR) 10-40 Mbps"; 4:2:2; single video track; progressive |
| Container / codec | .MOV, .MP4, .M4V; Apple ProRes 422 HQ or H.264 |
| Max file weight | Partner, VAST or programmatic-served: 1.9 GB; Hulu-served: 250 MB |
| Frame rate | 23.98, 24, 25, 29.97 or 30 fps, native, constant |
| Audio | Required; two channels only; 128 Kbps minimum CBR; 16- or 24-bit (PCM); 44.1 or 48 kHz; AAC or PCM; exactly one audio track |
| Leaders | Must be submitted without slates, countdowns |
| Tags | VAST 2.0 & 3.0 from approved vendors; no wrappers, no VPAID |
| CTA / QR | Clickable-looking CTA buttons not allowed; URLs, hashtags accepted; QR accepted subject to review |
| Turnaround | Up to 5 business days from final assets |
| Duration | Not in the text read. SNIPPET ONLY: ":15 or :30" (Disney "Ad Selector", https://products.disneyadvertising.com/?p=9421) |
| Loudness | Not in the text read. SNIPPET ONLY: "24 LKFS ±2 dB" (Disney Marvel pre-roll PDF, https://files.disneyadvertising.com/MediaKit/Marvel/marvel_pre-roll.pdf) |

**Roku Ads Manager** - OFFICIAL - https://help.ads.roku.com/en/articles/7154647-creative-guidelines (dated September 23, 2025)
| Fact | Value |
|---|---|
| File | .mov or .mp4; maximum 1 GB; file name 170 character max |
| Length | 6 seconds - 92 seconds |
| Video | Must be 16:9; 23.98, 25.00, 29.97 FPS; AVC or ProRes 422 HQ; minimum 6 Mbps |
| Audio | PCM preferred, AAC accepted; minimum 96 kbps; 16- or 24-bit; 2-channel stereo; 48 kHz |
| Review | Tech check in minutes; manual review 2-3 business days |
Roku Advertising Guidelines - OFFICIAL - https://docs.roku.com/published/advertisingguidelines/en/us : "Ads should be :15 or :30 in duration. Exceptions may be made for :60 ads."; "Low resolution (less than 720 x 480p) or low frame rate (less than 30 fps) is not permitted."

**Paramount Ads Manager (Paramount+, CBS etc.)** - OFFICIAL - https://adsmanager.paramount.com/creative-center/tech-specs ((c) 2026)
| Fact | Value |
|---|---|
| Duration | :15 or :30 |
| Video | 1280x720 (16:9) minimum; mp4 H.264 high profile (preferred), mov Apple ProRes 422 or 422HQ; progressive only; 6 Mbps minimum; 8 bits minimum |
| Frame rate | 23.98 (23.976), 24, 25, 29.97 or 30 fps; constant |
| File size | 10 GB max |
| Audio | 2 channels only, AAC; 192 KBPS minimum; 48 kHz; 16 or 24 bits |
| Loudness | "-24 LUFS +/- 2 LUFS, based on ATSC A/85"; max peak "Never excess -6db" |
| Other | No leaders, slates, countdowns; no black bars; remove 3:2 pull-down |
| Budget (context) | $500 - $260,000 per campaign, CPM model |

**Samsung Ads (Samsung DSP, "Samsung Hosted Video")** - OFFICIAL - https://help.dsp.samsungads.com/docs/video (updated Mar 6, 2025)
| Fact | Value |
|---|---|
| Format | MP4; H.264; audio AAC or MP3; 16:9; recommended 1920 x 1080; CTV minimum 1280 x 720 |
| CTV file size | Maximum 50 MB; recommended 30 MB |
| CTV duration | Between 5 and 90 seconds; recommended 15-30 seconds |
| Bitrate | Maximum 10 Mbps / 10,000 kbps; minimum 5 Mbps / 5,000 Kbps; "Some publishers or exchange sellers require... 15,000 kbps" |
| Frame rate | CTV 30 fps recommended |

**Peacock / NBCU, Max / WBD** - not opened (see section 3). SNIPPET ONLY for NBCU: ProRes 422 HQ preferred, "-24LKFS +/-2", lengths :6s, :15s, :30s, :45s, :60s, :90s, Ad-ID required.
**YouTube CTV** - pointer only: https://support.google.com/google-ads/answer/2375464 (OFFICIAL, opened; format overview page).

### 1B. IAB Tech Lab - "Ad Format Guidelines for Digital Video and CTV" - OFFICIAL
Landing page https://iabtechlab.com/dv-ctv-ad-format-guidelines/ (last updated January 15, 2024); PDF https://iabtechlab.com/wp-content/uploads/2022/03/Ad-Format-Guidelines_DV-CTV.pdf (27 pages, "Released August 2022").
| Fact | Value |
|---|---|
| Linear ad durations | 6, 15, 30 seconds; also bumpers 3-10 seconds, 60 second spots; long "infomercial" 1-5 minutes or longer |
| Ready-to-serve | MP4 H.264; three files (high/medium/low) or HLS / MPEG-DASH; 4:2:0; progressive; no leaders or slate |
| Target bitrates | 500-700 kbps low; 700-1500 kbps medium; 1500-2500 kbps for 720p; formula width x height x frame rate x VBPP |
| Frame rate | Keep native: 29.970 (NTSC countries), 25 (PAL countries), 23.976 (film look); avoid conversion, telecine, 3:2 pulldown |
| Ready-to-serve audio | AAC-LC 128-192 kbps or HE-AACv1 64-128 kbps; 44.1 kHz or 48 kHz |
| Audio levels | "-24 LKFS (+/- 2.0 dB) in the US as per ATSC A/85"; "-23 LUFS (+/- 1.0) in the EU as per EBU R128"; "Peak levels should not exceed -6 db true peak" |
| Mezzanine video | 50Mbps VBR or 15-30 CBR; 16:9, 1920x1080 or 1280x720; 4:2:0 or 4:2:2; PAL 25 / 23.98 / 29.97; .mov or .mp4; "Apple ProRes preferred but may exceed file size threshold for some vendors"; H.265 "may not yet be widely accepted"; progressive; no slate, countdown, bars or tone; no burned-in boxing |
| Mezzanine audio | AAC 192 kbps (PCM allowed for mezzanine); 2 channel stereo; 48kHz |
| VAST | Mezzanine + multiple ready-to-serve files supported from VAST 4.0; SIMID replaces VPAID |
COMMUNITY / SNIPPET ONLY: a major revision was put out for public comment on 11 Dec 2025, with a second comment round to 16 Jul 2026 (ppc.land, newscaststudio.com) - not confirmed on iabtechlab.com.

### 1C. UK broadcast (Clearcast / DPP / Cape, formerly Peach)
| Fact | Value | Tag | Source |
|---|---|---|---|
| Clearance | All UK TV ads cleared by Clearcast; sponsorship cleared by broadcasters | VENDOR | https://help-advancedtv.cape.io/hc/en-us/articles/35315002536849-UK-Overview |
| Clock number, short-form (under five minutes) | AAA/BBBB123/456 = 3-letter agency code (assigned by Clearcast) / four letters + three numbers / duration as three digits (030 = 30 s) | OFFICIAL | https://help.clearcast.co.uk/en/article/how-do-i-create-a-clock-number-and-slate |
| Clock number, long-form | AAA/BBBB12/3456 (duration four digits, 1800 = 30-minute) | OFFICIAL | same |
| Sponsorship ident (SSI) | SABC/ABCD001/10; idents do not run longer than 60 seconds | OFFICIAL | same |
| Slate timing | Clock 09:59:50:00 to 09:59:56:24; black 09:59:57:00 to 09:59:59:24; ad starts 10:00:00:00; clock number in capitals on slate; changing the file means a new clock number | OFFICIAL | same |
| Clearcast Library layout | 10 second clock slate + ad + either 0 second or 5 second end freeze; 6 frames of audio silence at start and end | OFFICIAL | https://clearcast.co.uk/wp-content/uploads/2024/07/Clearcast-Library-Technical-Specification-Guide-v1.6.pdf (file name v1.6, cover says v1.5) |
| Clearcast QC | Colour ITU-BT.709; gamut EBU R103; PSE ITU-R BT.1702; loudness EBU R128 -23 LUFS; peak -1dbTP; stereo on ch 1 and 2 | OFFICIAL | same |
| Clearcast TVC formats | XDCAM 50: MXF OP-1a, MPEG 4:2:2, 50 Mbit/s, 1920 x 1080, 25 FPS, interlaced, PCM 48Khz 24 bit. Also ProRes 422 HQ (MXF or MOV, 10 bit), DNxHD, AVC-Intra Class 100 (114 Mbit/s), all 1920 x 1080, 25 FPS, interlaced | OFFICIAL | same |
| Clearcast rough cut | MP4 H264, 15 Mbit/s, 1920 x 1080, 25 FPS, interlaced or progressive, AAC | OFFICIAL | same |
| DPP012 v2.0 loudness | -23.0 LUFS ±0.2LU; true peak recommended max -3dBTP, "will fail if... exceeds -1dBTP"; max short-term -18.0 LUFS (EBU R128 s1); "R128 S1 should be used for commercials and R128 for infomercials" | OFFICIAL (DPP document, copy hosted by Channel 4 Sales) | https://cdn-2.4sales.com/staging/2025-11/dpp012-production-and-post-production-commercial-guidance-v2.0%5B43%5D.pdf |
| DPP012 caption safe area | One area for 16:9 (EBU R 95-1): 80% of active width, 90% of active height; HD pixels 191-1726, lines 55-1026 | OFFICIAL | same |
| DPP012 legal text | BCAP: preferred minimum text height 30 TV lines for HD, reducible to 26 lines on opaque single-colour background | OFFICIAL | same |
| DPP012 other | Video per BT.709-6; PSE test to Ofcom guidance; SOM 10:00:00:00; "clock or slate is to precede each item for a duration of 7 seconds"; subtitles per Ofcom best practice | OFFICIAL | same |
| Peach is now Cape.io | peach.me redirects (301) to cape.io | VENDOR | https://cape.io/news/deliver-ads-in-the-uk-ireland (10 Apr 2024) |
| Cape UK/ROI | Upload one XDCAM file; 10" pre-roll = 7" slate/countdown + 3" black; first and last 6 frames mute; instructions via CARIA; allow minimum 5 weeks | VENDOR | same + UK Overview |
| UK lead times | 2 working days; Sky Adsmart 7 working days; BVOD 5 working days; Finecast 10 working days | VENDOR | https://cape.io/news/deliver-ads-in-the-uk-ireland |
| ROI | Cleared per channel (RTE and/or Virgin; Clearcast for UK channels) | VENDOR | same |

### 1D. US / Canada broadcast (XR / Extreme Reach, Comcast AdDelivery)
| Fact | Value | Tag | Source |
|---|---|---|---|
| XR layout | 5-second slate -> 2 seconds of black -> ad; active content starts frame 168 (23.98 fps) or 210 (29.97 fps); slate mute; fades max 10 frames | VENDOR | https://helpcenter.xr.global/hc/en-us/articles/5758928813332-North-America-Broadcast-Specifications-and-Requirements |
| XR slate content | AD ID (must match metadata), Advertiser, Title, Duration | VENDOR | same |
| XR preferred file | MXF OP1a XDCAM HD 422, 50 Mbps, or QuickTime ProRes 422 HQ; 1920 x 1080, 23.98, progressive, 4:2:2; PCM 16 or 24 bit 48 kHz. Accepted: MP4 AVC Main@L4, 20 Mbps, AAC 224 Kbps | VENDOR | same |
| XR alternatives | 1920 x 1080 29.97 interlaced upper field; 1080 29.97 progressive; 1280 x 720 59.94 progressive | VENDOR | same |
| XR audio | ATSC RP A/85 and ITU-R BS.1770-3; target -24 LKFS (auto-normalised if not); true peak must be below -2 dB TP, recommended below -6 dB TP; stereo and 5.1 plus stereo | VENDOR | same |
| Title safety | SMPTE ST 2046-1: safe title 90% of width and height; up to 93% tolerated, beyond 93% rejected | VENDOR | same |
| Video levels | BT.601, BT.709, EBU R 103; 8-bit 16-235, 10-bit 64-940 | VENDOR | same |
| Captions | "In Canada closed captions are mandatory for all commercials"; optional paid service in US | VENDOR | same |
| Ad code | Ad-ID or ad code; HD file names end with "H" (not "HH"; not required in Canada); max length ABC and ESPN 13, NBC 15, DIRECTV 16, CBS 20, FOX and Discovery 25 characters | VENDOR | same |
| Clearance | US: no central body, each network's BS&P. Canada: mandatory, ThinkTV / Telecaster | VENDOR | same |
| Comcast AdDelivery Lite lengths | No slate, no black; exact lengths 15 sec/450 frames, 30 sec/900, 60 sec/1800, 90 sec/2700, 120 sec/3596, 5 min/8992 | VENDOR | https://support.comcasttechnologysolutions.com/sites/default/files/files/2021-11/2022%20-%20ad-delivery-format-specs%20LITE%20.pdf |
| Comcast HD formats | MPEG-2 (.mpg, recommended) 20-100 Mbps; ProRes 422 LT/422/HQ (.mov) 40-220 Mbps; DNxHD 145/220; H.264 15-100 Mbps; 1920x1080 29.97 (1080i) or 23.976 (1080p), 1280x720 59.94; 16:9 | VENDOR | same |
| Comcast audio / captions | 48KHz, 16 bit; stereo or 5.1; instantaneous peak max -8dBFS, average peak max -10dBFS; captions EIA-608 and EIA-708 | VENDOR | same |

### 1E. Standards and bodies (links)
| Item | Fact | Tag | Source |
|---|---|---|---|
| ITU-R BS.1770 | "Algorithms to measure audio programme loudness and true-peak audio level"; "Approved in 2023-11" | OFFICIAL | https://www.itu.int/rec/R-REC-BS.1770 |
| ATSC A/85 | Current version A/85:2026-07, approved 8 July 2026; separate "Loudness and True Peak Quick Reference" | OFFICIAL | https://www.atsc.org/atsc-documents/a85-techniques-for-establishing-and-maintaining-audio-loudness-for-digital-television/ |
| EBU R128 | Page not opened (Cloudflare). -23 LUFS confirmed via DPP012, Clearcast, IAB | UNKNOWN for version/date | https://tech.ebu.ch/publications/r128 |
| DPP AS-11 | Spec page (redirects to /specs/as-11); DPP012 refers to thedpp.com/filedelivery | OFFICIAL (page shell only) | https://www.thedpp.com/specs/as-11 |
| ARPP (France) | French ad self-regulatory body; "Mandatory Pre-Clearance before TV and VOD Broadcast"; submissions via ARPP.PRO | OFFICIAL | https://www.arpp.org/the-arpp/ |
| Ad-ID (US) | Site reachable; detail page tried returned "page not found" | UNKNOWN | https://www.ad-id.org/ |

## 2. CONFLICTS
- UK slate length: Clearcast Library says "10 second clock slate" (7 s clock + 3 s black); DPP012 v2.0 says clock/slate "for a duration of 7 seconds". Same layout, different wording.
- True peak: Clearcast -1dbTP; DPP012 recommends -3dBTP, fails above -1dBTP; XR must be below -2 dB TP (recommends -6); Netflix -2 dBFS; Paramount -6db; IAB -6 db true peak.
- Loudness tolerance: DPP ±0.2LU; IAB says EU ±1.0; US platforms ±2.
- IAB release date: PDF "Released August 2022" vs landing page "Released September 2022"; PDF URL path is /2022/03/.
- Roku: Ads Manager accepts 6-92 seconds and 23.98/25.00/29.97 FPS; Roku Advertising Guidelines say :15 or :30 (:60 exception) and "less than 30 fps is not permitted".
- Netflix durations: search snippet of the older Netflix help page gave 10, 15, 20, 30 or 60 s; current page adds :45s and :75s mid-roll. Mountain blog (COMMUNITY, SNIPPET) says letterboxing not allowed; Netflix page permits it up to 37%.
- Disney bitrate / file size: Disney page CBR 10-40 Mbps, 1.9 GB / 250 MB; Vibe help (COMMUNITY, SNIPPET, https://help.vibe.co/en/articles/11131427-peacock-disney-hulu-creative-guidelines) says 15-30 Mbps and 10 GB.
- Clearcast Library PDF: "ProRes 422 HQ" block lists "Format: AVC ... 114 Mbit/s" (looks like a copy error in the source; INFERENCE).
- Comcast Lite PDF: "Average Levels" row reads -20dBFS, -20dBFS, "-2 dBTP" in extracted text; third value may be an extraction artefact.

## 3. COULD NOT OPEN / UNKNOWN
- NBCU / Peacock: together.nbcuni.com/specs and /nbcu-creative-guidelines/peacock redirect to https://nbcuniversal-creative-guidelines.scrollhelp.site/nbcuadspecs/nbcuniversal-standard-digital-video-guidelines - proxy refused that host (curl 000, Playwright ERR_TUNNEL_CONNECTION_FAILED). Only snippets.
- WBD / Max: adspecs.wbd.com does not resolve; https://brand.hbomax.com/av-specs requires login (access denied). SNIPPET ONLY: -24 LKFS ±2dB, -2dBTP. No official ad-spec URL confirmed.
- Samsung Ads public spec page: https://www.samsung.com/us/business/samsungads/resources/ad-specs/ redirects to /resources/ (no specs). go.samsungads.com/nasb-creative-ads-specs and helpcenter.admanager.samsungads.com not tried.
- EBU R128 page (tech.ebu.ch): Cloudflare bot check in curl (403) and Playwright.
- Ad-ID code structure and pricing; Comcast newer than the "2022" PDF; XR closed-caption sub-page; XR DACH / Generic PAL / AUNZ pages (URLs found, not read: https://helpcenter.xr.global/hc/en-us/articles/26261537064852-DACH-Broadcast-Specifications-and-Requirements , https://helpcenter.xr.global/hc/en-us/articles/49477563876628-Generic-PAL-R68-Broadcast-Specifications-and-Requirements).
- DPP013 (AS-11 X6 commercial technical requirements) and the official thedpp.com download of DPP012 not read; DPP012 document date not captured (URL path 2025-11).
- Not researched: per-country linear spot-length norms beyond the tables above, HDR rules for linear broadcast, FCC caption rules for ads (fcc.gov returned 403), ITV / Channel 4 / Sky own spec pages (itv.com unreachable), France PubID, Germany, Australia (Free TV OP-59, CAD).
- Hulu/Disney duration and loudness on the official page (tabbed content not fully expanded).
- Netflix "12 ad markets" list and restricted categories policy not opened.

## 4. TOP 10 URLS FOR THE VERIFIER
1. https://advertising.netflix.com/en-us/creative-specs (accordions need clicking)
2. https://advertising.amazon.com/resources/ad-specs/dsp/video/streaming-tv-prime-video-ads
3. https://products.disneyadvertising.com/video-commercial/
4. https://help.ads.roku.com/en/articles/7154647-creative-guidelines
5. https://adsmanager.paramount.com/creative-center/tech-specs
6. https://iabtechlab.com/wp-content/uploads/2022/03/Ad-Format-Guidelines_DV-CTV.pdf
7. https://help.clearcast.co.uk/en/article/how-do-i-create-a-clock-number-and-slate
8. https://clearcast.co.uk/wp-content/uploads/2024/07/Clearcast-Library-Technical-Specification-Guide-v1.6.pdf
9. https://helpcenter.xr.global/hc/en-us/articles/5758928813332-North-America-Broadcast-Specifications-and-Requirements
10. https://cdn-2.4sales.com/staging/2025-11/dpp012-production-and-post-production-commercial-guidance-v2.0%5B43%5D.pdf (plus https://help.dsp.samsungads.com/docs/video and the blocked NBCU scrollhelp URL above)
