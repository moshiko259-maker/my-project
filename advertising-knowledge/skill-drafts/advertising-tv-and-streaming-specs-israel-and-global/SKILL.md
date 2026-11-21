---
name: "advertising-tv-and-streaming-specs-israel-and-global"
description: "Delivery specs for TV and streaming / connected-TV commercials: Netflix, Prime Video, Disney+ / Hulu, Roku, Paramount, Samsung, UK broadcast (Clearcast, DPP, clock numbers and slate), US broadcast (XR, Comcast), the IAB connected-TV guideline, and what is known for Israel - lengths, container and codec, resolution, frame rate, bitrate, loudness and true peak, safe areas, slates, with the official link per platform. Use when a film must be exported or checked for TV or a streaming platform. Not for social or YouTube ads, and not for Israeli approval rules. Hebrew triggers: מפרט טלוויזיה, פרסומת לטלוויזיה, נטפליקס פרסומות, סטרימינג, עוצמת קול לשידור, קובץ לשידור."
---

# TV and streaming ad specs - Israel and global

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
Owns: file and delivery specs for linear TV and streaming / connected TV. YouTube (incl. YouTube on TV), Meta, TikTok -> `advertising-social-media-specs-and-formats`. Israeli approvals, ethics, subtitles law -> `advertising-israel-broadcast-approvals-and-ad-law-basics`. Mix and loudness method -> `voice-audio-music`, `audio-software-windows-resolve-fairlight-audacity-and-daws`. Export steps -> `ai-video-post-production`.

## 1. Israel - what is and is not known
- Loudness rule of the Second Authority (regulator PDF): Dialnorm not above minus 26 dB and not below minus 30 dB, average minus 28 dB. Not the European R128 number.
- A commercial is at most 90 seconds; subtitles in a commercial: contrasting colour, letters at least 16 pixels high, at least 5 consecutive seconds (regulator PDFs).
- File format, codec, frame rate, slate and who delivers the file for Keshet, Reshet, Kan, Channel 14: UNKNOWN - no public spec page was found. Ask the channel's traffic / ad-operations desk before export. Do not assume the UK spec below applies.

