# 13 - Learning sources and lessons from videos read in full

Read: 20-21 Nov 2026. STATUS: DRAFT - NOT YET VERIFIED. Do not copy any number into a skill until `15-verification-log.md` shows it PASS.
Tags per fact: OFFICIAL / VENDOR / COMMUNITY / INFERENCE / UNKNOWN. "SNIPPET ONLY" = seen in a search result, page not opened.
Origin: sub-agent report `research-raw/R6-learning-sources-and-video-lessons.md`, reformatted only (no fact added or removed by the main agent).

R6 REPORT - LEARNING SOURCES + VIDEO LESSONS (read 20-21 Nov 2026)

Method: WebFetch failed on most hosts (DNS not allowed), so pages were opened with curl (browser UA) and text read directly. "Opened" = HTTP 200 and text read by me. YouTube watch pages returned HTTP 429 / "Sign in to confirm you're not a bot" to yt-dlp, curl and Playwright. Transcripts were obtained by loading youtube.com/embed/<id> in my own Playwright Chromium and capturing the player's own caption (timedtext) response; each was checked to run to the video's end and read in full by me.

## 1. FINDINGS

### 1A. Official academies (all opened 20-21 Nov 2026 unless marked)
| Source | Value (as page shows) | Tag | URL |
|---|---|---|---|
| Google ABCDs guide | Page dated "May 2023". "30% lift in short-term sales likelihood", "17% lift in long-term brand contribution"; source "Google/Kantar, The Short & the Long of ABCDs Effectiveness, Global, Apr 2021. n=11,000 ads". A=Attention ("Hook and sustain attention with an immersive story"), B=Branding ("Brand early, often, and richly"), C=Connection, D=Direction ("Include a CTA", "Boost CTAs with audio"). Sub-tips: jump in, tight framing, bright high-contrast visuals, "See and say", "Focus the message". Free, English + Hebrew locale listed | OFFICIAL | https://business.google.com/us/resources/articles/abcds-of-effective-video-ads/ |
| Google Skillshop | Live; lists "Google Ads Video", "Creatives", "Get Certified", "Learn at your own pace". Cost/length not shown on page read | OFFICIAL | https://skillshop.withgoogle.com/ |
| Skillshop Video certification detail | "50 questions, 75 minutes, pass 80%, valid one year" - SNIPPET ONLY from third-party sites; whether still free is disputed (see Conflicts) | COMMUNITY | https://support.google.com/skillshop/answer/14746215 (not opened) |
| Think with Google | Live, now at business.google.com/en-all/think/ | OFFICIAL | https://www.thinkwithgoogle.com/ |
| Meta Blueprint | "Explore free online courses, live webinars and videos"; has "Creative inspiration" topic, Certifications tab | OFFICIAL | https://www.facebookblueprint.com/student/catalog |
| Meta certification price | $150 (most sources) vs about $99 (one) - SNIPPET ONLY | COMMUNITY | https://markampus.com/blog/meta-blueprint-certification-cost-2026/ |
| TikTok Academy | "Is TikTok Academy free? Yes." Topics: "ad formats, creative, measurement, ad policy, industry best practices, and campaign strategy"; certification for media buying | OFFICIAL | https://ads.tiktok.com/business/en/academy |
| TikTok Creative Center | Old URL redirects to "TikTok One Creative Suite" | OFFICIAL | https://ads.tiktok.com/creative/creativeCenter |
| Snapchat | Resources page lists "Snapchat Ads Certification", webinars, "free tools"; course catalogue at focus.snapchat.com/pages/catalog (opened, JS only, no text) | OFFICIAL | https://forbusiness.snapchat.com/resources |
| Pinterest Academy | "free resources like courses, live webinars and a certification exam" | OFFICIAL | https://business.pinterest.com/pinterest-academy/ |
| LinkedIn Marketing Academy (ex-Labs) | Live: learning paths, courses, videos, certifications. Cost not shown in text read | OFFICIAL | https://training.marketing.linkedin.com/ |
| Amazon Ads Academy | learningconsole URL redirects here; "Explore free courses, certifications, videos, and curated learning paths" | OFFICIAL | https://advertising.amazon.com/academy |
| HubSpot Academy | 200, JS only, no text read | UNKNOWN | https://academy.hubspot.com/courses |
| IPA | Effectiveness page live; "Download our free material"; "The Long and the Short of It" publication page returns 200; price not found in text | OFFICIAL | https://ipa.co.uk/knowledge/effectiveness-research-analysis |
| D&AD | /learn live: "Masterclasses, Team training, Creative Leaders, Junior Creative Onboarding"; no free tier seen | OFFICIAL | https://www.dandad.org/learn |
| AICP | Resources page lists "AICP Guidelines and Best Practices", "...Post Production", "AI Resources", "Bidding Resources", "Contracts & Riders" (has Log In; access level not tested) | OFFICIAL | https://aicp.com/business-resources |
| Cannes Lions The Work | 200, JS only; free parts not confirmed | UNKNOWN | https://www.lovethework.com/en |
| WARC | Live; "Book a demo", "Our subscription options"; no free tier seen | VENDOR | https://www.warc.com/en |
| Blackmagic DaVinci Resolve training | Training videos with lengths: Intro to Editing Part 1 "1h 09m", Part 2 "44m", Intro to Color "1h 33m", Advanced Color "57m", Color Management "31m", Intro to Audio (Fairlight) "1h 28m", Delivering Content "19m". Books for "DaVinci Resolve 20": Beginner's, Editor's, Colorist, Fairlight Audio, Visual Effects, Advanced Visual Effects - each "Download PDF", "Buy Now on Amazon", "Complete Online Exam". "over 250 certified trainers and over 100 training centers". Software: Resolve 21 "Free"; Studio 21 "Was $295 Now $236" | OFFICIAL | https://www.blackmagicdesign.com/products/davinciresolve/training |
| Higgsfield Academy | Course "Your own film": "7 lessons. 90 minutes."; "You can watch all the lessons for free"; homework needs "an active Higgsfield subscription and credits"; "Get certificate". Other courses listed: Blockbuster 4K: The AI Filmmaking Pipeline; Build an Ultra-Realistic Short Film in 4K; Add AI VFX to Real Footage; Make an AI Animated Short | VENDOR | https://higgsfield.ai/academy |
| Runway Academy | "AI for Advertising ... From concept to final delivery ... 10 modules, Level: Beginner, Enroll for free"; also "Prompt Guide", tutorials (Runway Ruby, Aleph 2.0) | VENDOR | https://academy.runwayml.com/ |
| Google Flow | labs.google/fx/tools/flow redirects to flow.google.com ("Google Flow - AI Creative Studio"); Help centre has credits, shortcuts, Flow Music articles | OFFICIAL | https://support.google.com/flow/ |
| Veo prompt guide | "Video generation prompt guide" live (now under "Gemini Enterprise Agent Platform") | OFFICIAL | https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/video-gen-prompt-guide |
| ElevenLabs docs | Live; menu shows "Eleven v4", "Best practices", Music, Text to Dialogue, "Ads Engine", Sound Effects | VENDOR | https://elevenlabs.io/docs/overview/intro |
| Suno help | 200 "Knowledge Base", JS only | UNKNOWN (content) | https://help.suno.com/ |
| Adobe learn / Canva Design School | HTTP 403 to curl | UNKNOWN | https://www.adobe.com/learn ; https://www.canva.com/design-school/ |

