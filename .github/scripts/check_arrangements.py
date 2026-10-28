#!/usr/bin/env python3
"""position-fields, the Overseen link (GOV 15 October 2026; DR-0049, 28 October 2026).
Structure only. Since DR-0049 who holds a position, how many hold it and how they decide among
themselves are the organisation's own mechanism, outside the system: this check no longer asks for
a holder count, a signing rule or an accountable member, and never reads a person. It checks only
the Overseen link, which stays as a link between positions.
Positions that exist ("known") are the HOAC labels [ORG]HOAC-GOV, [ORG]HOAC-TM and [ORG]HOAC-ACS
plus every position declared in a tracked YAML or JSON file (an object {"entry": "position",
"position": CODE} or {"position": {"code": CODE}}). The files checked are, on a pull request
(BASE_SHA set), those it adds or changes; otherwise every tracked file. Wherever a checked file
has an "overseen" link (on its own, or inside a legacy "arrangement" object), it must be an object
naming a known overseeing position ("by") and a timing form ("timing": pre or post); a GOV
position (code ending in HOAC-GOV) that is overseen is rejected, since every other position is
lower. A YAML or JSON file that cannot be parsed is an error; a missing PyYAML is an error.
Self-test: .github/tests/arrangements_selftest.sh."""
import json, os, subprocess, sys
try:
    import yaml
except ImportError:
    print("::error::PyYAML is not installed; the arrangement check cannot read YAML."); sys.exit(1)
EXT = (".yaml", ".yml", ".json")
def git_files(*args):
    out = subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout
    return [f for f in out.split("\n") if f and not f.startswith(".github/") and f.endswith(EXT)]
def changed():
    base = os.environ.get("BASE_SHA", "").strip()
    if base:
        return git_files("diff", "--name-only", "--diff-filter=AM", base + "...HEAD")
    return git_files("ls-files")
bad = 0
def err(f, msg):
    global bad
    print(f"::error file={f}::{msg}"); bad += 1
cache = {}
def load(f, report):
    if f not in cache:
        try:
            text = open(f, encoding="utf-8").read()
            cache[f] = [json.loads(text)] if f.endswith(".json") else list(yaml.safe_load_all(text))
        except Exception as e:
            cache[f] = None
            if report: err(f, f"cannot be parsed: {type(e).__name__}")
    return cache[f] or []
def walk(o):
    if isinstance(o, dict):
        yield o
        for v in o.values(): yield from walk(v)
    elif isinstance(o, list):
        for v in o: yield from walk(v)
check = changed()
known = {"[ORG]HOAC-GOV", "[ORG]HOAC-TM", "[ORG]HOAC-ACS"}
for f in git_files("ls-files"):
    for d in load(f, f in check):
        for o in walk(d):
            p = o.get("position")
            if isinstance(p, dict) and isinstance(p.get("code"), str): known.add(p["code"])
            elif isinstance(p, str) and o.get("entry") == "position": known.add(p)
for f in check:
    if f in cache and cache[f] is None: continue
    for d in load(f, True):
        for o in walk(d):
            if "overseen" not in o: continue
            for pos, ov in [(o.get("position", o.get("code")), o.get("overseen"))]:
                if isinstance(pos, dict): pos = pos.get("code")
                if not isinstance(ov, dict):
                    err(f, f"overseen link of {pos}: it must be an object"); continue
                if ov.get("by") not in known: err(f, f"overseen link of {pos}: overseeing position {ov.get('by')!r} is not a defined position")
                if ov.get("timing") not in ("pre", "post"): err(f, f"overseen link of {pos}: timing must be pre or post")
                if isinstance(pos, str) and pos.endswith("HOAC-GOV"): err(f, "GOV overseen by a lower position is rejected (no loops)")
if bad:
    print(f"::error::{bad} Overseen link problem(s)."); sys.exit(1)
print(f"position-fields: every Overseen link is well formed ({len(check)} file(s) checked, {len(known)} known positions).")
