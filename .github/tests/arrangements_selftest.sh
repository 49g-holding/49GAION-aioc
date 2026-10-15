#!/usr/bin/env bash
# Must-pass and must-fail cases for check_arrangements.py, run in a scratch repository.
# An identical copy sits in each repository that runs the check (excluded-types-parity compares them).
set -eu
script="$(cd "$(dirname "$0")/../scripts" && pwd)/check_arrangements.py"
t=$(mktemp -d); cd "$t"; git init -q; git config user.email t@t; git config user.name t
printf '{"entry":"position","position":"[ORG]CELL-QA"}\n' > p.json
git add -A; git commit -qm base; BASE_SHA=$(git rev-parse HEAD); export BASE_SHA
run() { git add -A >/dev/null; git commit -qm c --allow-empty >/dev/null; if python3 "$script" >/dev/null 2>&1; then echo pass; else echo fail; fi; }
expect() { [ "$(run)" = "$1" ] || { echo "FAIL $1 expected: $2"; exit 1; }; rm -f c.json c.yaml; }
printf '{"arrangement":{"position":"[ORG]CELL-ENG","holders":3,"signing_rule":"majority","overseen":{"by":"[ORG]CELL-QA","timing":"pre"}},"decision_stamp":{"properties":{"accountable_member":{}}}}\n' > c.json
expect pass "complete arrangement; overseer declared in an unchanged file"
printf '{"arrangement":{"position":"[ORG]CELL-ENG","holders":1}}\n' > c.json; expect pass "Solo: one holder, no signing rule"
printf '{"arrangement":{"position":"[ORG]CELL-ENG","holders":1,"overseen":{"by":"[ORG]HOAC-TM","timing":"post"}}}\n' > c.json; expect pass "overseen by TM"
printf '{"arrangement":{"position":"[ORG]CELL-ENG","holders":0}}\n' > c.json; expect fail "zero holders"
printf '{"arrangement":{"position":"[ORG]CELL-ENG","holders":2}}\n' > c.json; expect fail "two holders, no signing rule"
printf '{"decision_stamp":{"position":"x","occupants":[]}}\n' > c.json; expect fail "stamp without accountable member"
printf '{"arrangement":{"position":"[ORG]CELL-ENG","holders":1,"overseen":{"by":"[ORG]CELL-NONE","timing":"pre"}}}\n' > c.json; expect fail "overseer not defined"
printf '{"arrangement":{"position":"[ORG]CELL-ENG","holders":1,"overseen":{"by":"<anything>","timing":"pre"}}}\n' > c.json; expect fail "overseer placeholder"
printf '{"arrangement":{"position":"[ORG]CELL-ENG","holders":1,"overseen":{"by":"[ORG]HOAC-XYZ","timing":"pre"}}}\n' > c.json; expect fail "undefined HOAC code"
printf '{"arrangement":{"position":"[ORG]CELL-ENG","holders":1,"overseen":{"by":"[ORG]CELL-QA"}}}\n' > c.json; expect fail "no timing form"
printf '{"arrangement":{"position":"[ORG]HOAC-GOV","holders":1,"overseen":{"by":"[ORG]HOAC-TM","timing":"post"}}}\n' > c.json; expect fail "GOV overseen by a lower position"
printf '{"arrangement":{"position":"[ORG]CELL-ENG","holders":1,"overseen":"[ORG]CELL-QA"},"decision_stamp":{"position":"x"}}\n' > c.json; expect fail "overseen not an object, stamp still checked"
printf '{"arrangement": {\n' > c.json; expect fail "unparseable JSON"
printf 'a: [1, 2\n' > c.yaml; expect fail "unparseable YAML"
echo "arrangements self-test: all cases behave as expected."
