# Test results (21 Nov 2026)

## Run and passed
- Structure validation of 17 skills and 8 agents: `studio.py validate` -> VALID (frontmatter, names, activation and 'Not for' lines, required sections, template files exist, every skill attached to an agent, every agent's skills exist, only one agent holds generation tools, delegation list names real agents, no two descriptions more than 60% alike).
- Gate behaviour on a throwaway project (output below; the project was deleted afterwards).

```
T1 new:
created advertising-studio/client-projects/zz-sample-test
T2 check before approval (expect BLOCKED, exit 1):
BLOCKED: no owner approval recorded for gate 'paid-images'
exit=1
T3 log without approval (expect refused):
refused: no approval for gate 'paid-images' - this generation should not have run; report it to the owner
exit=1
T4 approve by agent (expect refused):
only the owner can approve (--by owner)
exit=1
T5 approve paid gate without ceiling (expect refused):
paid gates need --ceiling <credits>
exit=1
T6 approve with ceiling 10:
recorded paid-images
T7 check (expect APPROVED):
APPROVED: paid-images; spent 0 of 10 credits
exit=0
T8 log 8 credits then check (expect 80% warning):
logged; total spent 8.0
APPROVED: paid-images; spent 8 of 10 credits - WARNING 80% used
T9 log 2 more then check (expect BLOCKED ceiling):
logged; total spent 10.0
BLOCKED: ceiling reached (10 of 10 credits) - new approval needed
exit=1
T10 other paid gate still blocked:
BLOCKED: no owner approval recorded for gate 'paid-video'
exit=1
T11 second new on same slug (expect not overwritten):
exists, not overwritten: advertising-studio/client-projects/zz-sample-test
exit=0
T12 settings.json valid JSON + ask rules:
31 ask rules
T13 client-projects git-ignored:
?? advertising-studio/client-projects/
ignored
```
Note: T11 prints exit=0 because the test piped the output; the message shows the folder was not overwritten.

## NOT tested (stated plainly)
- Live delegation by the Executive Producer to the seven agents: project agents load only when a session starts in this folder, so it could not be exercised from the session that built them.
- Intake, research, concept, script and storyboard runs on sample data by the agents themselves.
- Model selection against a live model list (no Higgsfield workspace selected here).
- The permission "ask" rules in a real run (the file is valid JSON with 31 rules; the prompts themselves were not triggered).
- Any generation: none was run, by design.

## First real test to do
Start `claude --agent executive-producer` in this folder with a small sample brief and confirm: (1) it delegates research to research-brand-strategist, (2) it stops at the strategy gate, (3) a Higgsfield command shows a permission prompt.

## Live agent test 1 (21 Nov 2026) - creative-director on a fictional sample project - PASSED with fixes
What ran: the `creative-director` project agent was started from the main session on `client-projects/zz-sample-test` (fictional honey brand, facts + strategy only).
Observed:
- The agent loaded; its skill `creative-concept-development` arrived preloaded with the hard rules; both CLAUDE.md files were injected.
- It wrote 3 concepts with different mechanisms + a comparison, recommended one, recorded no approval, ran nothing paid.
- It did NOT use the fact marked UNKNOWN (health benefits) and kept the unproven client claim out of every concept.
- It had no way to load the owner's knowledge skills (no Skill tool).
Fixes made after the test: Skill tool added to all agents; rule for missing inputs (continue, mark UNKNOWN); attempts/credits removed from the concept template (belongs to budget control); cost score direction defined; comparison template added; scores kept in one place; language rule clarified (owner-facing Hebrew, agent-to-producer English); "stop for approval" defined for sub-agents.
Still not tested: the other six specialists, delegation started by the executive-producer itself, the permission prompts, model selection against a live list.
