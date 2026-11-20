# 10 - Connectors inventory (what is connected, what it can do for ad work)

Date: 20 Nov 2026. Source for every row: the live tool list of the owner's cloud session on 20 Nov 2026 (tag OBSERVED = seen in the session's tool list; no tool was called, nothing was spent). Prices and credit costs are NOT in this file - they live in ai-connectors-map and the price skills, and must be re-checked live before any paid run.
"Connected" means the tools were listed. It does not prove the account is signed in or has credits.

## Creative generation (every generate call spends the owner's credits - never without his written yes)
| Connector | Useful for (stage) | Free read-only calls seen | Calls that spend / act for real |
|---|---|---|---|
| Higgsfield | image, video, audio, 3D, ads (Ads Studio, Marketing Studio), reframe, upscale, virality check | balance, models_explore, estimate_image_cost / estimate_video_cost / estimate_audio_cost, get_presets, show_plans_and_credits | generate_*, ads_studio_generate, execute_preset, upscale_*, publish_*, tiktok publish, meta_ads_write |
| Runway | video, image, multishot, music, SFX, speech, ad creation (create_ad, localize_ad), upscale | whoami, show_plans_and_credits, list_*, get_skill | generate_*, create_ad, edit_video, upscale_*, run_workflow |
| ElevenLabs | speech, voice design, image, video, transcription; voice agents | creative_list_voices, account_get_usage, get_model_guide | creative_generate_*, design_voice, agents_outbound_call |
| Suno | songs, jingles, sounds, speech, stems, MIDI | account-me, account-usage, library-*, audio-analysis | audio-create, sounds-create, stems, covers, account-upgrade |
| HyperFrames (HeyGen) | code-built motion graphics video rendered in the cloud | list_projects, get_project, get_render_status | compose and render_video are disabled from CLI/IDE clients (observed in the connector's own instructions) |
| Canva | designs, resize for social, brand templates, export | search-designs, list-brand-kits, get-export-formats | generate-design, generate-image, create-video, export |
| Adobe (Express, Firefly Boards, Acrobat, fonts, photo/video tools) | layouts, social variations, background removal, quick cut, resize, PDF | asset_search, font_search, get_account_type | image_generative_expand, video_render, asset_license_and_download_stock |
| Figma | design files, diagrams, FigJam boards (storyboards) | whoami, get_metadata, get_screenshot | generate_image, weave_run_model, use_figma writes |
| Gamma | pitch decks, proposals | get_themes, search_templates | generate, generate_image |
| vidIQ | YouTube research, titles, thumbnails, transcripts | channel and keyword tools | generate_*, publish, update_video (credit balance tool: vidiq_balance) |
| Hugging Face (+ Spaces) | free open models through Spaces (image) | hub_repo_search | dynamic_space runs (quota) |
| Unsplash | free stock photos (check licence for ads) | search_photos | download_asset |
| Trimble SketchUp | simple 3D sets | list_skills | build_model |

## Research and data (some bill per request - treat as paid)
Firecrawl, Parallel Search, Nimble, Clay, Supermetrics, Metricool, Zapier, Context7 (failed to connect in this session), Claude Academy.

## Publishing, clients and business (act for real - never without his written yes)
Metricool (schedule posts), Postiz skill, Higgsfield TikTok and Meta Ads tools, vidIQ social publish, Upwork (jobs, proposals, messages), Gmail (read and labels only in the listed tools), Google Calendar, Google Drive / Docs / Sheets / Slides, Slack, Notion, Lovable, Framer, Vercel, Supabase, Expo, GitHub.

## Not connected / needs sign-in (OBSERVED 20 Nov 2026)
Datadog and GitLab need authorisation. About 55 plugin servers failed to connect because of the then-limited network - not relevant to ad work.

## UNKNOWN - verify before use
1. Blender connector: not in this cloud session's tool list (it is a local connector on the owner's computer per blender-hub).
2. Live credit balance of each paid connector - read it with the free balance call at the start of a job.
3. Whether any generation tool has a free quota today.
