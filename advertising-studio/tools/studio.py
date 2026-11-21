#!/usr/bin/env python3
"""Studio helper: project scaffold, approval gates, generation log, system validation.
No network, no generation. Usage:
  studio.py new <slug>
  studio.py approve <slug> <gate> --by owner --quote "<owner's words>" [--ceiling N]
  studio.py check <slug> <gate>            exit 0 + APPROVED, else exit 1 + BLOCKED
  studio.py log <slug> --shot S --model M --credits N --job ID --file PATH [--gate G]
  studio.py status <slug>
  studio.py validate                       checks agents, skills and links
"""
import argparse, csv, datetime, json, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
PROJECTS = ROOT / "advertising-studio" / "client-projects"
STAGES = ["01-brief","02-original-assets","03-research","04-strategy","05-concepts","06-scripts","07-storyboard",
          "08-prompts","09-generated-images","10-generated-videos","11-quality-control","12-post-production",
          "13-final-delivery","production-log"]
GATES = ["strategy","concept","script","storyboard","models","paid-images","paid-video","paid-audio","bulk-run","purchase","delivery","publish"]
PAID = {"paid-images","paid-video","paid-audio","bulk-run"}
now = lambda: datetime.datetime.now().isoformat(timespec="seconds")
def pdir(slug):
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{1,60}", slug): sys.exit("bad slug: use lowercase letters, digits, hyphens")
    return PROJECTS / slug
def load(p, default): return json.loads(p.read_text()) if p.exists() else default
def spent(d, gate=None):
    f = d / "production-log" / "generations.csv"
    if not f.exists(): return 0.0
    return sum(float(r["credits"]) for r in csv.DictReader(f.open()) if gate is None or r["gate"] == gate)
def cmd_new(a):
    d = pdir(a.slug)
    if d.exists(): sys.exit(f"exists, not overwritten: {d}")
    for s in STAGES: (d / s).mkdir(parents=True)
    (d/"production-log"/"project.json").write_text(json.dumps({"slug": a.slug, "created": now(), "client_contact_allowed": None, "spec_work": None}, indent=1))
    (d/"production-log"/"approvals.json").write_text("[]")
    print("created", d)
def cmd_approve(a):
    d = pdir(a.slug)
    if not d.exists(): sys.exit("no such project")
    if a.gate not in GATES: sys.exit(f"unknown gate; use one of {GATES}")
    if a.by != "owner": sys.exit("only the owner can approve (--by owner)")
    if len(a.quote.strip()) < 2: sys.exit("the owner's own words are required in --quote")
    if a.gate in PAID and a.ceiling is None: sys.exit("paid gates need --ceiling <credits>")
    if a.test and a.gate in PAID | {"purchase","publish","delivery"}: sys.exit("a test marker cannot be recorded on a paid, purchase, delivery or publish gate")
    f = d/"production-log"/"approvals.json"; L = load(f, [])
    L.append({"gate": a.gate, "by": a.by, "quote": a.quote, "ceiling": a.ceiling, "time": now(), "test": bool(a.test)})
    f.write_text(json.dumps(L, indent=1, ensure_ascii=False)); print("recorded", a.gate, "(TEST MARKER - not an approval)" if a.test else "")
def is_test(x): return bool(x.get("test")) or "SYSTEM TEST" in x.get("quote","").upper()
def latest(d, gate, allow_test=False):
    L = [x for x in load(d/"production-log"/"approvals.json", []) if x["gate"] == gate and (allow_test or not is_test(x))]
    return L[-1] if L else None
def cmd_check(a):
    d = pdir(a.slug); ap = latest(d, a.gate) if d.exists() else None
    if not ap:
        t = latest(d, a.gate, allow_test=True) if d.exists() else None
        print(f"BLOCKED: only a TEST MARKER exists for gate '{a.gate}' - not an owner approval" if t else f"BLOCKED: no owner approval recorded for gate '{a.gate}'"); sys.exit(1)
    if a.gate in PAID:
        s = spent(d, a.gate)
        if s >= ap["ceiling"]: print(f"BLOCKED: ceiling reached ({s:g} of {ap['ceiling']:g} credits) - new approval needed"); sys.exit(1)
        print(f"APPROVED: {a.gate}; spent {s:g} of {ap['ceiling']:g} credits" + (" - WARNING 80% used" if s >= 0.8*ap["ceiling"] else ""))
    else: print(f"APPROVED: {a.gate} at {ap['time']}")
def cmd_log(a):
    d = pdir(a.slug)
    if not latest(d, a.gate): sys.exit(f"refused: no approval for gate '{a.gate}' - this generation should not have run; report it to the owner")
    f = d/"production-log"/"generations.csv"; new = not f.exists()
    with f.open("a", newline="") as h:
        w = csv.writer(h)
        if new: w.writerow(["time","gate","shot","model","credits","job","file"])
        w.writerow([now(), a.gate, a.shot, a.model, a.credits, a.job, a.file])
    print("logged; total spent", spent(d))
