<!-- RAW sub-agent report, UNVERIFIED. Saved by the main agent on 20 Nov 2026. Do not copy into a skill before the verifier pass. -->

# R4b report: non-generation tools for ad production (read 20–21 Nov 2026)

Coverage is partial: about 45 of roughly 80 tools were read on live official pages. The rest are listed in section 3 as UNKNOWN; nothing below is from memory. The session's WebFetch could not resolve external hosts, so pages were read with headless Playwright Chromium (no login, no forms, no files written). Tags: V = VENDOR, O = OFFICIAL, C = COMMUNITY. Prices are as shown; several pages carried Black Friday banners, so sale prices are marked.

## 1. Findings

### 1.1 Voice / TTS / cloning
| Tool | Plans and prices as shown | Commercial right / notes | Hebrew | Tag, URL |
|---|---|---|---|---|
| ElevenLabs | Free $0, 10k credits/mo. Starter "$6 / $5 /mo, 2 months free" (monthly / yearly toggle), 30k. Creator $22, yearly $18.33/mo; Black Friday "$8.25/mo first year, until Dec 1", 121k. Pro $99, yearly $82.50; BF $37.13, 600k. Scale $299 / $249.17, 3 seats. Business $990 / $825. "Prices exclude all taxes" | Starter lists "Commercial License", "Instant Voice Cloning", "Music commercial use". "Professional Voice Cloning" from Creator. Free has no commercial licence listed | "Hebrew (he)" in model language lists; table shows 74 languages | V, https://elevenlabs.io/pricing ; O, https://elevenlabs.io/docs/overview/models |
| ElevenLabs consent | Use policy: "If you believe your voice has been used without your consent, you can submit an Unauthorized Use of Voice report". Terms: "we will not commercialize your voice on a standalone basis without your permission" | Exact clone-consent clause not captured | | O, https://elevenlabs.io/use-policy ; https://elevenlabs.io/terms-of-use |
| Cartesia | Free $0, 20K credits/mo. Pro $5/mo, 100K. Startup $49/mo, 1.25M. Scale $299/mo, 8M. Enterprise custom | Pro: "Commercial use license", "Instant voice cloning". Startup: "Pro voice cloning". Terms: user warrants having "all rights, licenses, consents, permissions" for content | "Hebrew (he)" listed for Sonic 3.6 | V, https://www.cartesia.ai/pricing ; O, https://docs.cartesia.ai/build-with-cartesia/tts-models/latest |
| Murf (Studio tab) | Free "$0 / month", 10 min voice generation, "No Downloads", "No Commercial Rights". Creator "$19 / month, $228 Billed Annually", 24 hrs/year. Business "$66 / month, $792 Billed Annually", 96 hrs/year. Enterprise custom | Creator: "Commercial Rights". Business: "Business License". API: $0.03 per 1000 characters (Gen2), $0.01 (Falcon 2.1) | UNKNOWN (languages page returned 404) | V, https://murf.ai/pricing |
| WellSaid | No public prices; "Get a demo" only | "Every WellSaid voice is cleared for commercial use, with a license record on each file"; "300 licensed voices across 55 languages and accents" | UNKNOWN | V, https://www.wellsaid.io/ai-voice-pricing |
| Resemble | Pricing page is now titled "Deepfake Detection & AI Security Pricing": Flex $0/mo, Team $280/mo, Business $800/mo (billed annually) | No TTS plan shown on the pricing page | UNKNOWN | V, https://www.resemble.ai/pricing |
| Hume | hume.ai/pricing redirects to a home page about an "Audio Decisions API"; the TTS docs URL redirects to Audio Decisions docs | No TTS pricing found. A blog says Hume TTS shut down | UNKNOWN | V, https://www.hume.ai/ ; C, https://www.stork.ai/blog/playht-alternatives-2026 (SNIPPET ONLY) |
| PlayHT | play.ht did not connect (tunnel failed) | Blogs report Meta acquisition and shutdown around 31 Dec 2025; exact date disputed | n/a | C, SNIPPET ONLY, https://www.stork.ai/blog/playht-alternatives-2026 ; https://murf.ai/blog/play-ai-transition-guide |
| Azure TTS | Free (F0): "Neural 0.5 million characters free per month". Standard voice Neural: "$15 per 1M characters". Custom professional voice synthesis "$24 per 1M characters" | Licence terms not read | he-IL-HilaNeural (Female), he-IL-AvriNeural (Male) | O, https://azure.microsoft.com/en-us/pricing/details/speech/ ; https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts |
| Google Cloud TTS | Per-character rates shown from "US$4 per 1 million characters" to "US$160 per 1 million characters"; which voice type maps to which rate was not captured | | "Hebrew (Israel) Premium he-IL-Chirp3-HD-…" voices, male and female | O, https://cloud.google.com/text-to-speech/pricing ; https://docs.cloud.google.com/text-to-speech/docs/list-voices-and-types |
| OpenAI TTS | Price not captured | "Create an approved custom voice from a speaker's consent recording and matching audio sample" | Hebrew in the supported-language list | O, https://developers.openai.com/api/docs/guides/text-to-speech |

