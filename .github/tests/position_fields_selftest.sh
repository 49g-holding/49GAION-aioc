#!/usr/bin/env bash
# Must-fail and must-pass cases for check_position_fields.py, run in a scratch repository.
set -eu
script="$(cd "$(dirname "$0")/../scripts" && pwd)/check_position_fields.py"
t=$(mktemp -d); cd "$t"; git init -q; mkdir decisions
run() { git add -A >/dev/null; if python3 "$script" >/dev/null 2>&1; then echo pass; else echo fail; fi; }
printf 'cell:\n  accountable_to: "[ORG]CELL-GOV"\n  label_holder: "<code of the human Cell>"\n  attached_to: "TenCELL-TMS"\n' > a.yaml
printf -- '- **Decided by:** the governing seat (GOV)\n' > decisions/DR-9999-x.md
[ "$(run)" = pass ] || { echo "FAIL must-pass: position codes"; exit 1; }
printf 'cell:\n  accountable_to: "Jane Example"\n' > b.yaml
[ "$(run)" = fail ] || { echo "FAIL must-fail: a name in accountable_to"; exit 1; }
rm b.yaml; printf -- '- **Decided by:** Jane Example\n' > decisions/DR-9998-y.md
[ "$(run)" = fail ] || { echo "FAIL must-fail: a name in Decided by"; exit 1; }
echo "position-fields self-test: all cases behave as expected."