def cmd_status(a):
    d = pdir(a.slug)
    for s in STAGES: print(f"{s:24} {len([x for x in (d/s).rglob('*') if x.is_file()])} files")
    for g in GATES:
        ap = latest(d, g); t = latest(d, g, allow_test=True); print(f"gate {g:12} {'APPROVED ' + ap['time'] if ap else ('test marker only' if t else '-')}")
    print("credits spent:", spent(d))
def fm(p):
    m = re.match(r"---\n(.*?)\n---\n", p.read_text(), re.S)
    return dict(re.findall(r"^(\w+):\s*(.*)$", m.group(1), re.M)) if m else None
def cmd_validate(a):
    errs = []; skills = {}
    for p in sorted((ROOT/".claude/skills").glob("*/SKILL.md")):
        f = fm(p); t = p.read_text(); n = p.parent.name
        if not f: errs.append(f"{n}: no frontmatter"); continue
        d = f.get("description","").strip('"'); skills[n] = d
        if f.get("name") != n: errs.append(f"{n}: name != folder")
        if not re.fullmatch(r"[a-z0-9-]{1,64}", n): errs.append(f"{n}: bad name")
        if not d or len(d) > 1024 or "<" in d or ">" in d: errs.append(f"{n}: bad description")
        if "Use when" not in d and "Use " not in d: errs.append(f"{n}: description has no activation condition")
        if "Not for" not in d: errs.append(f"{n}: description has no 'Not for'")
        for h in ["## Purpose","## Required inputs","## Workflow","## Expected outputs","## Quality checklist","never ruled out"]:
            if h not in t: errs.append(f"{n}: missing {h}")
        if t.count("\n") > 500: errs.append(f"{n}: over 500 lines")
        for tpl in re.findall(r"`templates/([\w.-]+)`", t):
            if not (ROOT/"advertising-studio/templates"/tpl).exists(): errs.append(f"{n}: missing template {tpl}")
    used = set(); agents = []
    for p in sorted((ROOT/".claude/agents").glob("*.md")):
        f = fm(p); n = p.stem; agents.append(n)
        if not f or f.get("name") != n: errs.append(f"agent {n}: bad frontmatter"); continue
        for k in ["description","tools","skills"]:
            if not f.get(k): errs.append(f"agent {n}: no {k}")
        for s in [x.strip() for x in f.get("skills","").split(",")]:
            used.add(s)
            if s not in skills: errs.append(f"agent {n}: unknown skill {s}")
        gen = "mcp__Higgsfield" in f.get("tools","")
        if gen and n != "ai-visual-production-director": errs.append(f"agent {n}: must not have generation tools")
    for n in agents:
        f = fm(ROOT/".claude/agents"/f"{n}.md")
        for sub in re.findall(r"Agent\(([^)]*)\)", f.get("tools","")):
            for s in [x.strip() for x in sub.split(",")]:
                if s not in agents: errs.append(f"agent {n}: delegates to unknown agent {s}")
    for s in skills:
        if s not in used: errs.append(f"skill {s}: not attached to any agent")
    ds = list(skills.values())
    for i in range(len(ds)):
        for j in range(i):
            A, B = set(ds[i].lower().split()), set(ds[j].lower().split())
            if len(A & B) / len(A | B) > 0.6: errs.append(f"descriptions too similar: {list(skills)[i]} / {list(skills)[j]}")
    print(f"{len(skills)} skills, {len(agents)} agents checked")
    print("VALID" if not errs else "\n".join(["INVALID"] + errs)); sys.exit(1 if errs else 0)
ap = argparse.ArgumentParser(); sp = ap.add_subparsers(dest="c", required=True)
x = sp.add_parser("new"); x.add_argument("slug"); x.set_defaults(f=cmd_new)
x = sp.add_parser("approve"); x.add_argument("slug"); x.add_argument("gate"); x.add_argument("--by", required=True); x.add_argument("--quote", required=True); x.add_argument("--ceiling", type=float); x.add_argument("--test", action="store_true", help="record a test marker for system tests; never counts as approval"); x.set_defaults(f=cmd_approve)
x = sp.add_parser("check"); x.add_argument("slug"); x.add_argument("gate"); x.set_defaults(f=cmd_check)
x = sp.add_parser("log"); x.add_argument("slug"); [x.add_argument(o, required=True) for o in ["--shot","--model","--job","--file"]]; x.add_argument("--credits", type=float, required=True); x.add_argument("--gate", default="paid-images"); x.set_defaults(f=cmd_log)
x = sp.add_parser("status"); x.add_argument("slug"); x.set_defaults(f=cmd_status)
x = sp.add_parser("validate"); x.set_defaults(f=cmd_validate)
a = ap.parse_args(); a.f(a)