### 1.2 Music / SFX generation
| Tool | Plans and prices as shown | Commercial right | Tag, URL |
|---|---|---|---|
| Suno | Plans: Free, Pro, Premier, Platinum. Prices did not render. Search snippets conflict (see section 2) | "Commercial rights: Not included (Free) / Included / Included / Included". Paid: "you are considered the owner of the song. You also retain the rights to commercial use… even if you end your subscription". Free: "we retain ownership… non-commercial purposes". "See the terms of service for limitations on commercial use" | V, https://suno.com/pricing ; O, https://help.suno.com/en/articles/2416769 ; https://help.suno.com/en/articles/14617153 ("Edited 3 days ago") |
| ElevenLabs Music | Same plans as 1.1 (monthly: Starter $6, Creator $22, Pro $99) | Table row reads "Personal use only" / "Commercial, no streaming" / "Commercial, not enterprise" / "Commercial, not enterprise"; mapping to Free / Starter / Creator / Pro is INFERENCE from column order | V, https://elevenlabs.io/music |
| Stable Audio | Free $0/mo, 50 credits. Solo $12/mo, 660 credits. Session $30/mo, 1,800 credits. Producer $90/mo | "Commercial license" listed on every tier including Free. "If your company makes over $1M a year, contact our team about licensing" | V, https://stableaudio.com/pricing |
| AIVA | Free €0, 3 downloads/mo. Standard "€11 / month + VAT, Billed Annually", 15 downloads. Pro "€33 / month + VAT, Billed Annually", 300 downloads | Free: "Copyright owned by AIVA, No monetization, Credit must be given". Standard: "monetize compositions only on Youtube, Twitch, Tik Tok and Instagram". Pro: "Copyright owned by YOU, Full monetization" | V, https://www.aiva.ai/ |
| Soundraw | Four paid tiers: "$16.99/mo, $11.04/mo"; "$29.99/mo, $19.49/mo"; "$35.99/mo, $23.39/mo"; "$50/mo, $32.50/mo" (monthly, yearly). Plan names not captured | Rows "Commercial use: use as background music" and "Distribute & monetize songs" exist; per-tier values not captured | V, https://soundraw.io/pricing |
| Mubert Render | Free (25 tracks/mo, 5 MP3 downloads). Then $14, $39, $89 per month; Black Friday first-year $8.17, $22.75, $43.75 ("Billed $98 / $273 / $525 for the first year") | Free and the $14 tier are labelled "Non-commercial". $39: "Commercial Usage". $89: "Clients, apps & games". "Tracks cannot be sold or commercially distributed" | V, https://mubert.com/render/pricing |
| Udio, Beatoven, Adobe Firefly soundtrack | Not readable | UNKNOWN | see section 3 |

### 1.3 Stock music
| Tool | Plans and prices as shown | Client work / ads / TV | Tag, URL |
|---|---|---|---|
| Epidemic Sound | Creator $9.99 "Per month, billed $119.88 yearly". Pro $16.99, "billed $203.88 yearly". Pro Plus $39.99, "billed $479.88 yearly". 30 days free offered | Creator: "Licensing for social, podcasts and websites". Pro: "commercial use online", "Licensing for digital ads", "Licensing for client work". TV/broadcast clause not found on the page | V, https://www.epidemicsound.com/pricing/ |
| Artlist | AI plans: $19.99/month (16,500 credits), $39.99 (40,000), $99.99 (120,000); each "License covers commercial use". Stock music price page rendered empty | Licence page: "Client work", "Paid & promoted videos", "broadcasting of your Project is permitted under the Pro / Business License. If you are a broadcaster please see section 11" | V, https://artlist.io/page/pricing/max ; O, https://artlist.io/help-center/privacy-terms/artlist-license/ |
| Musicbed | No prices shown ("View Pricing", "Request Quote") | Individual: web, podcast, social up to 1M followers. Business: adds "Client and brand work", "Clients up to 250 employees". Enterprise: "Clients of Any Size", "Broadcast", "Cinema / Film Festival", "VOD / OTT / CTV" | V, https://www.musicbed.com/pricing |
| Soundstripe, PremiumBeat, Uppbeat, Pixabay | Blocked | UNKNOWN | see section 3 |

