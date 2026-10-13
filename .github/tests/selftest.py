#!/usr/bin/env python3
"""ci-selftest (companion): must-fail and must-pass cases for the checks of this repository.
A must-fail case counts only when it fails on its own rule with the named error in the log."""
import os, pathlib, shutil, subprocess, sys, tempfile

ROOT = pathlib.Path(__file__).resolve().parents[2]
S = ROOT / ".github/scripts"
DEPS = os.environ.get("REF_DEPS", "")
results = []

def run(cwd, *a, env=None):
    return subprocess.run(list(a), cwd=cwd, capture_output=True, text=True, env={**os.environ, **(env or {})})

def expect(name, r, code=None):
    out = r.stdout + r.stderr
    ok = r.returncode == 0 if code is None else (r.returncode != 0 and code in out)
    results.append((name, ok))
    print(f"{'ok  ' if ok else 'FAIL'} {name}: expected {'exit 0' if code is None else 'failure with ' + code}")
    if not ok:
        print("    " + out.replace("\n", "\n    "))

# ref-check reads the escaped section sign \u00a7 in schema text
dirs = {"HUB_DIR": f"{DEPS}/hub", "PROTOCOL_DIR": f"{DEPS}/protocol", "AIOC_DIR": f"{DEPS}/aioc"}
for name, body, code in (("a valid escaped reference passes", "see Standard \\u00a74.4", None),
                         ("a broken escaped reference fails", "see Standard \\u00a799.9", "§99.9 does not exist")):
    d = pathlib.Path(tempfile.mkdtemp()) / "repo"
    shutil.copytree(ROOT, d, ignore=shutil.ignore_patterns(".git", ".deps"))
    run(d, "git", "init", "-q")
    (d / "probe.schema.json").write_text('{"description": "%s"}\n' % body)
    run(d, "git", "add", "-A")
    env = dict(dirs, BASE_SHA="")
    env[os.environ["SELF_DIR_VAR"]] = "."
    expect("ref-check: " + name, run(d, sys.executable, str(S / "check_refs.py"), env=env), code)

# template-fill (AIOC repository only)
if (S / "check_template_fill.py").exists():
    schema = f"{DEPS}/protocol/spec/schemas/unit-card.schema.json"
    import json
    v15 = "accountable_to" in json.load(open(schema))["properties"]  # the fixture matching the schema fetched
    fx = ROOT / f".github/tests/template-fill/complete-{'v1.5' if v15 else 'v1.4'}.md"
    expect("template-fill: a complete card block passes", run(ROOT, sys.executable, str(S / "check_template_fill.py"), str(fx), schema))
    for key in ("lifecycle_state", "full_name", "lineage"):
        t = pathlib.Path(tempfile.mkdtemp()) / "missing.md"
        t.write_text("\n".join(l for l in fx.read_text().splitlines() if not l.strip().startswith(key + ":")) + "\n")
        expect(f"template-fill: removing the required key {key} fails",
               run(ROOT, sys.executable, str(S / "check_template_fill.py"), str(t), schema), f"'{key}' is a required property")
    # Ratchet: a finding already on the base is a warning; a new finding fails.
    def drop(keys):
        t = pathlib.Path(tempfile.mkdtemp()) / "t.md"
        t.write_text("\n".join(l for l in fx.read_text().splitlines() if not any(l.strip().startswith(k + ":") for k in keys)) + "\n")
        return str(t)
    base1 = drop(["full_name"])
    expect("template-fill: a finding already on the base passes as a warning",
           run(ROOT, sys.executable, str(S / "check_template_fill.py"), drop(["full_name"]), schema, base1))
    expect("template-fill: a new finding beside one on the base fails",
           run(ROOT, sys.executable, str(S / "check_template_fill.py"), drop(["full_name", "lineage"]), schema, base1), "'lineage' is a required property")
    # Known list (as read from the base commit): listed findings are warnings, others fail; an empty list is strict.
    kl = pathlib.Path(tempfile.mkdtemp()) / "base.known.tsv"
    kl.write_text(run(ROOT, sys.executable, str(S / "check_template_fill.py"), "--list", drop(["full_name"]), schema).stdout)
    expect("template-fill: a finding on the base's known list passes as a warning",
           run(ROOT, sys.executable, str(S / "check_template_fill.py"), drop(["full_name"]), schema, str(kl)))
    expect("template-fill: a finding not on the base's known list fails",
           run(ROOT, sys.executable, str(S / "check_template_fill.py"), drop(["full_name", "lineage"]), schema, str(kl)), "'lineage' is a required property")
    empty = pathlib.Path(tempfile.mkdtemp()) / "empty.known.tsv"; empty.write_text("# empty\n")
    expect("template-fill: with an empty known list an old finding fails",
           run(ROOT, sys.executable, str(S / "check_template_fill.py"), drop(["full_name"]), schema, str(empty)), "'full_name' is a required property")

# ---------- person-names (fictional name; the real list is never used here) ----------
expect("person-names: selftest cases", subprocess.run([sys.executable, str(pathlib.Path(__file__).resolve().parent / "person_names_selftest.py")], capture_output=True, text=True))

bad = [n for n, ok in results if not ok]
print(f"\nci-selftest: {len(results) - len(bad)}/{len(results)} cases as expected")
if bad:
    print("::error::ci-selftest: cases not as expected: " + "; ".join(bad)); sys.exit(1)
