# Usage guide

## Start a project
1. Open the repository folder in Claude Code.
2. Run: `claude --agent executive-producer`
3. Write, for example: "New client project. Material is in <folder path>. Goal: a 30-second cinematic ad. The client must not be contacted."
4. The producer creates `advertising-studio/client-projects/<slug>/`, copies the material in, and reports what it found and what is missing.

## What you will be asked to approve, in order
strategy -> concept -> script -> storyboard -> models -> paid-images -> paid-video -> paid-audio -> delivery -> publish.
Each paid approval comes with a written estimate and a credit ceiling. Nothing paid runs before your yes.

## Useful commands (free, local)
- `python3 advertising-studio/tools/studio.py status <slug>` - files per stage, gates, credits spent.
- `python3 advertising-studio/tools/studio.py validate` - checks all agents and skills.
- `python3 advertising-studio/tools/build_system.py` - rebuilds agents and skills after editing the table.

## Higgsfield in this environment
- CLI installed: version 1.2.2. Sign-in state: no workspace selected ("hf workspace set <workspace_id>" is requested by the CLI). Signing in is the owner's action.
- Official Higgsfield skills installed: higgsfield-generate, higgsfield-product-photoshoot, higgsfield-soul-id, higgsfield-brandkit, higgsfield-marketplace-cards, higgsfield-youtube-thumbnail, higgsfield-faceless-video, higgsfield-video-explainer, higgsfield-websites.
- Higgsfield MCP connector: listed as connected in the session; not called during the build.

## Where client files must be
The system can only read folders that the session can reach. In a cloud session that means files inside this repository's working copy or a computer folder shared through Remote Control. A folder that exists only on the owner's computer is not reachable from a cloud session until it is shared or the session runs on that computer.