### 1.4 3D
| Tool | Plans and prices as shown | Tag, URL |
|---|---|---|
| Tripo | Free $0. Pro "$20.00 / Month, billed annually as: $240.00 / year", 3000 monthly credits. Max "$90.00 / Month, billed annually as: $1080.00 / year", 25000 credits. Team "$110.00 → $55.00 / Mo / seat" (50% off) | V, https://www.tripo3d.ai/pricing |
| Rodin (Hyper3D) | Free $0 ("Direct credits cost $1.5 per credit"). Creator "$24 / mo, Billed yearly - $288 today", about 60 models. Business "$96 / mo, Billed yearly - $1,152 today", API access | V, https://hyper3d.ai/pricing |
| Spline | Hobby "$6 (struck $12) per seat / month, annually, $72 the first year, then $144/yr". Pro "$12.50 (struck $25)… $150 the first year, then $300/yr" | V, https://spline.design/pricing |
| Fab (Epic) | Fab Standard License summary: "Use the assets commercially or privately", "Commercially distribute your Projects with the Fab assets incorporated". Not allowed: "Resell or redistribute the asset… on a standalone basis" | O, https://www.fab.com/eula |
| Meshy, Unreal Engine licence, Blender licence, Maxon, Adobe Substance, Mixamo, Luma Genie, Sketchfab | Not readable or not opened | see section 3 |

### 1.5 Editing / finishing
| Tool | Plans and prices as shown | Tag, URL |
|---|---|---|
| DaVinci Resolve | Free version: "Free Download Now". Studio: "Was $295 Now $236" | V, https://www.blackmagicdesign.com/products/davinciresolve |
| Final Cut Pro | "new subscribers pay $12.99 per month or $129 per year"; "also available as a one-time purchase for $299.99"; free for 30 days | V, https://www.apple.com/final-cut-pro/ |
| CapCut | Free "USD 0". Pro "USD 19.99 /month", 1200 monthly AI credits. Ultra "USD 79 /month". Teams tier exists. Page says final price shows at sign-in | V, https://www.capcut.com/pricing |
| CapCut terms | "terms governing whether Company Content can be used for commercial or non-commercial purposes may vary depending on the CapCut product you are using"; "For Pippit, you are expressly permitted to use Company Content for commercial purposes, subject to… the CapCut Materials License" | O, https://www.capcut.com/clause/terms-of-service |
| Descript | Free $0. Hobbyist "$16 / $24 per person / month". Creator "$24 / $35". Business "$50 / $65" (annual / monthly; "Saving up to 35% over monthly plan") | V, https://www.descript.com/pricing |
| Topaz | Topaz Video "$299/yr → $254/yr" (sale). Topaz Studio "$499 → $299/yr". Studio Pro "$799 → $499/yr". "Pro licenses add full commercial use for organizations over $1M USD in annual revenue" | V, https://www.topazlabs.com/pricing |
| Frame.io | Free $0. Pro "$15 per member per month + tax". Team $25. Enterprise custom. Annual "SAVE 13%" | V, https://frame.io/pricing |
| Premiere / Creative Cloud | Blocked | see section 3 |

### 1.6 Motion graphics / design
| Tool | Plans and prices as shown | Tag, URL |
|---|---|---|
| Canva | Two paid prices shown: "US$18 → US$9, 50% off, /month for one person" and "US$25 → US$12.50, 50% off, /month per person". Plan names not captured (INFERENCE: Pro and Business) | V, https://www.canva.com/pricing/ |
| Canva content licence | Permitted for Free or Pro Content in designs: "advertising and promotional projects, including… film and video presentations, commercials"; "video, broadcast and theatrical presentations of unlimited prints". No rights granted for "names, people, trademarks, trade dress, logos" | O, https://www.canva.com/policies/content-license-agreement/ |
| Affinity | "$0, free"; "One powerful app. No cost."; download needs a Canva account; AI tools need a Canva premium plan | V, https://www.affinity.studio/get-affinity |
| Figma | Professional: Full seat $16/mo, Dev $12, Collab $3. Organization (billed annually): Full $55, Dev $25, Collab $5. Enterprise: Full $90 | V, https://www.figma.com/pricing/ |
| Jitter | Free (720p 30fps, 3 files). Pro "$15 per editor / month billed annually". Max $35. Ultra $59 | V, https://jitter.video/pricing/ |
| Rive | Free $0. Cadet $9 /seat/mo. Voyager $32. Enterprise ($10M+ annual revenue) $120 | V, https://rive.app/pricing |
| Cavalry | "Professional, real-time animation software. For free." Paid tier page returned 404 | V, https://cavalry.studio/en/ |
| LottieFiles | Individual "$19.99 Per user / month, Billed annually". Team $24.99 | V, https://lottiefiles.com/pricing |
| Remotion | "Remotion for Creators… $25/mo" per seat. "Remotion for Automators… $0.01 per render, $100/mo minimum". Enterprise "Starting at $500 per month". A free-licence eligibility page exists; its criteria were not captured | O, https://www.remotion.dev/docs/license/pricing |
| HyperFrames (HeyGen) | "Free and open source." | V, https://hyperframes.heygen.com/ |
| After Effects, Adobe Express | Blocked | see section 3 |

