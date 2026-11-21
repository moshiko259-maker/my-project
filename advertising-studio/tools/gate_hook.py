#!/usr/bin/env python3
"""PreToolUse hook: blocks paid generation, publishing and account-changing calls unless the active
client project holds a real owner approval for the matching gate and is under its credit ceiling.
It only ever BLOCKS (exit 2) or lets the normal permission flow continue (exit 0). It runs nothing else.
Active project: one line with the slug in advertising-studio/ACTIVE-PROJECT (written by the producer)."""
import json, pathlib, re, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
try: ev = json.load(sys.stdin)
except Exception: sys.exit(0)
tool = ev.get("tool_name", ""); inp = ev.get("tool_input", {}) or {}
gate = None
if tool == "Bash":
    c = inp.get("command", "")
    if re.search(r"\b(higgsfield|higgs|hf)\b[^|;&]*\b(generate\s+(create|workflow)|soul-id\s+(create|train)|website\s+(deploy|publish)|marketing-studio\s+\w*(create|generate)|product-photoshoot\s+(create|generate)|marketplace-cards\s+(create|generate))", c): gate = "bulk-run" if "batch" in c else "paid-images"
    if re.search(r"\b(higgsfield|higgs|hf)\b[^|;&]*\b(workspace\s+set|auth\s+(login|logout))", c):
        print("BLOCKED by the studio gate: changing the Higgsfield sign-in or workspace is the owner's own action.", file=sys.stderr); sys.exit(2)
else:
    t = tool.lower()
    if re.search(r"(publish|tiktok_prepare_publish|meta_ads_write|social_post_publish|createscheduledpost|send_message)", t) and "higgsfield" in t or re.search(r"higgsfield__(publish|tiktok_prepare|meta_ads_write)", t): gate = "publish"
    elif re.search(r"(account-upgrade|auto.?refill|buy|purchase|checkout)", t): gate = "purchase"
    elif re.search(r"batch", t) and re.search(r"generate", t): gate = "bulk-run"
    elif re.search(r"(generate_video|upscale_video|motion_control|reframe|scene_builder_3d_generate_video|video-create|creative_generate_video|generate_multishot|create_ad|ads_studio_generate|edit_video)", t): gate = "paid-video"
    elif re.search(r"(generate_audio|create_voice|voice_change|audio-create|sounds-create|speech-create|creative_generate_speech|generate_music|generate_speech|generate_sound)", t): gate = "paid-audio"
    elif re.search(r"(generate_image|generate_3d|execute_preset|upscale_image|outpaint_image|ai_influencer_generate|creative_generate_image|creative_edit_image|image-create)", t): gate = "paid-images"
if not gate: sys.exit(0)
f = ROOT / "advertising-studio" / "ACTIVE-PROJECT"
slug = f.read_text().strip() if f.exists() else ""
if not slug:
    print(f"BLOCKED by the studio gate ({gate}): no active client project is set, so no owner approval can exist. Present the estimate to the owner first.", file=sys.stderr); sys.exit(2)
r = subprocess.run([sys.executable, str(ROOT/"advertising-studio/tools/studio.py"), "check", slug, gate], capture_output=True, text=True)
if r.returncode != 0:
    print(f"BLOCKED by the studio gate for project '{slug}': {r.stdout.strip() or r.stderr.strip()}", file=sys.stderr); sys.exit(2)
sys.exit(0)
