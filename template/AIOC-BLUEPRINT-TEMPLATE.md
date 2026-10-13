```yaml
# ── Blueprint metadata (machine-readable; the panel generator and the back-office builder read this block) ──
blueprint:
  aioc: "<[ORG]AIOC-INITIALS>"            # e.g. [ORG]AIOC-SL or TenAIOC-SL. Only cores carry a [ORG]AIOC code; it never changes when the AIOC moves.
  parent: "<code of the unit that holds this AIOC, or none>"   # e.g. [ORG]AIOC-OCO; its place, never part of its code
  full_name: "<Full name>"                # e.g. Organization Core Office
  organisation: "<organisation>"          # e.g. Ten
  type: "<foundational | structural | specialised | connector | other>"   # why the AIOC exists; a card field, never part of the name
  org_aion: "<[ORG]AION>"                # the [ORG]AION this AIOC belongs to, e.g. TenAION
  blueprint_version: "<vN.N.N>"
  status: "<draft | in force | replaced>"
  template:
    name: "49GAION AIOC Blueprint Template"
    version: "v1.3.0"
    source: "github.com/49g-holding/49GAION-aioc, template/AIOC-BLUEPRINT-TEMPLATE.md @ <commit>"
  mother:
    name: "<Library blueprint name>, or none yet"
    version: "<version>, or none"
    source: "<location>, or none"
  writing_repository: "<org>aioc-<abbr>"
  code_project: "<code project path>, or none"
  panel_register_id: "<panel register id, or none>"
  capabilities:                           # plain English names only; no codes, no [ORG]AIOC prefix
    standard: ["Chief of Staff", "Office", "Input socket", "Panel"]   # Office only where a position needs more than one Chief of Staff
    functional: ["<name>", "<name>"]
```

# Blueprint · `<[ORG]AIOC-INITIALS>` · `<Full name>` · `<blueprint version>`

**The 49GAION AIOC Blueprint Template, `v1.3.0`.** Blank: every field is a placeholder; it holds no AIOC's content.

> **What this file is.** This is the one git file that defines an AIOC. It is its blueprint and its panel definition. It lists **every capability** the AIOC has, and each capability is written in **four parts: Definition, Process (SOP), Role card, Fixed test**. The AIOC's Panel and its Back office are both **built from this one file**. A change to the AIOC is a **tested git commit** to this file; the Panel then rebuilds from that commit, so the blueprint never drifts from what runs (`docs/WHAT-IS-AN-AIOC.md` §2).
>
> **How to fill it.**
> 1. Copy this file into the AIOC's writing repository as `blueprint/<AIOC>-BLUEPRINT.md`. Record in the metadata block the **template version and the commit** it was copied from (each AIOC records this in its own repository; `49GAION-aioc` keeps no copy of any AIOC's blueprint), and the **mother blueprint and version** it was customised from, or "none yet".
> 2. Fill every field. If a field does not apply, write "none" and say why.
> 3. Keep the **standard capabilities** (§4). Adopt their default definitions (`docs/STANDARD-CAPABILITIES.md`) unless the AIOC differs, and record each difference in §11.
> 4. Add one **functional capability** per function the AIOC performs (§5), each in the four parts.
> 5. Write for any organisation where you can; the organisation's own names go in the organisation table (§2).
> 6. Write positions, never people. A person's name appears only in the holders register.
> 7. Cite every rule to its source by ID and version. Never invent a fact, a version, a score or an appointment. `NOT_RUN` is never PASS.
> 8. **Names.** Capabilities have plain, recognisable English names — Chief of Staff, Office, Input socket, Panel, and the AIOC's own (for example Service Desk). They carry **no code and no branding**. Branded names exist only at the 49GAION level: `49GAION` for the framework, `[ORG]AION` for its product, `[ORG]AIOC-…` for cores (hub `standards/49GAION-NAMING-STANDARD.md`). The retired codes listed there are never used.

---

## 0. Identity and lineage