### 1.7 Storyboard / previz
| Tool | Plans and prices as shown | Tag, URL |
|---|---|---|
| Storyboarder | "Download for Free… free and open source"; version 1.0.0 | V, https://wonderunit.com/storyboarder/ |
| Boords | Solo $39/month (250 AI images). Pro $75. Team $125. Agency $250 (monthly billing; yearly "Save 33%") | V, https://boords.com/pricing |
| Katalist | Essential $19.00. Pro $39.00/month. Unlimited $99.00/month. 7-day free trial offered | V, https://www.katalist.ai/katalist-pricing |
| LTX Studio | Free $0, 800 credits one time, "Personal use license". Lite "$15 / $12 /month, Billed yearly $144". Standard "$35 / $28, Billed yearly $336", "Commercial use license". Pro "$125 / $100, Billed yearly $1,200" | V, https://ltx.io/studio/pricing |
| Storyboard Hero | Solo $19/month. Starter $59/month (5 seats). Advanced $199/month (10 seats). "Commercial use" listed | V, https://storyboardhero.ai/pricing |

### 1.8 Script / concept / research
| Tool | Plans and prices as shown | Tag, URL |
|---|---|---|
| Claude | Free $0. Pro "$17 per month with annual subscription discount ($200 billed up front). $20 if billed monthly". Max $100 per month. Ultra $200 per month | V, https://claude.com/pricing |
| ChatGPT | Plans Free, Go, Plus, Pro shown; prices did not render | V, https://chatgpt.com/pricing/ |
| Gemini | $0. Google AI Plus $4.99/month. $19.99/month tier (INFERENCE: AI Pro). Top tier "Starting at $99.99/month", $199.99 also shown | V, https://gemini.google/subscriptions/ |
| Final Draft 13 | "USD $249.99 → USD $199.99". Suite annual "USD $99.99 → USD $69.99 /year" (Black Friday). Monthly "USD $16.99 /month" | V, https://www.finaldraft.com/products/final-draft-13 |
| WriterDuet | Free $0 (three projects). Plus $9.99/mo. Pro $11.99/mo | V, https://www.writerduet.com/pricing |
| Arc Studio | Free $0. Essentials $69/year. Pro $99/year | V, https://www.arcstudiopro.com/pricing |
| Celtx | Plans Writer, Writer Pro, Team; prices not captured | V, https://www.celtx.com/pricing |

### 1.9 Stock footage
| Tool | Plans and prices as shown | Tag, URL |
|---|---|---|
| Storyblocks | Essentials "was $21, $16.80 /month billed annually", Individual license. Unlimited All Access "was $30" (sale price not captured). Small Business "was $40, $32 /month billed annually" for "under 50 employees, excluding agencies, production, and broadcast companies". Business: quote | V, https://www.storyblocks.com/pricing |

