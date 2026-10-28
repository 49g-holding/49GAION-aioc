# What an AIOC is

**Version `v2.1.0` · approved by the governing seat (GOV) of 49GAION.** Part of the 49GAION Standard (`49g-holding/49GAION`, `upstream/49GAION-UPSTREAM.md` §5.1). Where this page and the Standard differ, the Standard governs.

## 1. Definition

An **AIOC** (AI Operating Core) is an AI unit of one organisation, coded `[ORG]AIOC-[INITIALS]`. It belongs to that organisation's `[ORG]AION`. The AIOC is the only unit kind: a unit is a part with its own Blueprint, and Pods and Cells are parts with cards inside it. Inside it, its Blueprint holds Cells and Pods (`CELLS-AND-PODS.md`). HOAC (Human Oversight & Accountability Control) is a label of human accountability that sits on a Cell, a Pod or the whole AIOC. AI does the work; the AIOC's `[ORG]HOAC-ACS` seat oversees it.

49GAION is an organisation design framework: a framework for building organisations from interchangeable AI and human parts.

**The product: `[ORG]AION`**, the AI Operating Nexus of one organisation; its one definition is in the 49GAION Standard, §1.3, item 1 ([`49GAION/upstream/49GAION-UPSTREAM.md`](https://github.com/49g-holding/49GAION/blob/main/upstream/49GAION-UPSTREAM.md)).

## 2. Anatomy

An AIOC = **Panel + Back office + Versioned Definition**.

| Layer | Definition |
|---|---|
| **Panel** | The interface: the organisation's own, unique to it, written in code, made from the 49GAION patterns; every task of the unit can be controlled from it. It includes a Health section: test results and stuck, returned and late items. |
| **Back office** | The AI chat workspace where the unit's AI works: the AIOC's live working space (its instructions, files and settings) where its agents, led by its Chief of Staff, do the work. It is an authorised interface too, through the same controls as the Panel, and the keeper of the Panel, also after the Panel is built, so no separate admin back office is written. |
| **Versioned Definition** | The AIOC's one blueprint in git, from which the Panel and the Back office are built and rebuilt. |

Each covers the other: if the Panel fails, the work goes on from the Back office, which can rebuild it. The HU ports, stop doors and signature prompts stay at the human gateway surface.

**One file, no drift.** The blueprint is the only definition. A change to the AIOC is a tested change to the blueprint; the Panel and Back office follow it.

Sources: DR-0041.

## 3. Capabilities

1. A **capability** is one thing the AIOC does. Each has four parts: **Definition, Process, Role card, Fixed test** (template Annex A).
2. **Standard capabilities** in every AIOC: **Chief of Staff**, **Office** (where a position needs more than one Chief of Staff), **Input socket**, **Panel**. Their default text is in [`STANDARD-CAPABILITIES.md`](STANDARD-CAPABILITIES.md).
3. **Functional capabilities** are added by each AIOC for its own work.
4. Capabilities are not units: they take plain English names and no code.

## 4. Types

Every AIOC has a **Type**, recorded on its card, never in its name. The Type says why the AIOC exists.

| Type | Exists because |
|---|---|
| **Foundational** | Every organisation needs it |
| **Structural** | Of the organisation's structure |
| **Specialised** | The business needs it |
| **Connector** | Other AIOCs must be connected and coordinated |

The list is open. The hub of the operation, human and AI, is the Top Management Group, the first AIOC under the core, which builds everything in the operation. `[ORG]HOAC-TM` is the human hub: it decides and orders. 49GAION requires no separate AI hub unit; where an organisation has one, it is `[ORG]AIOC-OCO` (Organization Core Office), serving the operation under Top Management: every AIOC, at any depth, joins, is fixed, maintained and upgraded through it, and it gives no orders on what work is done. OCO sits under TM: TM orders it, meets its human needs and is its accountable seat; TM and `[ORG]HOAC-GOV` may each stop it (Standard §4.2, §4.3). Wherever this document names OCO, it reads: the hub of the operation, or that separate unit.

Sources: DR-0041.

## 5. The accountable seat and OCO

1. Where an AIOC has an `[ORG]HOAC-ACS` seat, that seat is accountable for its results. It oversees, receives reports, may request anything for the unit, and never builds or changes the AIs directly (Standard §4.2, item 6).
2. The seat's requests go to OCO. Where they disagree, OCO does not decide: the seat may hold the objection open until it reaches the HOAC seat accountable for OCO, which decides (Standard §4.2, item 7).
3. A change to an AI's authority (capacity, skills, bots, access, budget) is decided by the `[ORG]HOAC-ACS` seat; OCO prepares, checks and carries it out.
4. **Two relations (v1.5.0).** An AIOC's card names its `parent` (the AIOC whose Blueprint lists it, or none for the Charter) and its `accountable_to` (the human Cell carrying a HOAC label to which it answers); every rule on accountability follows `accountable_to` (Standard §1.7). Its `top_cell` gives its lead; its Type gives why it exists.
5. **Human-led AIOC (v1.5.0).** An AIOC whose top Cell is human may set its Chief of Staff Cell to human-or-ai. Whatever the filler, a Chief of Staff never signs for the position it serves (DR-0049). The Charter is installed and changed only on GOV's signature; any other AIOC carrying a GOV or TM label, on GOV or TM signature; neither by OCO alone (Standard §1.7 and §5.1).

## 6. Runtime

Every AIOC has its own runtime, woken from its queue.

1. **Runtime contract.** One versioned runner performs the common duties of every AI Cell in a clean workspace per run, and each Cell pins its runner version.
2. **Wake and cadence.** A woken Cell checks for work with no model call. An unattended Cell is flagged when its newest output is older than twice its cadence.
3. **Halt, pause and cut-off.** The AIOC can be halted by plan (running, draining, paused, resuming), with hand-offs and a declared resume order. Human seats may flag or hold its work. A stop of AI authority fences credentials already issued, and every executed action has a recovery path (Standard §4.3).
4. **Self-healing and outside inspection.**
   - Detectors with no model find stuck, silent or failing work.
   - A repair stays inside the repairer's authority and is never a listed type.
   - Every watcher reports its pulse, and unknown is never a pass.
   - An outside inspector, sharing no failure with the AIOC, checks that its duties happened (Standard §3.2).
5. **Spend.** Spend is kept as separate numbers. A soft hold applies before the cap, and a Cell past its cap pauses alone. The capability declares the order in which it sheds work (Standard §5.1).

Sources: GOV, 14 October 2026.

## 7. Ports and stop

Every AIOC has one input and one output of each kind (AI and HU), each with a Port card, plus the stop door: a mandatory, queue-less stop port of type HU, enforced outside the unit (Standard §6.1, §4.3). Stopping an AIOC stops every unit inside it; a human port never passes through an AI unit.

## 8. The Library, lineage, merge and split

1. Every AIOC blueprint is an entry in the 49GAION Library: built once, configured per `[ORG]AION`, never rebuilt. During the design of an `[ORG]AION`, the blueprint of any capability not already in the 49GAION Library is added back to it, generalised and tested.
2. Each AIOC card records its lineage: which AIOCs and versions it came from.
3. Self-Improvement may propose merging overlapping AIOCs or splitting an AIOC that has grown too broad. In an `[ORG]AION` the proposal is decided by `[ORG]HOAC-TM` and carried out through OCO; in 49GAION it is decided by the governing seat (GOV) of 49GAION (Standard §2). No AIOC is deleted, only replaced, and no fixed test is lost.
4. **The mechanism register and the Reserve (GOV, 14 October 2026).** Every AIOC keeps, in its blueprint, one register of its mechanisms: what each does, where it lives, its state today and its target. It never deletes a row, and every change that builds a row cites it. Ideas not adopted go to the Reserve, with their reason and a reconsider-when trigger (Standard §2.1, §3.2).
5. **Fresh instance and duty carriage (GOV, 14 October 2026).** On every change, a fresh instance is built from the blueprint alone and run against the fixed tests. Every duty a role card gives is traced to a process step, an event or a setting.

## 9. Blueprints and versions

1. Each kind of AIOC has a versioned default ("mother") blueprint in the Library, filled from the template in [`../template/AIOC-BLUEPRINT-TEMPLATE.md`](../template/AIOC-BLUEPRINT-TEMPLATE.md).
2. An organisation configures it in its `[ORG]AION` and records which version it took. Configuration lives in the blueprint's Configuration section; an AIOC with an empty slot does not join.
3. Lessons return to the mother blueprint as tested proposals.

## 10. Composition

1. An AIOC may hold other AIOCs, to any depth, and holds its own Pods and Cells; an AIOC may itself sit inside an AIOC (Standard §1.7). A HOAC label may sit on any of them.
2. Seen from outside, a composite AIOC is one unit: one card, its ports and its stop door. Its Chief of Staff is the door for AI work to its inner units; the HU ports and stop doors of inner units never pass through it.
3. Every inner unit has its own card: an inner AIOC has a card and a blueprint; a Pod or a Cell has a card in its AIOC's Blueprint. Each is listed in the parent's blueprint by link. Its place is the `parent` field of its card; its code never changes when it moves, and a change of parent needs the approval of the human seat over it (Naming Standard R14).
4. Every AIOC, at any depth, joins, is fixed, maintained and upgraded through the hub of the operation, the Top Management Group, or a separate `[ORG]AIOC-OCO` serving it.

Sources: DR-0041.

## 11. Working with other units

AIOCs exchange work only through the 49GAION Operating Protocol: a card per AIOC, one Work Item per hand-off, ports (one input and one output of each kind, AI and HU, plus the stop door), an input check on arrival, links to sources instead of copies.

Inside and between AIOCs:
- **Records.** Records live in one home as events; registers and numbers are projections; every surface is a portal.
- **Coordination log.** Parts that share records keep a coordination log of typed acts.
- **Move-on.** A waiting item takes a move-on, recorded as a debt.
- **Verdict records.** Verifications are records bound to the exact version, written by a non-author.
- **Decision requests.** A matter for a human arrives as a decision request.

Sources: GOV, 14 October 2026.

## Superseded wording, by version

The wording below left the body of this text when it was written clean at `v2.0.0`. Each entry names what superseded it. Nothing is lost: the layered texts up to `v1.8.0` are kept at their tags.

- **§2 Anatomy, table row Panel** · superseded by DR-0041 (reading), v2.0.0:
  The only surface humans use.
- **§2 Anatomy, table row Back office** · superseded by DR-0041 (reading), v2.0.0:
  Human conversation with it goes through the Panel.
- **§4 Types, last paragraph** · superseded by DR-0041 (reading), v2.0.0:
  `[ORG]AIOC-OCO` (Organization Core Office) is the AI hub: every AIOC, at any depth, joins, is fixed, maintained and upgraded through it; it gives no orders on what work is done.
- **§10 item 3** · superseded by v1.5.0 (label):
  Every inner unit has its own card and blueprint
- **§10 item 4** · superseded by DR-0041 (reading), v2.0.0:
  Every AIOC, at any depth, joins, is fixed, maintained and upgraded through `[ORG]AIOC-OCO`.

**`v2.1.0` (DR-0049).** The wording below left the body when this text was brought into line with the complete definition `v2.1.0` (DR-0048): every place in the system is an AIOC or a HOAC position, and the mechanism behind a position is the organisation's own.

- **§5 item 5, the Chief of Staff** · superseded by DR-0049 (the mechanism behind a position is the organisation's own, outside the system, under the complete definition `v2.1.0`, DR-0048), v2.1.0:
  Whatever the filler, a Chief of Staff never signs for its person.
