# Model capability registry

Rule: a model is credited only with what a row shows as VERIFIED (official page read, with date) or TESTED (the owner's own run, with job id). Everything else is UNVERIFIED and must be checked live before it is used in a plan. Entries older than 14 days are treated as UNVERIFIED.
Live re-check (free): `higgsfield model list --video`, `higgsfield model list --image`, `higgsfield model get <id>`, `higgsfield generate cost <id> ...`, the MCP `models_explore`, vendor pricing and terms pages.

Status of this file (21 Nov 2026): STRUCTURE READY, CAPABILITIES NOT YET VERIFIED. The Higgsfield CLI is installed (1.2.2) but no workspace is selected in this cloud environment, so its model list could not be read during the build. The ranking rows below come from one raw research report and have not passed the verifier.

## Criteria (score 1-5 only from VERIFIED or TESTED evidence)
image quality | video quality | reference fidelity | product accuracy | character consistency | motion quality | camera control | prompt adherence | speed | credit cost | commercial-use terms

## Candidates
| Model | Type | Where available | Capabilities | Cost | Commercial use for client ads | Status | Source / date |
|---|---|---|---|---|---|---|---|
| Seedance 2.5 | video | Higgsfield and others | UNVERIFIED | UNVERIFIED on Higgsfield | check plan terms | UNVERIFIED | ranked 1 image-to-video, 4 text-to-video on Artificial Analysis (COMMUNITY, read 20 Nov 2026, raw report R4a) |
| Kling 4.0 | video | Higgsfield, Kling | UNVERIFIED | UNVERIFIED | Kling paid plans list "for commercial use" (VENDOR, R4a) | UNVERIFIED | not in the leaderboard rows read |
| Veo 3.1 / Omni Flash 1.2 | video | Google Flow | UNVERIFIED | UNVERIFIED | UNKNOWN | UNVERIFIED | Google Flow help: Veo 3.1 Fast and Quality retire 5 Dec 2026 (OFFICIAL, R4a) |
| Wan 3.0 | video | Wan, Higgsfield | UNVERIFIED | UNVERIFIED | UNKNOWN | UNVERIFIED | ranked 1 text-to-video on Artificial Analysis (COMMUNITY, R4a) |
| MiniMax H3 | video | several | UNVERIFIED | UNVERIFIED | UNKNOWN | UNVERIFIED | R4a |
| GPT Image 2.6 | image | Higgsfield, OpenAI | UNVERIFIED | UNVERIFIED | UNKNOWN (OpenAI pages not readable) | UNVERIFIED | ranked 1 text-to-image on Artificial Analysis (COMMUNITY, R4a) |
| Nano Banana Pro / 2 / 2.1 | image | Higgsfield, Google | UNVERIFIED | UNVERIFIED | UNKNOWN | UNVERIFIED | R4a |
| Seedream 5.5 | image | Higgsfield, Dreamina | UNVERIFIED | UNVERIFIED | UNKNOWN | UNVERIFIED | R4a |
| Soul 2.0 / Soul Cinema | image | Higgsfield | UNVERIFIED | UNVERIFIED | UNKNOWN - Higgsfield terms clause not read | UNVERIFIED | - |
| FLUX 3 | image / video | BFL, Higgsfield | UNVERIFIED | UNVERIFIED | UNKNOWN | UNVERIFIED | R4a |

## Open item that blocks commercial work
Higgsfield's commercial-use clause for the owner's plan has not been read (the terms page did not yield its text to the research agent). It must be read and quoted here before any Higgsfield output goes into a client ad.

## Test log (owner's own runs)
| Date | Model | Shot type | Result | Credits | Job id | Lesson |
|---|---|---|---|---|---|---|