## 2. Conflicts
- Suno prices: search snippets give Pro $8 and Premier $24 per month (suno.com page capture cited by https://www.withorb.com/pricing-atlas/suno) versus $10 and $30 monthly with 20% off yearly (https://www.layer3labs.io/guides/suno-pricing). Both COMMUNITY, SNIPPET ONLY. The live page showed no prices to the headless browser.
- ElevenLabs: /pricing shows Black Friday first-year prices (Creator $8.25/mo); /music shows "Starter $6 per month, first month $1; Creator $22 per month, first month $11".
- Hume and Resemble are still on the tool list as TTS vendors, but both official sites now lead with other products (audio decisions; deepfake detection).

## 3. Could not open / UNKNOWN
- Blocked by bot protection (HTTP 403 / 429 / challenge): all adobe.com and helpx.adobe.com pages (Premiere, After Effects, Creative Cloud, Substance, Express, Firefly soundtrack, Adobe Stock), meshy.ai, unrealengine.com/license, blender.org/about/license, pexels.com/license, unsplash.com/license, pixabay.com licence, premiumbeat.com/license, shutterstock.com/pricing, uppbeat.io/pricing.
- Rendered empty or errored: udio.com, soundstripe.com/pricing, artlist stock-music price page, beatoven.ai/pricing (404), milanote.com/pricing (404), studiobinder.com/pricing (redirects to login), maxon.net/en/buy (no prices), frameforge.com (plain-HTTP redirect refused by proxy), play.ht.
- Not attempted (ran out of budget): Getty, Mixamo, Sketchfab, Luma Genie, Meta Ad Library, TikTok Creative Center, Google Ads Transparency Center, captioning tools and Hebrew subtitle support, shot-list tools, OpenAI TTS price, exact voice-clone consent clauses, Unreal linear-content terms, AI-content rules of stock libraries, Remotion free-licence criteria, CapCut Materials License text.
- TV/broadcast right confirmed only for: Artlist Pro/Business, Musicbed Enterprise, Canva content licence. For every other tool it is UNKNOWN.

## 4. Summary tables (only from the findings above)
| Category | Free option | Cheapest paid seen | Most expensive seen | INFERENCE: best-value candidate |
|---|---|---|---|---|
| Voice | ElevenLabs Free, Cartesia Free, Azure F0 (0.5M chars/mo) | Cartesia Pro $5/mo; ElevenLabs Starter $5–6/mo | ElevenLabs Business $990/mo | ElevenLabs Starter or Cartesia Pro: lowest tiers that list a commercial licence, both list Hebrew |
| AI music | Stable Audio Free (lists commercial licence), AIVA Free, Mubert Free (non-commercial) | Soundraw $11.04/mo yearly; Stable Audio Solo $12/mo | Stable Audio Producer $90/mo | Stable Audio Solo: commercial licence stated at $12. Suno not comparable because the price is unconfirmed |
| Stock music | none confirmed | Epidemic Creator $9.99/mo (no client work) | Epidemic Pro Plus $39.99/mo; Musicbed Enterprise by quote | Epidemic Pro $16.99/mo for online client ads; Artlist Pro where broadcast is needed (price unconfirmed) |
| 3D | Tripo Free, Rodin Free | Spline Hobby $6/seat/mo (first year) | Tripo Team $110/seat/mo list | Tripo Pro $20/mo, about 200 models |
| Editing | DaVinci Resolve free, CapCut Free, Descript Free, Frame.io Free | Final Cut Pro $12.99/mo | CapCut Ultra $79/mo; Topaz Studio Pro $499/yr | DaVinci Resolve free, or Studio at $236 one-off |
| Motion / design | Affinity, Cavalry, HyperFrames, Jitter Free, Rive Free | Rive Cadet $9/seat/mo; Canva US$9 (sale) | Rive Enterprise $120/seat/mo | Affinity (free) plus Canva's lower paid tier, whose content licence names commercials and broadcast |
| Storyboard | Storyboarder, LTX Free (personal use) | LTX Lite $12/mo yearly | Boords Agency $250/mo | Storyboarder (free); LTX Standard $28/mo is the lowest tier with a commercial-use licence |
| Script / LLM | Claude Free, Gemini $0, WriterDuet Free, Arc Free | Gemini AI Plus $4.99/mo | Claude Ultra $200/mo; Gemini top tier $199.99 | Arc Studio Free for script format plus one $17–20 LLM plan |
| Stock footage | UNKNOWN (Pexels / Unsplash / Pixabay blocked) | Storyblocks Essentials $16.80/mo | Storyblocks Business by quote | not enough data |

## 5. Top 10 URLs for the verifier
1. https://elevenlabs.io/pricing
2. https://www.cartesia.ai/pricing
3. https://suno.com/pricing (prices need a normal browser)
4. https://www.epidemicsound.com/pricing/
5. https://artlist.io/help-center/privacy-terms/artlist-license/
6. https://www.canva.com/policies/content-license-agreement/
7. https://www.capcut.com/clause/terms-of-service
8. https://www.remotion.dev/docs/license/pricing
9. https://stableaudio.com/pricing
10. https://www.blackmagicdesign.com/products/davinciresolve