| Field | Value |
|---|---|
| Code | `<[ORG]AIOC-INITIALS>`, checked for collisions (Naming Standard §5) |
| Full name | `<Full name>`, written beside the code once |
| Description | "`<code>` is `<organisation>`'s `<full name>` core, built from `<Library blueprint name>`" |
| Kind | AIOC |
| Parent | the code of the unit that holds this AIOC, or `none` (Naming Standard R14); a change needs the approval of the human seat over this AIOC |
| Inner units | the codes of the AIOCs this AIOC holds, each linked to its own card and Blueprint, and of its own Pods and Cells (§17), or "none" (Standard §1.7) |
| HOAC label | the HOAC label this AIOC carries as a whole, if any (`[ORG]HOAC-GOV`, `[ORG]HOAC-TM` or `[ORG]HOAC-ACS`) |
| Type | `<Foundational / Structural / Specialised / Connector / other (described)>`: why this AIOC exists (`docs/WHAT-IS-AN-AIOC.md` §4). |
| `[ORG]AION` | `<[ORG]AION>`, based on 49GAION Standard `<version>` |
| Versioned Definition | this file, at `<commit>`; the Panel and the Back office are built from it |
| Organisation | `<organisation>` |
| Made from | the Library blueprint `<name>` `<version>`, or "none" |
| Template | 49GAION AIOC Blueprint Template `<version>` at `<commit>` |
| Mother | `<name, version>`, or "none yet" |
| Blueprint version and status | `<vN.N.N>` · `<draft / in force / replaced>` |
| Accountable seat (`[ORG]HOAC-ACS`) | the seat (holder in the unit register only) |
| Reports to | the position or office above it |
| Writing repository | `<org>aioc-<abbr>` (+ `-records`, `-records-restricted`) |
| Code project | its code project, or "none" |
| Panel | its panel's name and register id, or "not yet built" |
| Back office | its Back office workspace, and the commit it was last built from |
| Attribution | Powered by 49GAION |

---

## 1. Card (49GAION Operating Protocol §4)

The card declares what this AIOC receives, what it delivers, and in what format. It is the only card for this AIOC; the protocol AIOC's map reads it from here. It follows `spec/schemas/unit-card.schema.json` in `49g-holding/49GAION-protocol`.

```yaml
card:
  unit_kind: "AIOC"
  code: "<code>"
  parent: "<code of the holding unit, or none>"
  inner_units: ["<code>"]                 # by link; empty if none
  type: "<foundational | structural | specialised | connector | other>"   # required; if other, add type_description
  org_aion: "<[ORG]AION>"
  card_version: "<vN.N.N>"
  input_door: "Chief of Staff"            # always; the AIOC's voice to its HOAC seat (input arrives only through the typed ports and the Input socket)
  wake: { method: "queue", verified: false }   # runtime woken from its queue
  receives:
    - kind: "<a kind of work>"
      format: "<format>"
      acceptance_test: "<test ID and version>"
      decision_needed: false
  delivers:
    - kind: "<a kind of output>"
      format: "<format>"
      usual_receivers: ["<AIOC>"]
  anatomy:
    panel: { health: { tests: true, metrics: ["stuck", "returned", "late"] } }
    back_office: { converses_with_humans: true, hosts: ["Chief of Staff", "Office"], protocol_traffic: true }
    definition: { location: "<repository and path of this file>", version: "<commit or version>" }
    delivery: { rollback: "one-click" }
    connectors:
      - { role: "<tool role, e.g. task tracking>", connector: "<connector id>", access_managed_in: "panel" }
    gateway: { metering_id: "<per-AIOC metering id on the shared AI gateway>" }
```

**Joining the protocol.** This AIOC joins the 49GAION Operating Protocol only after every input and output claimed on this card passes fixed samples. A claim that fails is removed from the card. Until then the card is marked `joined: false` and no Work Item is routed to it.

---

## 2. Organisation table and placement

### 2.1 Organisation table
The design uses general terms; this table says what each term is in this organisation.

