#!/usr/bin/env python3
"""template-fill: fill the machine-readable YAML blocks of the AIOC blueprint template
(§1 card and §17 Cells and Pods) with sample values and validate each against the unit card
schema of the 49GAION Operating Protocol (spec/schemas/unit-card.schema.json).

A placeholder "<a | b | c>" takes its first option; other placeholders take a sample value by
key (fictional codes such as TenAIOC-SL and TenCELL-TMS). Every block whose top key is card,
aioc, pod or cell is checked. A block that fails names the schema error (TEMPLATE-FILL).
Usage: check_template_fill.py <template.md> <unit-card.schema.json>"""
import json, re, sys
import yaml
from jsonschema import Draft202012Validator

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
        try:
            doc = yaml.safe_load(m.group(1))
        except yaml.YAMLError as e:
            yield md[:m.start()].count("\n") + 1, None, f"YAML error: {e}"
            continue
        if isinstance(doc, dict):
            for top in ("card", "aioc", "pod", "cell"):
                if top in doc:
                    yield md[:m.start()].count("\n") + 1, top, doc[top]

def main(tpl, schema_path):
    schema = json.load(open(schema_path, encoding="utf-8"))
    val = Draft202012Validator(schema)
    md = open(tpl, encoding="utf-8").read()
    n, bad = 0, 0
    for line, top, doc in blocks(md):
        if top is None:
            print(f"::error::TEMPLATE-FILL {tpl}:{line}: {doc}"); bad += 1; continue
        n += 1
        kind = str(doc.get("unit_kind", top.upper())) if isinstance(doc, dict) else top.upper()
        filled = fill(doc, kind if kind in ("AIOC", "POD", "CELL") else "AIOC")
        errs = sorted(val.iter_errors(filled), key=lambda e: list(e.path))
        for e in errs:
            print(f"::error::TEMPLATE-FILL {tpl}:{line} ({top}): {'/'.join(map(str, e.path)) or '(card)'}: {e.message}")
        bad += bool(errs)
        print(f"{tpl}:{line} {top}: {'FAIL' if errs else 'valid'}")
    if n == 0:
        print(f"::error::TEMPLATE-FILL {tpl}: no card blocks found"); sys.exit(1)
    if bad:
        print(f"::error::template-fill: {bad} of {n} filled blocks do not validate against the unit card schema."); sys.exit(1)
    print(f"template-fill: {n} filled blocks validate")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
