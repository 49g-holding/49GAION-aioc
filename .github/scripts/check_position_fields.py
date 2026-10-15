#!/usr/bin/env python3
"""position-fields (Position Principle, GOV 15 October 2026; non-required at first).
Light, pattern-based. Every field that points to a human seat (accountable_to, label_holder,
attached_to, signer_seat, seat) takes a position code only, never a person, and a decision
record's "Decided by" line names a seat, never a person.
On a pull request only the files it changes are read (BASE_SHA set); otherwise every tracked
text file. Frozen records are never edited, so they are read only when changed.
Allowed values: a placeholder <...>, none, empty, a HOAC label [ORG]HOAC-GOV|TM|ACS, or a code
of the form <prefix>AIOC-X, <prefix>POD-X or <prefix>CELL-X (prefix [ORG] or letters/digits)."""
import os, re, subprocess, sys
FIELDS = r"accountable_to|label_holder|attached_to|signer_seat|seat"
LINE = re.compile(r'["\']?\b(' + FIELDS + r')\b["\']?\s*[:=]\s*(.+)$')
CODE = re.compile(r'^(\[ORG\]|[0-9A-Za-z]+)(AIOC|POD|CELL|HOAC)-[A-Z0-9][A-Z0-9-]{0,15}$')
def ok(v):
    v = v.split("#", 1)[0].strip().rstrip(",").strip().strip('"\'').strip()
    if v in ("", "none", "null", "~", "{", "[") or v.startswith("<") or v.startswith("{") or v.startswith("[ORG]HOAC-"):
        return True
    if v.startswith("[") and not v.startswith("[ORG]"):
        return all(ok(x) for x in v.strip("[]").split(",") if x.strip())
    return bool(CODE.match(v))
def files():
    base = os.environ.get("BASE_SHA", "").strip()
    if base:
        out = subprocess.run(["git", "diff", "--name-only", "--diff-filter=AM", base + "...HEAD"], capture_output=True, text=True, check=True).stdout
    else:
        out = subprocess.run(["git", "ls-files"], capture_output=True, text=True, check=True).stdout
    return [f for f in out.split() if not f.startswith(".github/") and f.endswith((".md", ".yaml", ".yml", ".json"))]
bad = 0
for f in files():
    try:
        lines = open(f, encoding="utf-8").read().splitlines()
    except (OSError, UnicodeDecodeError):
        continue
    in_code = f.endswith((".yaml", ".yml", ".json"))
    for n, line in enumerate(lines, 1):
        s = line.strip()
        if s.startswith("```"):
            in_code = not in_code if f.endswith(".md") else in_code
            continue
        if in_code:
            m = LINE.search(s.lstrip("#").strip() if s.startswith("# ") and ":" in s else s)
            if m and not ok(m.group(2)):
                print(f"::error file={f},line={n}::{m.group(1)} must hold a position code, never a person: {m.group(2)[:60]}"); bad += 1
        if f.startswith("decisions/") and s.startswith("- **Decided by:**"):
            v = s.split("**Decided by:**", 1)[1]
            if not re.search(r"\bseat\b|HOAC-|(AIOC|POD|CELL)-", v):
                print(f"::error file={f},line={n}::Decided by must name a seat or position, never a person"); bad += 1
if bad:
    print(f"::error::{bad} human-pointing field(s) hold something other than a position code."); sys.exit(1)
print("position-fields: every human-pointing field holds a position code.")
