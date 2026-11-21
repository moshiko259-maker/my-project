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
| Soul 2.0 / Soul Cinema | image | Higgsfield | UNVERIFIED | Soul 2.0: 0.12 credits per image (VENDOR, 21 Nov 2026) | allowed by Higgsfield Terms s.4.4 (VERIFIED) | cost + rights read; capabilities UNVERIFIED | pricing page + terms, 21 Nov 2026 |
| FLUX 3 | image / video | BFL, Higgsfield | UNVERIFIED | UNVERIFIED | UNKNOWN | UNVERIFIED | R4a |

## Commercial use on Higgsfield - VERIFIED 21 Nov 2026 (Terms of Use, last updated October 23, 2026, s.4.4)
"Company does not claim ownership of any of your Inputs or Outputs, nor does it restrict your commercial use of Outputs ... you may transfer or sublicense your rights in Outputs to your clients or other third parties."
Limits read on the same pages: inputs and outputs may be used to train the company's models; no guarantee that an output is unique; disclose AI generation where the law requires and do not remove provenance marks (s.5.5, s.6.4); files made on the FREE plan keep a visible watermark (regenerate on a paid plan); "Unlimited" generations work only on higgsfield.ai, not through MCP / CLI.
Each third-party model reached through Higgsfield may carry its own terms: UNVERIFIED.

## Higgsfield credit costs read on the pricing page 21 Nov 2026 (VENDOR; confirm with a live estimate before any run)
Per 5 s: Seedance 2.5 720p 35, 1080p 80; Kling 4.0 720p 12.5, 1080p 18.75; Wan 3.0 720p 7.5, 1080p 15. Veo 3.1 about 40 per 4 s. Per image: Nano Banana Pro 2 (4K: 4); GPT Image 2.6 1.75; Seedream 5.0 Pro 2.5; Soul 2.0 0.12.

## Test log (owner's own runs)
| Date | Model | Shot type | Result | Credits | Job id | Lesson |
|---|---|---|---|---|---|---|
