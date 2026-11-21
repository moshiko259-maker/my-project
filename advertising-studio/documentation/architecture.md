# Architecture (built 21 Nov 2026)

```
                         OWNER (approves every gate, in Hebrew)
                                   |
                     EXECUTIVE PRODUCER  (main thread)
        skills: ad-project-intake, production-budget-control
        tools: files, studio.py, Agent(7 specialists)   - no generation tools
   ________________________________|_________________________________________
  |            |             |              |               |          |      |
RESEARCH &   CREATIVE    SCRIPTWRITER   STORYBOARD &    AI VISUAL    QUALITY  POST &
BRAND        DIRECTOR                   ART DIRECTOR    PRODUCTION   CONTROL  DELIVERY
STRATEGIST                                              DIRECTOR
web + files  files only   files only    files only      files, Bash, read +   files, Bash
                                                        Higgsfield   QC log
                                                        (ONLY agent  only
                                                        that can
                                                        generate)
  |            |             |              |               |          |      |
 3 skills    1 skill       1 skill        4 skills        4 skills   2 skills 2 skills
                                   |
        KNOWLEDGE LAYER (not copied): the owner's ~130 saved skills
        (advertising, Higgsfield family, sound family, Blender family, legal, pricing)
        + advertising-knowledge/ files with source, date and tag per fact
                                   |
        CONTROL LAYER: studio.py gates + approvals.json + generations.csv
                       .claude/settings.json "ask" rules on every generation tool
```

## Three layers
1. Procedure: 17 studio skills (what to do, in what order, what to output, checklist).
2. Knowledge: the owner's existing skills and `advertising-knowledge/`. Each studio skill names the knowledge skills that own its details.
3. Control: gate script (soft, checked by the agents), permission "ask" rules (hard, enforced by Claude Code unless permissions are bypassed), tool limits per agent.

## Why the producer is the main thread
A sub-agent cannot start other sub-agents. So the Executive Producer is run as the session's main agent (`claude --agent executive-producer`), or the normal main session takes that role by following the root `CLAUDE.md`.

## Known limits
- The gate script records and checks approvals; it cannot physically stop a tool call. The hard stop is the permission prompt. In bypass-permissions mode there is no hard stop.
- The owner's saved knowledge skills exist in his Claude account. In Claude Code they load as account skills; if a session does not have them, the studio skills still work but with less depth.
- The model registry holds no verified capabilities yet.