## 2. Streaming / connected TV
| Platform | Lengths | Video | Audio and loudness | Limits | Source |
|---|---|---|---|---|---|
| Netflix | pre-roll :10 :15 :20 :30; mid-roll also :45 :60 :75; live :15 :30 | MP4 or MOV; ProRes 422 recommended, H.264 accepted; 1920x1080 recommended (1280x720, 3840x2160 accepted); 16:9; progressive; SDR only; H.264 at least 12 Mbps at 1080p recommended | PCM recommended, AAC-LC min 192 kbps; stereo; 48 kHz; -24 LKFS +/-2; true peak not above -2 dBFS | 1 GB or less recommended; letterbox never over 37% of the picture; no advertiser QR; allow 72 hours, restricted categories up to five days | advertising.netflix.com/en-us/creative-specs |
| Amazon Prime Video / Streaming TV | US, CA: 15, 30, 45, 60. UK, DE, AT, FR, IT, ES, BR, IN: 10, 15, 20, 30, 40, 60. JP: 15, 30 | 16:9, min 1920x1080; H.264 / MPEG-2 / MPEG-4; 23.976 recommended, 24, 25, 29.97; Prime Video min 15 Mbps, recommended 50 Mbps | AAC, min 192 kbps, 44.1 or 48 kHz, min 2 channels; no loudness figure on the page | max 500 MB; no click-style buttons; inline VAST 2.0 / 3.0 only | advertising.amazon.com/resources/ad-specs/dsp/video/streaming-tv-prime-video-ads |
| Disney+ / Hulu | not on the page read (search snippet: :15 or :30 - UNVERIFIED) | 1920x1080 preferred, 1280x720 accepted; 16:9 only; no letterbox or pillarbox; CBR 10-40 Mbps; ProRes 422 HQ or H.264; .mov .mp4 .m4v; 23.98-30 fps | required; 2 channels; min 128 kbps; AAC or PCM; loudness not on the page (snippet: -24 LKFS +/-2 - UNVERIFIED) | 1.9 GB (partner-served) / 250 MB (Hulu-served); no slates or countdowns; up to 5 business days | products.disneyadvertising.com/video-commercial/ |
| Roku Ads Manager | 6-92 seconds (general Roku guidelines: :15 or :30, :60 by exception) | .mov or .mp4; 16:9; 23.98 / 25.00 / 29.97; AVC or ProRes 422 HQ; min 6 Mbps | PCM preferred, AAC accepted, min 96 kbps, stereo, 48 kHz | max 1 GB; review 2-3 business days | help.ads.roku.com/en/articles/7154647-creative-guidelines |
| Paramount Ads Manager | :15 or :30 | min 1280x720, 16:9; mp4 H.264 preferred or ProRes 422 / HQ; progressive; min 6 Mbps; 23.98-30 fps | AAC stereo, min 192 kbps, 48 kHz; -24 LUFS +/-2 (ATSC A/85); peak never above -6 dB | max 10 GB; no slates, no black bars | adsmanager.paramount.com/resources/tech-specs |
| Samsung Ads (DSP) | 5-90 seconds, 15-30 recommended | MP4 H.264; 16:9; 1920x1080 recommended, min 1280x720; 5-10 Mbps; 30 fps recommended | AAC or MP3 | max 50 MB, 30 MB recommended | help.dsp.samsungads.com/docs/video |
| Peacock (as republished by an ad-buying partner, single source, updated 2 Nov 2026) | 15 or 30 seconds | .mov or .mp4; 16:9; 1920x1080 preferred; ProRes 422 HQ or H.264; 15-30 Mbps at 1080p; 23.98-30 fps progressive | 2-channel, 48 kHz, min 192 kbps; -24 LKFS +/-2 | 10 GB | help.vibe.co article 9735845 (PARTNER, not NBCU's own page) |
| Max / HBO Max | no advertiser spec found | | | | UNKNOWN |

IAB Tech Lab guideline for digital video and connected TV (PDF "Released August 2022"): typical lengths 6, 15, 30 seconds (bumpers 3-10, also 60); mezzanine 1920x1080 or 1280x720, 16:9, progressive, no slate, no burned-in boxing; audio -24 LKFS (+/-2) in the US, -23 LUFS (+/-1) in the EU, peaks not above -6 dB true peak. Source: iabtechlab.com/wp-content/uploads/2022/03/Ad-Format-Guidelines_DV-CTV.pdf

## 3. UK broadcast (model of a strict broadcast spec)
| Item | Value | Source |
|---|---|---|
| Clearance | all UK TV ads are cleared by Clearcast | Cape UK overview (VENDOR) |
| Clock number | AAA/BBBB123/456 = 3-letter agency code / four letters + three numbers / duration in three digits (030 = 30 s); a changed file needs a new clock number | help.clearcast.co.uk/en/article/how-do-i-create-a-clock-number-and-slate |
| Slate | clock 09:59:50:00 to 09:59:56:24 (7 s), black 09:59:57:00 to 09:59:59:24 (3 s), ad starts 10:00:00:00; 6 frames of audio silence at start and end | same + Clearcast Library spec v1.6 |
| File | 1920x1080, 25 fps, 16:9; XDCAM 50 (MXF OP-1a, 50 Mbit/s) or ProRes 422 HQ; PCM 48 kHz 24 bit, stereo on channels 1 and 2 | Clearcast Library spec v1.6 (2024) |
| Loudness | EBU R128: -23.0 LUFS +/-0.2 LU; true peak aim -3 dBTP, fails above -1 dBTP; max short-term -18.0 LUFS (R128 s1 for commercials) | DPP012 v2.0 (17-05-2025); EBU R128 s1 |
| Safe area | 80% of width and 90% of height | DPP012 |
| Legal text | min height 30 TV lines in HD (26 on an opaque single-colour block); hold 0.2 s per word + 2 s (up to 9 words) or 3 s (10 or more) | Clearcast / BCAP |
| Lead times (delivery house Cape, formerly Peach) | linear 2 working days; BVOD 5; Sky Adsmart 7 on one page and 5 on another | cape.io (VENDOR) |

## 4. US and Canada broadcast
| Item | Value | Source |
|---|---|---|
| XR (Extreme Reach) layout | 5-second slate, 2 seconds black, then the ad; slate shows Ad-ID, advertiser, title, duration | helpcenter.xr.global article 5758928813332 (VENDOR) |
| XR file | XDCAM HD 422 50 Mbps or ProRes 422 HQ; 1920x1080; 23.98 progressive preferred | same |
| XR audio | -24 LKFS; true peak below -2 dB TP (recommended below -6) | same |
| Title safe | 90% of width and height (up to 93% tolerated) | same |
| Captions | mandatory for all commercials in Canada; optional service in the US | same |
| Clearance | US: each network's own standards department; Canada: mandatory | same |
| Comcast AdDelivery Lite | no slate; exact lengths 15 / 30 / 60 / 90 / 120 seconds; 1920x1080 29.97 or 23.976 | Comcast PDF "2022" (VENDOR) |
Standards: ATSC A/85 current version A/85:2026-07 (approved 8 July 2026); ITU-R BS.1770 is the loudness measurement method.

## 5. One master, many exports (INFERENCE from the tables)
1. Finish one high-quality master: 1920x1080, progressive, ProRes 422 HQ, 48 kHz stereo PCM, no slate, no burned-in bars.
2. Frame rate follows the destination: 25 for the UK and Europe, 23.976 or 29.97 for the US; never convert late - decide before generating.
3. Make a separate export per destination with its own loudness: -23 LUFS (EU broadcast), -24 LKFS (US and most streaming), Israel per the regulator's Dialnorm rule and the channel's instruction.
4. Add the slate only where the destination asks for one (UK, XR); streaming platforms forbid it.
5. Keep text inside 80% width / 90% height and away from the top-right corner on Netflix.

## General rule - recommend then teach
For any creative request first run `creative-request-advisor-tools-models-prices-then-teach-steps`: show the tool and model options (cheapest, most expensive, best quality, best value, free alternative) with live prices, commercial rights and one pick; wait for Moshe's choice; then guide him with the exact tool, settings and numbered steps from this skill.

## Open questions - verify before use
1. Israeli channels' technical specs.
2. Disney+ / Hulu duration and loudness on the official page; NBCU / Peacock and Max specs.
3. HDR for linear broadcast, France, Germany, Australia: not researched.

## Lessons learned
- 21 Nov 2026: loudness and true-peak limits differ by destination; one "broadcast mix" does not fit all.