| Term in the blueprint | In `<organisation>` |
|---|---|
| The Top Office (the only centre of decision) | |
| **`[ORG]AIOC-OCO`** (every `[ORG]HOAC-ACS` request about this unit's AIs goes to it) | |
| The engineering division | |
| The IT and infrastructure division | |
| The builder of every tool | |
| The Library blueprint this core is made from | |

### 2.2 Placement
- **Where it sits:** under whom, beside whom.
- **Its role:** one sentence.
- **Scope:** what it does; what it does not do.
- **Companies it serves:** all, or which.
- **Boundaries with other AIOCs:** each boundary, and who holds what on the other side.
- **Overlap:** each overlap with an existing AIOC and how it is resolved.

---

## 3. Positions

Every unit has one accountable `[ORG]HOAC-ACS` seat, held by a human (Standard §4.1, §4.2, item 6). Holders are never named here.

| Position (standard title) | Purpose | Reports to | Run today by | Deputy |
|---|---|---|---|---|
| | | | an agent / a person (holders register) | |

Each position's role pack (job description, responsibilities, limits, permissions, checklists, KPIs, coverage, handover, first week) is carried in the role cards of the capabilities it performs.

---

## 4. Standard capabilities

Every AIOC has these: Chief of Staff, Input socket and Panel, and an Office where a position needs more than one Chief of Staff. Their **default definitions** are in `docs/STANDARD-CAPABILITIES.md` (49GAION level). Write "default" in a part to adopt the default text unchanged, or write this AIOC's own text and list the difference in §11.

### 4.1 Office
#### Definition
`<default | this AIOC's text>` · form: `<single Chief of Staff | Office of several Chiefs of Staff>`
#### Process (SOP)
`<default | this AIOC's text>`
#### Role card
`<one card per Chief of Staff in the Office, Annex A.3 fields>`
#### Fixed test
`<test ID and version>` · result `NOT_RUN`

### 4.2 Chief of Staff
#### Definition
`<default | this AIOC's text>` · it is this AIOC's voice to its HOAC seat; input arrives only through the typed ports and the Input socket
#### Process (SOP)
`<default | this AIOC's text>`
#### Role card
`<Annex A.3 fields>`
#### Fixed test
`<test ID and version>` · result `NOT_RUN`

### 4.3 Input socket
#### Definition
`<default | this AIOC's text>` · this AIOC's standard format: `<format>`
#### Process (SOP)
`<default | this AIOC's text>` · converters: `<one per input type, each with its test>`
#### Role card
`<Annex A.3 fields>`
#### Fixed test
`<one test per converter + the shared mechanism test>` · result `NOT_RUN`

### 4.4 Panel
#### Definition
`<default | this AIOC's text>`
#### Process (SOP)
`<default | this AIOC's text>`
#### Role card
`<Annex A.3 fields>`
#### Fixed test
`<test ID and version>` · result `NOT_RUN`

---

## 5. Functional capabilities

One block per function the AIOC performs. Use the **four-part capability form** (Annex A). Name each capability by a plain English name, with no code.

### 5.N `<Capability name>`
#### Definition
#### Process (SOP)
#### Role card
#### Fixed test

---

## 6. Coordination and routes
- **Whom it works with**, and the route to each: always through the 49GAION Operating Protocol (one Work Item per hand-off; this AIOC's Chief of Staff as its door).
- **Routing rows this AIOC contributes** to the routing table of its `[ORG]AION`.
- **Requests and objections.** Owners do not design or change this AIOC's AIs: every proposal, correction or critique is a `design-proposal` Work Item to **OCO**; where they disagree, the `[ORG]HOAC-ACS` seat may hold the objection open until it reaches the HOAC seat accountable for OCO, which decides.

## 7. Records and where things live
| Record | Home | Source rule |
|---|---|---|
| Writing, decisions, registers | its writing repository `<org>aioc-<abbr>` (+ `-records`) | one home for each thing |
| Code that runs | the code platform named in the `[ORG]AION`, if any | one home for each thing |
| Work Items | the shared queue | 49GAION Operating Protocol §2 |

## 8. Tools and the shared AI gateway
| Tool | Existing shared tool, or new | If new: asked of the builder as |
|---|---|---|
| | | |

All model calls go through the **shared AI gateway** at the 49GAION level (keys, cost and logs in one place).

**Connectors and metering.** Each tool is reached through a **swappable connector**, recorded by tool **role**; access is granted and withdrawn in the Panel. This AIOC's AI usage and cost are **metered separately** on the shared AI gateway; its **budget cap** is set in §15. A new tool enters only by a sourced proposal, a side-by-side test against the current tool and an update of the part's card.

| Tool role | Connector | Access managed in | Part card version |
|---|---|---|---|
| | | Panel | |

## 9. Fixed tests: index, triggers and scores
| Capability | Test ID and version | Evidence level | Last run | Result |
|---|---|---|---|---|
| Office | | | — | `NOT_RUN` |
| Chief of Staff | | | — | `NOT_RUN` |
| Input socket | | | — | `NOT_RUN` |
| Panel | | | — | `NOT_RUN` |

- **Re-run triggers:** any change to a model, instructions, this AIOC's card, this blueprint or the 49GAION Operating Protocol re-runs the affected tests automatically; also any change to tools or access, an Input socket converter or the AIOC's standard format, or any shared panel part.
- **Evidence levels:** `MEASURED_IN_BUILD_ENVIRONMENT` ranks above `OWNER_ATTESTED`; only a measured score counts toward widening authority (the owner requests with the score attached; the `[ORG]HOAC-ACS` seat decides and OCO prepares, checks and carries out).
- **Complete** only when every capability's test has a visible result.

## 10. Build: what is generated from this file
| Built thing | Generated from | Recorded where |
|---|---|---|
| Panel profile | §0, §1, §3, §4.4, §5 role cards | the panel profile and the Panel's release record name this file's commit |
| Back office | §4.2 role card and SOP (instruction); §4–§5 definitions and SOPs (knowledge) | the back office records the commit it was built or installed from |
| Card in the protocol AIOC's map | §1 | The protocol AIOC's register links this file |
| Panel Health section | §9 test results; stuck, returned and late Work Items | the Panel |

**Delivery path:** definition change → tests → Panel and Back office update → **one-click rollback** to the previous commit. Both the Panel and the Back office can be rebuilt from any commit of this file.

## 11. Exceptions
Anything in which this AIOC differs from the template defaults, and why.

## 12. Lessons and proposals to the mother
One dated line per lesson, each with the test question it added and whether it was proposed to the mother (written without the organisation's details).

## 13. For the `[ORG]HOAC-ACS` seat
What the `[ORG]HOAC-ACS` seat is asked to decide. Money, people and legal matters are listed here so they are seen.

## 14. Change log
| Blueprint version | Date | Change | Template version | Commit |
|---|---|---|---|---|

---

## 15. Configuration
49GAION fixes the path; who holds each role is configured here (`docs/WHAT-IS-AN-AIOC.md` §5). Every slot is filled by this organisation or unit; **an AIOC with any empty slot does not pass the joining test** (Protocol §11). Each value records who set it, when, and in which version; a changed value records what it replaced.

| Slot | Value | Default offered by 49GAION | Set by | Date | Version | Replaces |
|---|---|---|---|---|---|---|
| HOAC seat accountable for OCO (decides objections held open; Protocol §4.7) | | none: must be set | | | | |
| OCO of this `[ORG]AION` (receives `[ORG]HOAC-ACS` requests and carries out approved blueprint changes) | | none: must be set | | | | |
| Discussion limits (how far a discussion may go, and how requests are weighed) | | none: must be set | | | | |
| Waiting deadlines (per status) | | none: must be set | | | | |
| Bounce limit | | none: must be set | | | | |
| Chain depth (maximum depth of Work Item chains; set by the organisation, no fixed cap) | | none: must be set | | | | |
| Halt-request priority | | immediate | | | | |
| Budget cap (AI spend through the shared AI gateway, per AIOC) | | none: must be set | | | | |
| Unattended action (`unattended_action`: what the Chief of Staff may do after an automatic wake-up with no human present; Protocol §7) | | read-record-triage | | | | |
| Final authority (each `[ORG]AION` fills it; on the objection path it is the HOAC seat accountable for OCO, first row) | | none: must be set | | | | |

---

## 16. Type
- **Type:** `<Foundational / Structural / Specialised / Connector / other>`, as in §0.
- **Why this AIOC exists in this organisation:** one sentence (the `[ORG]AION` decides which AIOCs the organisation has).
- **Type-specific test:** `<test ID and version>` · result `NOT_RUN`.

The Type sets no count limit, no default connections and no mandatory sections. The Panel is a capability (§4.4), not a type. The AION Builder is a 49GAION capability, not an AIOC type (Standard §1.2).

## 17. Cells and Pods

The parts inside this AIOC (`docs/CELLS-AND-PODS.md`). One card per Cell and per Pod, following `spec/schemas/unit-card.schema.json` in `49g-holding/49GAION-protocol`. The role and nature of this AIOC are read from the type of its top Cell.

| Code | Kind | Type | Filler kind | HOAC label | Parent | Attached to | Fixed test (owner) | External ports |
|---|---|---|---|---|---|---|---|---|
| `<[ORG]CELL-INITIALS>` | CELL | `<from the organisation's list>` | `<human / ai / human-or-ai>` | `<none / [ORG]HOAC-...>` | `<code>` | `<person's Cell, for an AI assistant>` | `<test ID and version (seat)>` | `<none / service and direction>` |
| `<[ORG]POD-INITIALS>` | POD | `<from the organisation's list>` | — | `<none / [ORG]HOAC-...>` | `<code>` | — | `<test ID and version (seat)>` | — |

```yaml
cell:
  unit_kind: "CELL"
  code: "<[ORG]CELL-INITIALS>"
  parent: "<code of this AIOC or of its Pod>"
  type: "<from the organisation's list>"
  filler_kind: "<human | ai | human-or-ai>"
  hoac: "<[ORG]HOAC-GOV | [ORG]HOAC-TM | [ORG]HOAC-ACS>"   # omit if none
  attached_to: "<code of the person's Cell>"              # only for a person's AI assistant
  fixed_test: { id: "<test ID>", version: "<vN>", owner: "<code of the seat>" }
```

- A Pod holds Cells only; anything that needs nesting is an AIOC.
- An external service, API or tool is a port on the card of the Cell that receives or sends, never a Cell; an external AI agent acting directly in the work is an AI Cell.

## Annex A. The four-part capability form (normative for every capability)

### A.1 Definition — must contain
| Field | Content |
|---|---|
| Name | plain English, no code |
| What it is | one paragraph |
| Purpose | one sentence |
| Scope | does / does not |
| Inputs | what, from whom, in what format |
| Outputs | what, to whom, in what format |
| Limits | what it may never do |
| Sources | the governing texts it rests on, by ID and version |
| Status | draft, in force or replaced |

### A.2 Process (SOP) — must contain
| Field | Content |
|---|---|
| Trigger | what starts it |
| Steps | numbered; each: position — action — output — evidence |
| States | the states an item passes through and who moves it |
| Failure and recovery | raise, never guess; two failures on the same step stop and go to the owner |
| Records | what it writes, and where |
| Cadence | daily / weekly / monthly / quarterly, if any |
| Measures | name — definition — target (no target invented) |


### A.3 Role card — must contain
| Field | Content |
|---|---|
| Name | plain English |
| Position and seat | the position; its accountable `[ORG]HOAC-ACS` seat |
| Performed by | a bot, an agent or a person (holder in the holders register only) |
| Purpose | one line |
| Authority limits | alone / needs the owner / never — mirroring the panel switch |
| Write location | the single place it writes |
| Reports to | normally the Chief of Staff; the owner directly only in a board session |
| Escalation | where and how |
| Tools and access | which, through the panel; never credentials in instructions |
| Deputy and cover | who acts when it cannot |
| Fixed test and score | the test ID |
| Card version and status | — |

### A.4 Fixed test — must contain
| Field | Content |
|---|---|
| Test ID and version | frozen once used; items are struck by adjudication, never renumbered |
| Cases | each with pass criteria, written before use |
| Evidence level | MEASURED or OWNER_ATTESTED |
| Re-run triggers | §9 |
| Lessons added | each lesson adds at least one case |
| Where results are kept | §9 and the panel |
| Last result | `NOT_RUN` until run; never reported as PASS |

### A.5 Bot identity card — must contain
Every bot performing a role card has one identity card.

| Field | Content |
|---|---|
| Role | the role card it performs (A.3) |
| Account | its **own separate account**; never a human's account and never shared with another bot |
| Allowed actions | what it may do alone |
| Ask first | the actions that require a **prior request to the accountable human**, and how the request is made |
| Card version and status | — |

Schema: `49GAION-protocol` `spec/schemas/bot-identity-card.schema.json`.

*49GAION AIOC Blueprint Template v1.3.0 · Powered by 49GAION*