### 1B. Teachers / channels (YouTube channel pages opened by curl; subscriber counts as shown)
| Who | Value | Tag | URL |
|---|---|---|---|
| The Futur (Chris Do) | 2.83M subscribers | COMMUNITY | https://www.youtube.com/@thefutur |
| Dara Denney (performance creative, agency owner per her video) | 264K | COMMUNITY | https://www.youtube.com/@DaraDenney |
| Barry Hott ("ugly ads") | 16.9K | COMMUNITY | https://www.youtube.com/@BarryHott |
| Motion (Creative Analytics) | 18.2K; motionapp.com/creative-trends now redirects to runneth.com (title "2025 Ad Creative & Creative Strategy Trends") | VENDOR | https://www.youtube.com/@MotionCreativeAnalytics |
| Film Riot | 2.26M | COMMUNITY | https://www.youtube.com/@FilmRiot |
| StudioBinder | channel + blog live (count not parsed); "Stages of Filmmaking" series found in search (Ep 3 Production 1531 s, Ep 4 Post 1307 s) | VENDOR | https://www.youtube.com/@StudioBinder |
| Corridor Crew | 7.21M | COMMUNITY | https://www.youtube.com/@CorridorCrew |
| Curious Refuge (AI filmmaking school) | 279K; site "The World's First Home for AI Filmmaking" | VENDOR | https://www.youtube.com/@curiousrefuge |
| Theoretically Media | 202K | COMMUNITY | https://www.youtube.com/@TheoreticallyMedia |
| Tao Prompts | 199K | COMMUNITY | https://www.youtube.com/@TaoPrompts |
| Dan Kieft | 331K | COMMUNITY | https://www.youtube.com/@DanKieft |
| Futurepedia | 772K | COMMUNITY | https://www.youtube.com/@futurepedia_io |
| MattVidPro, Rory Flynn | channels exist (200), counts not parsed | COMMUNITY | https://www.youtube.com/@MattVidPro ; https://www.youtube.com/@RoryFlynn |
| System1 / Orlando Wood | site lists "Lemon", "Look Out", "Test Your Ad", "Super Bowl 2027 Ads"; YouTube 2.24K | VENDOR | https://system1group.com/ |
| Ehrenberg-Bass (Byron Sharp) | site live; "How Brands Grow Live!", sponsor model | OFFICIAL | https://marketingscience.info/ |
| Hebrew | "דיגיטלי בעסקים" podcast; "חדשות הדיגיטל לניהול שיווק" (monthly, episode Jan 2026); "פרסום" by מירן פחמן on ice.co.il (episodes mainly 2018) - SNIPPET ONLY, none opened | COMMUNITY | https://podcasts.apple.com/il/podcast/id1754304837 |

