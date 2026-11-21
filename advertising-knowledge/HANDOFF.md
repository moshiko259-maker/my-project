# HANDOFF - advertising knowledge base and skill system

Last update: 21 Nov 2026 (end of session 1). Status: research done and partly verified; studio system built and partly tested; 8 new account skills drafted; 108 proven edit lists built. NOT done: save cards (need a claude.ai chat), the acceptance-test ad (needs the owner's Downloads folder).

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

## State at end of session 1 (21 Nov 2026) - read this first
DONE
- 10 raw research reports (research-raw/), 11 knowledge files (knowledge/), 3 verifier reports (verification/): 304 rows re-read, 286 PASS, 4 CHANGED, 1 FAIL corrected. Log: knowledge/15-verification-log.md.
- Account skills, drafted and validated with publisher script A: skill-drafts/<name>/SKILL.md (8 skills).
- General-rule section: 108 one-edit lists in skill-drafts/edits/, each proven; list and sizes in skill-drafts/EDITS-INDEX.md; rounds in skill-drafts/ROUNDS-PLAN.md (39 rounds).
- Studio system: advertising-studio/ + .claude/agents (8) + .claude/skills (17) + .claude/settings.json (31 ask rules). Tests: documentation/test-results.md.
NOT DONE
1. Save cards: open a claude.ai chat (it has the card tool), load skill-cards-publisher, and publish rounds 1-39 from skill-drafts/. Re-prove each edit against the current saved skill first.
2. Requested skill name was 68 characters; drafts use creative-request-advisor-tools-models-prices-then-teach-steps (61). Owner informed.
3. Acceptance test: the surprise gift ad from the owner's Downloads folder "דיגיטלי" - blocked until the folder is reachable. Start with `claude --agent executive-producer`.
4. Not verified / unknown (do not present as fact): Israeli tax figures on official pages; Israeli channels' delivery specs; Adobe Firefly; Disney+, NBCU, Max specs; Snapchat, X, Reddit; print; rows tagged DRAFT in files 07, 09, 11, 13.
5. Studio: delegation from the executive-producer itself, six of seven specialists, permission prompts and live model selection are untested. The model registry has verified rights and costs for Higgsfield only; no capability scores.
6. Prices read on 21 Nov 2026 include Black Friday promotions; re-check live.
LESSONS
- 10 agents in parallel exhausted the 5-hour usage limit; run 3 at a time. Agents can be resumed with SendMessage after the limit resets.
- WebFetch does not work in this cloud environment even with unrestricted network; agents must use curl or the headless browser.
- Never instruct an agent to get around a site's bot block: the request is refused, and the block is the site owner's decision.
- Save every sub-agent report to the repository immediately; the worker restarted several times and only pushed files survived.
- The owner's saved skills must not be copied in full into this public repository; edit lists hold only a short anchor and the new text.

## Addendum, later on 21 Nov 2026
- Gap-fill round done: knowledge files 06 (Israel), 14 (expert lessons), 16 (platforms and tools); skills updated from them.
- Skill upload route VERIFIED on the official support page (Customize > Skills > Upload a skill; ZIP containing the skill folder; folder name = skill name). Eight upload-ready archives: advertising-knowledge/ready-to-upload-skill-zips/. Whether uploading replaces an existing skill of the same name is UNKNOWN - edits to saved skills still go through save cards.
- Owner wants everything on his computer: a full package (work files + a private backup of his saved skills as synced on 20 Nov 2026) was sent to him as a download; the saved-skill copies are NOT in this repository. Hebrew guide: advertising-knowledge/START-HERE-HEBREW-GUIDE.md.
- YouTube refused all requests on 21 Nov 2026 (429 / unplayable); do not retry in a loop. gov.il service pages refuse automated access, but files under gov.il/BlobFolder open normally.

## Addendum 2, 21 Nov 2026 08:12 UTC
- The owner uploaded all 8 new account skills himself (ZIP upload). Verified: each synced copy is identical to its draft. Rounds 1-3 are DONE. If a draft changes after this point, the saved skill must be updated again (upload-replace behaviour still unknown - check with one skill first).
- He also uploaded three of the studio's procedure skills to the account: ad-project-intake, ad-scriptwriting, advertising-strategy (identical to .claude/skills). The other 14 studio skills are only in the repository.
- Still open: the 108 edits (rounds 4-39), the acceptance-test ad, a second live studio test (scriptwriter) and a re-try of the unread expert videos were running when this was written.

## Addendum 3, 21 Nov 2026 (after five live studio tests)
- Five of seven specialists tested live on the fictional sample (creative, script, storyboard, visual production planning, post planning); every gap found was fixed. Results: advertising-studio/documentation/test-results.md.
- The gate is now enforced by code: test markers never count (studio.py), and a PreToolUse hook (advertising-studio/tools/gate_hook.py, wired in .claude/settings.json) blocks paid generation, publishing, purchase and sign-in changes without a real approval for the project named in advertising-studio/ACTIVE-PROJECT. Unit-tested; NOT yet seen firing in a real session.
- Model registry now holds live Higgsfield settings and credit prices (read 21 Nov 2026); quality scores still empty.
- Pending edit to a saved skill: ai-video-legal-consent-labels lists three regions for Google's visible AI label; verified current list is six.
- YouTube refuses playback from this cloud network (asks for sign-in); unread videos need the owner's pasted transcripts or a session on his computer.
