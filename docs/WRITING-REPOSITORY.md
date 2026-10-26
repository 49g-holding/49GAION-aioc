# The writing repository of an AIOC

What every AIOC's writing repository holds, and the checks it runs. Drawn from the writing repositories of the design stages of the Library, which share this layout and these checks.

Sources: DR-0019, DR-0021; GOV, 16 October 2026.

## What it holds

| Path | Holds |
|---|---|
| `blueprint/<CODE>-BLUEPRINT.md` | the blueprint, on the template of this repository; it governs everything generated from it |
| `tests/` | the fixed test, written before use, with the Library part's cases kept and mapped (template §9) |
| `contracts/` | the machine contracts the AIOC owns, each with valid and must-fail examples, and `PINS.json`: every outside text it reads, pinned by version, commit and SHA-256 (for example the Library's contracts and the Human Floor signature list) |
| `cards/` | the unit cards of its Pods and Cells and the bot identity cards of its AI Cells, generated from template §17, never written by hand |
| `tools/` | the code that generates the cards and checks the contracts |
| `docs/` | what the blueprint states only in short, and the record of why each rule is there |
| `decisions/` | the decision records of the repository, one file per subject, never edited once merged, with an index that holds their status |
| `upstream/` | drafts proposed to 49GAION or to other AIOCs, each with its state |
| `README.md`, `STATE.md`, `CHANGELOG.md` | what it is in one page; where it stands, with the result of every check and its date; one row per version |

## The checks, on every pull request and on main

1. **Cards.** The cards in `cards/` are exactly what the tool generates from the blueprint, and they validate against the schemas of `49GAION-protocol`.
2. **Contracts.** Every valid example validates; every must-fail example is refused at the place its reason names; every pinned outside text is read at its pinned commit and has its pinned SHA-256.
3. **Names.** No organisation's name, host or code in a repository that is public (Naming Standard R9), checked by the scanner of `49GAION-protocol`.
4. **Language.** Any rule the organisation sets for the language of its shared texts.

A reference workflow for checks 1 to 3 is `template/writing-repository-checks.yml`.

## Where it lives and who sees it

The writing repository is recorded before it is created, with its name, its visibility and its platform (Naming Standard R9). It may be public only when it holds no organisation's data; its `-records` and `-records-restricted` repositories are never public. Where it also holds a Library mother blueprint, the Library register pins it.

Powered by 49GAION
