#!/usr/bin/env bash
# Must-pass and must-fail cases for check_arrangements.py (the Overseen link; DR-0049), run in a scratch repository.
# An identical copy sits in each repository that runs the check (excluded-types-parity compares them).
set -eu
script="$(cd "$(dirname "$0")/../scripts" && pwd)/check_arrangements.py"
t=$(mktemp -d); cd "$t"; git init -q; git config user.email t@t; git config user.name t
printf '{"entry":"position","position":"[ORG]CELL-QA"}\n' > p.json
git add -A; git commit -qm base; BASE_SHA=$(git rev-parse HEAD); export BASE_SHA
run() { git add -A >/dev/null; git commit -qm c --allow-empty >/dev/null; if python3 "$script" >/dev/null 2>&1; then echo pass; else echo fail; fi; }
expect() { [ "$(run)" = "$1" ] || { echo "FAIL $1 expected: $2"; exit 1; }; rm -f c.json c.yaml; }
printf '{"entry":"position","position":"[ORG]CELL-ENG","overseen":{"by":"[ORG]CELL-QA","timing":"pre"}}\n' > c.json
expect pass "a position overseen by a position declared in an unchanged file"
printf '{"entry":"position","position":"[ORG]CELL-ENG","overseen":{"by":"[ORG]HOAC-TM","timing":"post"}}\n' > c.json; expect pass "overseen by TM, post"
printf '{"entry":"position","position":"[ORG]CELL-ENG"}\n' > c.json; expect pass "a position with no Overseen link"
printf '{"arrangement":{"position":"[ORG]CELL-ENG","holders":2}}\n' > c.json; expect pass "a legacy arrangement: holders are no longer read (DR-0049)"
printf '{"decision_stamp":{"position":"[ORG]CELL-ENG"}}\n' > c.json; expect pass "a stamp with the position code only"
printf '{"arrangement":{"position":"[ORG]CELL-ENG","overseen":{"by":"[ORG]CELL-QA","timing":"pre"}}}\n' > c.json; expect pass "a legacy arrangement with a well-formed Overseen link"
printf '{"entry":"position","position":"[ORG]CELL-ENG","overseen":{"by":"[ORG]CELL-NONE","timing":"pre"}}\n' > c.json; expect fail "overseer not defined"
printf '{"entry":"position","position":"[ORG]CELL-ENG","overseen":{"by":"<anything>","timing":"pre"}}\n' > c.json; expect fail "overseer placeholder"
printf '{"entry":"position","position":"[ORG]CELL-ENG","overseen":{"by":"[ORG]HOAC-XYZ","timing":"pre"}}\n' > c.json; expect fail "undefined HOAC code"
printf '{"entry":"position","position":"[ORG]CELL-ENG","overseen":{"by":"[ORG]CELL-QA"}}\n' > c.json; expect fail "no timing form"
printf '{"entry":"position","position":"[ORG]HOAC-GOV","overseen":{"by":"[ORG]HOAC-TM","timing":"post"}}\n' > c.json; expect fail "GOV overseen by a lower position"
printf '{"entry":"position","position":"[ORG]CELL-ENG","overseen":"[ORG]CELL-QA"}\n' > c.json; expect fail "overseen not an object"
printf '{"arrangement":{"position":"[ORG]CELL-ENG","overseen":{"by":"[ORG]CELL-QA","timing":"later"}}}\n' > c.json; expect fail "legacy arrangement with a bad timing form"
printf '{"entry": {\n' > c.json; expect fail "unparseable JSON"
printf 'a: [1, 2\n' > c.yaml; expect fail "unparseable YAML"
echo "arrangements self-test: all cases behave as expected."
