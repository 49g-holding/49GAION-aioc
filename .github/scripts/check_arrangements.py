#!/usr/bin/env python3
"""position-fields, arrangement structure (GOV 15 October 2026; non-required at first).
Structure only; no model name is hard-coded. Positions that exist ("known") are the HOAC labels
[ORG]HOAC-GOV, [ORG]HOAC-TM and [ORG]HOAC-ACS plus every position declared in a tracked YAML or
JSON file (an object {"entry": "position", "position": CODE} or {"position": {"code": CODE}}).
The files checked are, on a pull request (BASE_SHA set), those it adds or changes; otherwise
every tracked file. Wherever a checked file has:
- an "arrangement" object: it names its "position"; its holder count ("holders": a number or a
  list) is at least 1; with more than one holder it records a non-empty "signing_rule";
- an "overseen" link in an arrangement: it is an object naming a known overseeing position
  ("by") and a timing form ("timing": pre or post); an arrangement for GOV (code ending in
  HOAC-GOV) with an overseen link is rejected, since every other position is lower;
- a "decision_stamp" object (an instance or a schema with "properties"): it carries the field
  "accountable_member". Whether that member is a current occupant is checked by the tool
  gateway at signing, not here.
A YAML or JSON file that cannot be parsed is an error; a missing PyYAML is an error.
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
            a = o.get("arrangement")
            if isinstance(a, dict):
                pos = a.get("position", o.get("position"))
                if isinstance(pos, dict): pos = pos.get("code")
                if not isinstance(pos, str) or not pos: err(f, "arrangement must name its position")
                h = a.get("holders")
                n = len(h) if isinstance(h, list) else h if isinstance(h, int) and not isinstance(h, bool) else None
                if n is None or n < 1: err(f, f"arrangement for {pos}: holder count must be at least 1")
                elif n > 1 and not str(a.get("signing_rule") or "").strip(): err(f, f"arrangement for {pos}: more than one holder needs a recorded signing_rule")
                ov = a.get("overseen")
                if ov is not None and not isinstance(ov, dict):
                    err(f, f"arrangement for {pos}: overseen must be an object")
                elif isinstance(ov, dict):
                    if ov.get("by") not in known: err(f, f"arrangement for {pos}: overseeing position {ov.get('by')!r} is not a defined position")
                    if ov.get("timing") not in ("pre", "post"): err(f, f"arrangement for {pos}: overseen needs timing pre or post")
                    if isinstance(pos, str) and pos.endswith("HOAC-GOV"): err(f, "GOV overseen by a lower position is rejected (no loops)")
            s = o.get("decision_stamp")
            if isinstance(s, dict):
                fields = s["properties"] if isinstance(s.get("properties"), dict) else s
                if "accountable_member" not in fields: err(f, "decision_stamp lacks the accountable_member field")
if bad:
    print(f"::error::{bad} arrangement structure problem(s)."); sys.exit(1)
print(f"position-fields: arrangement structure is complete ({len(check)} file(s) checked, {len(known)} known positions).")