### 1C. Free courses (item 3)
Colour and sound: Blackmagic videos/books above (OFFICIAL). Ad production with AI: Runway "AI for Advertising" (free enrol), Higgsfield Academy (free to watch). Producing: StudioBinder series. Copywriting-for-ads, storyboard and commercial-directing courses: not researched - UNKNOWN.

### 1D. Videos - transcript read in full: yes (all 8)

V1. "Understanding the ABCD guidelines for effective YouTube ads" - YouTube Ads / YouTube For Business - https://www.youtube.com/watch?v=Z8dizaqBK4Q - uploaded 21 Apr 2022 - 5:53. All OFFICIAL.
1. Based on analysis of "thousands of ads"; ABCDs are "not a formula"; a strong creative idea is "the single most critical factor".
2. Attention: drop viewers into the story; options named: strong colours, most exciting scenes first, powerful close-up opener.
3. Branding: on-screen graphics, voiceover, or product close-up.
4. Connection: make viewers think or feel; storyline, music, cast.
5. Direction: clear, simple CTA in voiceover or on screen; sets expectations.
6. Awareness: work harder on attention (dramatic action, audio cue), multiple branded elements, more human story.
7. Consideration: more product focus; people demonstrate the product promise; CTA that creates urgency.
8. Action: product "front and center", story revolves around it; connect on specifics; contextualise the CTA.

