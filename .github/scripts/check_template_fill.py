#!/usr/bin/env python3
"""template-fill: fill the machine-readable YAML blocks of the AIOC blueprint template
(§1 card and §17 Cells and Pods) with sample values and validate each against the unit card
schema of the 49GAION Operating Protocol (spec/schemas/unit-card.schema.json).

A placeholder "<a | b | c>" takes its first option; other placeholders take a sample value by
key (fictional codes such as TenAIOC-SL and TenCELL-TMS). Every block whose top key is card,
aioc, pod or cell is checked, except a block whose preceding line starts with "Superseded". A block that fails names the schema error (TEMPLATE-FILL).
Usage: check_template_fill.py <template.md> <unit-card.schema.json>"""
import json, os, re, sys
import yaml
import pathlib
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

SAMPLE = {
    "code": {"AIOC": "TenAIOC-SL", "POD": "TenPOD-RV", "CELL": "TenCELL-SLCS"},
    "parent": {"AIOC": "TenAIOC-CH", "POD": "TenAIOC-SL", "CELL": "TenAIOC-SL"},
    "accountable_to": "TenCELL-TMS", "top_cell": "TenCELL-SLCS", "attached_to": "TenCELL-TMS",
    "hoac": "TenHOAC-ACS", "org_aion": "Ten AION", "organisation": "Ten",
    "label_holder": "TenCELL-TMS", "owner": "TenCELL-TMS", "entity": "Ten Holding",
}

def first_option(s):
    inner = s.strip()[1:-1]
    return inner.split("|")[0].strip() if "|" in inner else None

def fill(o, kind, key=None):
    if isinstance(o, dict):
        return {k: fill(v, kind, k) for k, v in o.items()}
    if isinstance(o, list):
        return [fill(v, kind, key) for v in o]
    if isinstance(o, str) and re.fullmatch(r"\s*<[^<>]*>\s*", o):
        opt = first_option(o)
        if opt:
            return opt
        v = SAMPLE.get(key)
        if isinstance(v, dict):
            return v[kind]
        if v:
            return v
        if re.search(r"vN", o):
            return "v1.0.0" if "N.N" in o else "v1"
        if "N.N.N" in o:
            return "1.0.0"
        if key in ("inner_units", "usual_receivers"):
            return SAMPLE["code"]["CELL"]
        return "sample"
    return o

def blocks(md):
    for m in re.finditer(r"```yaml\n(.*?)```", md, re.S):
        before = md[:m.start()].rstrip().splitlines()[-1:] or [""]
        if before[0].lstrip("> ").startswith("Superseded"):
            continue  # a block kept as written under a superseded label is read, never filled
        try:
            doc = yaml.safe_load(m.group(1))
        except yaml.YAMLError as e:
            yield md[:m.start()].count("\n") + 1, None, f"YAML error: {e}"
            continue
        if isinstance(doc, dict):
            for top in ("card", "aioc", "pod", "cell"):
                if top in doc:
                    yield md[:m.start()].count("\n") + 1, top, doc[top]

def errors(tpl, val):
    """(line, block, [(path, message)]) for every card block of a template, after filling."""
    md = open(tpl, encoding="utf-8").read()
    out = []
    for line, top, doc in blocks(md):
        if top is None:
            out.append((line, None, [("(yaml)", str(doc))])); continue
        kind = str(doc.get("unit_kind", top.upper())) if isinstance(doc, dict) else top.upper()
        filled = fill(doc, kind if kind in ("AIOC", "POD", "CELL") else "AIOC")
        errs = sorted(val.iter_errors(filled), key=lambda e: list(e.path))
        out.append((line, top, [("/".join(map(str, e.path)) or "(card)", e.message) for e in errs]))
    return out

def main(tpl, schema_path, baseline=None):
    """Validate every filled card block. With a baseline (the same template at the base commit),
    a finding the baseline already has is reported as a warning: a change may not add a
    finding, and once the base is clean every finding fails."""
    schema = json.load(open(schema_path, encoding="utf-8"))
    sib = {p.name: json.loads(p.read_text(encoding="utf-8")) for p in pathlib.Path(schema_path).parent.glob("*.schema.json")}
    reg = Registry().with_resources([(n, Resource.from_contents(x)) for n, x in sib.items()] +
                                    [(x["$id"], Resource.from_contents(x)) for x in sib.values() if "$id" in x])
    val = Draft202012Validator(schema, registry=reg)  # sibling schemas (for example the Port card) resolve locally
    known = set()
    if baseline and os.path.exists(baseline):
        if baseline.endswith(".known.tsv"):
            # The known-warning list as it stands on the base commit (never the pull request's copy).
            for ln in open(baseline, encoding="utf-8").read().splitlines():
                if ln.strip() and not ln.startswith("#"):
                    top, path, msg = ln.split("\t", 2); known.add((top, path, msg))
        else:
            known = {(top, path, msg) for _, top, errs in errors(baseline, val) for path, msg in errs}
    res = errors(tpl, val)
    n, bad, old = 0, 0, 0
    for line, top, errs in res:
        if top is not None: n += 1
        new_errs = [(p, m) for p, m in errs if (top, p, m) not in known]
        for p, m in errs:
            if (p, m) in new_errs:
                print(f"::error::TEMPLATE-FILL {tpl}:{line} ({top}): {p}: {m}")
            else:
                print(f"::warning::TEMPLATE-FILL-KNOWN {tpl}:{line} ({top}): {p}: {m} (on the base commit's known list)"); old += 1
        bad += bool(new_errs)
        print(f"{tpl}:{line} {top}: {'FAIL' if new_errs else 'valid' if not errs else 'existing findings only'}")
    if n == 0:
        print(f"::error::TEMPLATE-FILL {tpl}: no card blocks found"); sys.exit(1)
    if bad:
        print(f"::error::template-fill: {bad} of {n} filled blocks add findings against the unit card schema."); sys.exit(1)
    print(f"template-fill: {n} filled blocks add no finding" + (f" ({old} existing on the base, reported as warnings)" if old else "; all validate"))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--list":
        # Print the known-warning list for a template: block, path and message, one per line.
        v = Draft202012Validator(json.load(open(sys.argv[3])), registry=Registry().with_resources(
            [(q.name, Resource.from_contents(json.loads(q.read_text()))) for q in pathlib.Path(sys.argv[3]).parent.glob("*.schema.json")]))
        for _, top, errs in errors(sys.argv[2], v):
            for path, msg in errs: print(f"{top}\t{path}\t{msg}")
        sys.exit(0)
    main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
