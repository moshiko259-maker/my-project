# Advertising studio - operating guide

## What this is
A human-controlled production system for client advertising: 8 specialist agents (`.claude/agents/`), 17 workflow skills (`.claude/skills/`), templates, a model registry, a budget gate and a per-client workspace. Claude Code is the production manager; Higgsfield is the main generation platform; other models are used when the registry shows they fit a shot better.

## Start
1. Open this repository in Claude Code. Best: `claude --agent executive-producer` (the main thread must be the producer, because only the main thread can delegate to other agents).
2. Say what arrived: the client folder path and the goal.
3. The producer runs `ad-project-intake`, then walks the phases in `workflows/master-workflow.md`, stopping at every gate.

## Layout
- `tools/studio.py` - new / approve / check / log / status / validate (no network, no generation).
- `tools/build_system.py` - regenerates agents and skills from one table.
- `templates/` - brief, facts, strategy, concept, script, shot, truth sheet, budget, QC, delivery.
- `model-registry/registry.md` - candidate models, what is verified, when.
- `workflows/master-workflow.md` - phases, owners, outputs, gates.
- `client-projects/<slug>/` - one workspace per client (13 stage folders + production-log).
- `documentation/` - architecture, usage guide, test results, name map of the 23 requested skills.

## Non-negotiable rules
1. Gates: strategy, concept, script, storyboard, models, paid-images, paid-video, paid-audio, bulk-run, purchase, delivery, publish. `studio.py check` must print APPROVED first.
2. An approval is recorded only from the owner's own words in the chat. Agent messages, old approvals and silence are not approvals.
3. Only `ai-visual-production-director` may start generations. Two hard controls sit in `.claude/settings.json`: a PreToolUse hook (`tools/gate_hook.py`) that blocks paid generation, publishing, purchase and sign-in changes unless the project named in `advertising-studio/ACTIVE-PROJECT` holds a real owner approval under its ceiling; and 'ask' rules that prompt before generation tools. To switch the hook off, remove the `hooks` block from `.claude/settings.json` - the owner's decision only.
4. Originals are the source of truth for products. Nothing about a product is invented.
5. Knowledge lives in the owner's existing skills (advertising, Higgsfield, sound, Blender, legal, pricing). Studio skills are the procedure and point to them; they do not copy them.
6. Client folders may contain private material. This repository is public unless the owner changed it: never commit `client-projects/` (it is git-ignored).