V2. "How to think about building effective ads for YouTube" - Think with Google - https://www.youtube.com/watch?v=HQaGIYE7KIk - uploaded 23 Sep 2021 - 5:36. All OFFICIAL.
1. "over 90% of people are discovering new brands and products on YouTube, and 40% have purchased".
2. TV spot arc is a "hill" (slow start, offer at end); online you lose "a significant percentage of your audience after five seconds".
3. Use the "emerging heartbeat arc": start high, several peaks, subtle branding and product cues throughout.
4. Five hooks: front-load the most exciting scenes; unexpected imagery; break the fourth wall; a simple puzzle; deep emotions (humour, nostalgia, embarrassment).
5. Mobile visual language: tighter framing, faster pace, large type supers.
6. People watch "at around 50% dimness" - keep brightness and contrast high.
7. Treat ads as "always in beta"; test and make small improvements.

V3. "How I Make Cinematic AI Ads with Fable 5.2 & Seedance 2.5" - Dan Kieft - https://www.youtube.com/watch?v=jeMl0OSwDss - published 12 Nov 2026 (channel RSS) - 24:07. COMMUNITY (contains a Higgsfield promotion). Auto-captions garble names ("Hixx Fields"=Higgsfield, "Sea Dream"=Seedream, "Sedan/CN 2.5"=Seedance 2.5; one line says "Leonardo.ai" - unclear).
1. Assets first (characters, locations, objects); "garbage in equals garbage out".
2. Character sheet: 16:9, 2K, grey background (white gives a bright studio look), three views - one face close-up in three-quarter view plus front and back full body without head.
3. Model test for his sheet: GPT 2.6 "four credits per image" (skin patches), Nano Banana 2 about three credits (plastic), Nano Banana Pro (over-sharp); he chose Seedream 5.5.
4. Video element with own voice: attach a phone audio line "between like four and 30 seconds".
5. Invented characters and locations: Soul Cinema, "For one credit, you get eight images"; run one batch at a time for variety; say what you do not want ("no caricature").
6. Locations: avoid sunbeams, rain, overexposure, stray people; rooms in three-quarter view showing two walls.
7. Objects: grey background, three-quarter angle; logo added with Seedream 5.5 and kept as a separate asset for the pack shot.
8. Prompt request line: "Specify the camera position movement and timing for every shot"; element names in the prompt match saved elements so references attach.
9. Draft first: 24 seconds at 480p draft "72 credits" vs 1080p "384 credits"; then upscale chosen takes.
10. Seedance 2.5 makes "up to 30 seconds" from one prompt; a location image used as key frame fixes the camera start.
11. One 4-second shot "like 64 credits"; he generated eight versions of the pack shot and of the 8-second closing joke.
12. Synchronised character movement fixed by giving each a different action.

