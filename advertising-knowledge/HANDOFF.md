# HANDOFF - advertising knowledge base and skill system

Last update: 20 Nov 2026 (session 1). Status (21 Nov 2026): wave 1 research done; 10 raw reports saved, UNVERIFIED. Advertising studio system built in advertising-studio/ + .claude/. Waves 2-5 not started.

## What this job is
Build a verified knowledge base + skills for advertising in all media, and a general
"recommend tools/models/prices first, then teach step by step" behaviour for every creative request.
Full plan: PLAN.md. File list: INDEX.md.

## Hard rules (owner's, apply in every session)
1. Reply to the owner in Hebrew only; Hebrew and English never on the same line.
2. Never invent facts, prices, specs, rules. Unverified = say so. Official sources first.
3. Never buy, start a trial, or press buy / upgrade / subscribe / publish / generate. Paid tools: present cost, pros, cons, free alternative, recommendation; act only after an explicit yes.
4. Sub-agents: free tools only, own isolated browser, read-only on his accounts.
5. Never save to his Google Drive or computer; never delete or overwrite his files, skills, docs without asking.
6. Never tell him "see section X" - paste the text. Do not end a reply with a question or an offer.
7. Explain the why in one sentence; numbered steps.
8. Only the main agent writes files, docs and skill cards.

## Done in session 1 (20 Nov 2026)
- Listed all 157 synced skills (about 132 are the owner's, 25 are built-in Anthropic skills that cannot be edited).
- Read skill-cards-publisher in full; read descriptions of all skills; read section maps + routing of the core ad skills.
- Wrote PLAN.md, INDEX.md, this file.

## Findings that change the plan (all OBSERVED in session 1)
1. This cloud session has NO skill save-card tool (propose_skills). Cards can only be issued from a claude.ai chat. So this job produces final drafts + proven edit lists in files; a claude.ai chat then publishes them in rounds of 3 with skill-cards-publisher.
2. The cloud environment "Higgsfield CLI" has LIMITED network: only higgsfield.ai hosts. Built-in WebSearch works; built-in WebFetch and the Playwright browser cannot reach gov.il, support.google.com, youtube.com, etc. Official pages cannot be read until the owner widens the network (free) or approves a connector fetcher (Firecrawl / Parallel / Nimble - may use credits on his accounts; cost not checked).
3. All three attached GitHub repositories are PUBLIC. Anything pushed here is public.
4. Existing coverage (do not duplicate): ad strategy = ai-advertising-director; pricing, quote, contract = ai-ad-pricing-and-selling; legal gate, labels = ai-video-legal-consent-labels; organic social formats + AI labels = video-marketing-distribution (6 platform reference files); formats = ai-video-formats-catalog; model prices = ai-video-tools-and-prices + ai-video-other-platforms-leaderboards-budgets-credit-saving + higgsfield-plans-and-credits-per-shot-price-table; idea -> free vs paid path = ai-video-idea-advisor; connectors = ai-connectors-map; music licences = ad-music-licensing-stock-libraries-and-sfx-sources-verified; brand film = client-brand-film-production; business = ai-business-starter; hubs = ai-video-project-workflow, higgsfield-hub, suno-and-ai-sound-hub, blender-hub.
5. Gaps (new material): paid-media specs per platform (TV, streaming/CTV, YouTube ads, Meta ads, TikTok ads, Google Ads, DOOH, radio, podcasts, print, cinema, in-app, influencer); Israeli broadcast process and approvals; full brief-to-delivery pipeline with roles and timelines; usage rights / buyouts depth; a single cross-domain "recommend then teach" entry skill.

## Decisions (owner, 20 Nov 2026)
A. Research fan-out: APPROVED.
B. Network: environment "Higgsfield CLI" changed to unrestricted (owner approved the card). curl to gov.il returns 403 (bot block) - use a real browser; youtube.com returned 429 to curl.
C. Paid web connectors (Firecrawl / Parallel / Nimble): NOT used.
D. Storage: this repository (public); no personal data in files.
E. General-rule section: creative skills only.
F. Skill architecture (owner's words, paraphrased): comprehensive skills built as BRANCHES - one main hub skill that controls and routes to every branch; each branch short, complete, with a very clear name and a very clear "use when / not for" so the model is never confused; many small branches are welcome.

## Wave 1 roles launched (general-purpose sub-agents, background)
R1a TV/streaming, R1b YouTube+Google Ads, R1c Meta+TikTok+social, R1d DOOH/radio/podcast/print/cinema/in-app/influencer,
R2 Israel, R3 pipeline, R4a AI video+image tools, R4b other tools, R5 business, R6 learning + transcripts.
R4c (connector inventory) done by the main agent -> knowledge/10-connectors-inventory.md.
Raw reports go to research-raw/ as they arrive. A report NOT in research-raw/ = lost with the session; re-run that role.

## Next step for a new chat
1. Read PLAN.md and INDEX.md.
2. Check research-raw/ for which roles are saved; re-run missing roles with the brief in research-raw/COMMON_BRIEF.md.
3. Continue with wave 2 (knowledge files), wave 3 (verifiers), wave 4 (skill drafts).

## Session 1 continued (21 Nov 2026)
- Raw reports saved in research-raw/: R1a, R1b, R1c, R1d, R2, R3, R4a, R4b, R5. R6 saved too (8 videos read in full; 8 more listed as NOT READ). All 10 raw reports are saved.
- Research agents could not open: gov.il (all pages), nevo, kolzchut, kan.org.il, adobe.com, openai.com, sagaftra.org, x business help, Higgsfield pricing page. Those facts are SNIPPET or UNKNOWN and must go to the verifier with a real browser, or be read by the owner.
- New owner requests (20-21 Nov):
  1. Wants everything private -> he was given the steps to make the repository private (his action). Do not make the bubapix repositories private without checking how the preview site is hosted.
  2. Wants skills written "on the computer" like other skills. This cloud session has no computer folder attached (list_computer_folders returned none) and no save-card tool. Skills for his Claude account must be issued as save cards from a claude.ai chat.
  3. System build (done): 8 agents in .claude/agents, 17 skills in .claude/skills, tools/studio.py gates, templates, registry, docs. See advertising-studio/CLAUDE.md and documentation/test-results.md (what was and was NOT tested).
  4. AFTER all research and skills are finished: a surprise gift ad for a business whose material is in the folder named "דיגיטלי" inside his Downloads folder (offers, reports, photos from their site). He cannot contact them before delivery. Wants several ideas, a full drawn storyboard with images, improved photos, a cinematic ad, model and platform recommendation with commercial licence checked. This is the acceptance test of the whole system. BLOCKED until that folder is reachable (share it through Remote Control or run the session on his computer). Spec-ad cautions apply: no consent from the business, their trademarks and photos, truth gate - see ai-advertising-director "Spec-ad rule" and ai-video-legal-consent-labels.
- Usage note: the 5-hour usage limit was hit once with 10 agents in parallel; run fewer agents at a time.