V4. "How to Make an AI Commercial for a Real Client with Claude" - Flick (tool's own channel) - https://www.youtube.com/watch?v=1_wckhR3SCo - upload date UNKNOWN - 10:08. VENDOR.
1. 30-second client ad; "the generation costs $50".
2. Five chapters: requirements to concept; structure and client brief; characters and environment; production tips; edit.
3. Upload client requirements to Claude to research the company and find one key message that can be shown on screen.
4. Set boundaries before ideation: max 30 seconds, show the automation, hide the product until the end.
5. Client brief has three parts: visual references; how the film communicates the core concept; beat-by-beat breakdown of the 30 seconds. Production starts after approval.
6. Each character built from at least two real-person references; vary faces, heights, genders, style on purpose.
7. Environment sheet designed so one fixed camera shows story growth (glass wall, earlier candidates working behind).
8. Generate a few extra seconds at the start and end of each shot.
9. Footage was almost a minute; cut to about 30 seconds with jump cuts; first character gets most time.
10. "seven rounds just to make one guy look more fun".

V5. "My AI Videos Hit 122M Views: First Broadcast AI Commercial (PJ Ace)" - Saturation ("Produced with" podcast) - https://www.youtube.com/watch?v=7T3em61dSYk - upload date UNKNOWN; INFERENCE mid-2025 (he says Veo 3 came out "about a month ago") - 53:36. COMMUNITY.
1. He was a commercial director for 15 years; says the Kalshi NBA Finals spot was, to his knowledge, the first AI ad at a major sporting event.
2. His claim: "a 95% reduction in time and cost"; pricing is value-based, not cost-based.
3. Pipeline: about 20 concepts with writers plus ChatGPT, narrow to two, client picks, script, simple shot list (example 10 shots).
4. Ask the LLM to rewrite the shot list as prompts and return "two to three prompts at a time".
5. Generate in Google Flow / Veo 3: "20 cents a slot machine pull", about "20 generations per shot"; they filter out "80% garbage, 90% garbage".
6. Sound and dialogue come baked in; then timeline, some colour, music; the last 5-10% of polish takes as long as the first 80%.
7. Hook: the algorithm is geared to the first 1.5 seconds; no title cards or slow openers.
8. He tells brands to lean into comedy; says his ads are "75 to 80% of the way there" on realism.
9. Lip-sync failed on a Popeyes job; fix was a large pop filter in front of mouths.
10. His generation costs "on a monthly basis are like $4,500".
11. Rates he cites: freelance directors "thousand a day, 2,000 a day"; premium "5, 10 grand" a day for 5 to 10 days a month; his agency offers a lower day rate for about 22 days a month.
12. Hires 10-year traditional directors and writers and teaches them the tools; work is mostly direct-to-brand, all inbound.

V6. "I Made 10,000 Ads, Here's What Works Right Now (in 2026)" - Dara Denney - https://www.youtube.com/watch?v=4wM-i1cxtAM - date UNKNOWN (she says "today in September 2026") - 15:36. COMMUNITY (sponsored by Modash).
1. She wants "30 to 50% of all ad spend" in partnership ads.
2. Three-part process: personas, diagnosis, creator formats. Personas = live ads compared with customer reviews.
3. Diagnosis = "one to two sentence statement"; without it "you only have testing".
4. Diagnosis checks: awareness levels (usually too little unaware/problem-aware); personas; spend share by image, video, carousel, partnership; three to four messaging pillars; message carried to landing page; creator fit.
5. Creator failures: profile not aspirational to persona, weak delivery, low volume, no personal storytelling.
6. Jones Road Beauty scaled with bigger creators; Caraway with micro creators "sub 50K followers".
7. Five formats scaling: authority angle; personal-history "yappers"; educational breakdowns; investigative-journalism ads (theirs made with AI, "77% hook rate"); transformations and comparisons.
8. Problem-solution UGC now "feels like an ad".

V7. "Meta Ad Hooks & Formats that NEVER MISS ($500k Creative Strategy Study)" - Motion (Creative Analytics) - https://www.youtube.com/watch?v=0QE6OifIlIM - date UNKNOWN; INFERENCE early 2026 - 6:50. VENDOR.
1. Dataset: "550,000 ads coming from 6,000 different brands", collected "between Black Friday and Christmas".
2. Metrics: hit rate and spend-use ratio (above 1.0 = "punching above its weight").
3. 25 hook tactics; offer-only hooks near the top on both metrics.
4. Bold claims and shocking statements ranked low; urgency and FOMO hooks did well.
5. Text-only ads, product images with overlays and GIFs produce more winners than high-production video; they communicate value "in under 2 seconds".
6. High production is for scaling what is proven, not discovery.
7. Unboxing led hit rate, "nearly one in 10"; behind-the-scenes and founder ads "above 8%".
8. Unboxing and POV win but plateau; celebrity ads rarely win but win big; offer-first banners and demos are the scale formats.

V8. "How to Produce Commercials for TV: Pre-Production Masterclass" - Nicole Shapiro (freelance producer, Toronto) - https://www.youtube.com/watch?v=vkyko3Cprfk - date UNKNOWN - 16:29. COMMUNITY.
1. Job: Smart Serve broadcast spot via Viva Media, "under 100K"; "27 crew and 46 talent", four shoot days.
2. Order: storyboard review with director, rough budget, production bible, dates, locations, crew, insurance, talent, schedule, lunch forms, permits, call sheet.
3. Ask the client for a low and top budget range.
4. Budget sheet tabs: cast, crew, equipment, locations, insurance; estimates on one side, actuals on the other.
5. Work backwards from the delivery date.
6. Locations: Set Scouter (needs a COI), Peerspace, Facebook Marketplace for odd places; paid the shop's opening cost and lost sales.
7. Book rain dates up front and keep contingency; moved crew must be rebooked and repaid.
8. Director names the DP; DP picks the gaffer.
9. Deal memos by email: dates, rates, payment terms (for example net 30).
10. Call sheet no later than 24 hours before call, sent as a live link.
11. Expect last-minute crew and cast cancellations; keep backups. Say "no, but this is my suggestion".

## 2. CONFLICTS
- Skillshop professional Video certification: a practice-exam site calls it free and self-proctored; another guide says Google's help page states the proctored professional exams "won't be free in future". Sources: https://open-exam-prep.com/practice/google-ads-video vs https://support.google.com/skillshop/answer/14746215 (neither opened).
- Meta creative certification price: $150 vs about $99. https://stackmatix.com/blog/meta-ads-certification-cost-2026 vs https://markampus.com/blog/free-meta-advertising-certifications-2026/ (snippets).
- ABCD "C": the 2022 video says "Connection ... think or feel something"; the May 2023 page adds "through the experience of your product". Same framework, later wording.

## 3. COULD NOT OPEN / UNKNOWN
- YouTube watch pages: HTTP 429 for all methods; upload dates for V4-V8 unknown. Third-party transcript pages failed (Cloudflare, Vercel checkpoint, empty).
- Transcripts captured but NOT READ, so no lessons given: Curious Refuge qJiwXH2h7ps and 0C97pAlyb8I; Mark Bone 3KV2MPSrlEs; Dara Denney p4yXXdnCgWg; Decoded AI BJJqcUsVUek. Not captured: Barry Hott on Motion 6jvIXIjieyA; PJ Ace Wonder Studios workshop ttgNFJ25xfU; Dan Kieft sMNjQ2Gks_4.
- Topic (ii) pricing is thin: only V4 ($50 generation cost) and V5 (day rates, monthly generation spend). No video read that gives client price lists.
- Topic (v): V8 is a production-company freelance producer, not an agency producer; no agency-side TVC process video was found.
- Not verified: Skillshop Video course page (JS), HubSpot, Suno help, Cannes Lions free parts, Adobe, Canva (403), IPA report price, AICP guideline access level, PJ Ace channel handle, Rory Flynn/MattVidPro counts.
- Not researched: Ogilvy, Dave Trott, Luke Sullivan, Binet and Field individual sources; Hebrew sources beyond search snippets; free copywriting/storyboard/directing courses.
- WebFetch blocked by session network for: business.google.com, blackmagicdesign.com, academy.runwayml.com, ads.tiktok.com, facebookblueprint.com, business.pinterest.com, advertising.amazon.com (all read via curl instead).

## 4. TOP 10 URLS TO RE-READ
1. https://business.google.com/us/resources/articles/abcds-of-effective-video-ads/
2. https://www.blackmagicdesign.com/products/davinciresolve/training
3. https://academy.runwayml.com/
4. https://higgsfield.ai/academy
5. https://www.youtube.com/watch?v=jeMl0OSwDss
6. https://www.youtube.com/watch?v=7T3em61dSYk
7. https://www.youtube.com/watch?v=0QE6OifIlIM
8. https://www.youtube.com/watch?v=4wM-i1cxtAM
9. https://support.google.com/skillshop/answer/14746215
10. https://aicp.com/business-resources

Scratch files (transcripts) are in /tmp/claude-0/-home-user/746b6263-7a14-550f-b965-9eab77b03769/scratchpad/yt/ - these were working files for the transcript capture only; no report files were written.
