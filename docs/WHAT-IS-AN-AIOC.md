# What an AIOC is

**Version `v1.0.0` · approved by Iman Tajik (Founder).** Part of the 49GAION Standard (`49g-holding/49GAION`, `upstream/49GAION-UPSTREAM.md` §5.1). Where this page and the Standard differ, the Standard governs.

## 1. Definition

An **AIOC** (AI Operating Core) is an AI unit of one organisation, coded `[ORG]AIOC-[INITIALS]`. It belongs to that organisation's `[ORG]AION` and sits at the unit level beside the human unit, the HOAC. AI does the work; the AIOC's `[ORG]HOAC-ACS` seat oversees it.

49GAION is an organisation design framework: a framework for building organisations from interchangeable AI and human parts.

**The product: `[ORG]AION`.** 49GAION's product is `[ORG]AION`, the AI Operating Nexus of one organisation (for example "Nike AION, Powered by 49GAION"). Each `[ORG]AION` is built for one organisation and is not public. It is a complete organisation design: it contains its own Standard, Protocol, Library, Self-Improvement, AIOCs and HOACs, and the organisation is built from it. It has its own `[ORG]HOAC-GOV` from day one, so its top authority is that organisation, not 49GAION, and it stands on its own Human Floor. Every AIOC in an `[ORG]AION` has its own runtime, woken from its queue. The AION Builder builds each `[ORG]AION` over a design period; once delivered, the `[ORG]AION` belongs entirely to the customer.

## 2. Anatomy

An AIOC = **Panel + Back office + Versioned Definition**.

| Layer | Definition |
|---|---|
| **Panel** | The only surface humans use. It includes a Health section: test results and stuck, returned and late items. |
| **Back office** | The AIOC's live working space (its instructions, files and settings) where its agents, led by its Chief of Staff, do the work. Human conversation with it goes through the Panel. |
| **Versioned Definition** | The AIOC's one blueprint in git, from which the Panel and the Back office are built and rebuilt. |

**One file, no drift.** The blueprint is the only definition. A change to the AIOC is a tested change to the blueprint; the Panel and Back office follow it.

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

The list is open. `[ORG]AIOC-OCO` (Organization Core Office) is the highest executive of the AIOCs (Standard §4.2).

## 5. The accountable seat and the responsible AI Office

1. Where an AIOC has an `[ORG]HOAC-ACS` seat, that seat is accountable for its results. It oversees, receives reports, may request anything for the unit, and never builds or changes the AIs directly (Standard §4.2, item 6).
2. The seat's requests go to the AI Office responsible for that unit. Where they disagree, the AI Office does not decide: the seat may hold the objection open until it reaches the HOAC seat accountable for that AI Office, which decides (Standard §4.2, item 7).
3. A change to an AI's authority (capacity, skills, bots, access, budget) is decided by the `[ORG]HOAC-ACS` seat; the AI Office responsible for that unit prepares, checks and carries it out.

## 6. Runtime

Every AIOC has its own runtime, woken from its queue.

## 7. Ports and stop

Every AIOC has two inputs and two outputs, typed AI or HU, each with a Port card, and a mandatory, queue-less stop port of type HU (Standard §6.1, §4.3). An `[ORG]AION` is handed over only when the stop ports of all its units, its `[ORG]HOAC-GOV` and its Human Floor are in place (Standard §1.4).

## 8. The Library, lineage, merge and split

1. Every AIOC blueprint is an entry in the 49GAION Library: built once, configured per `[ORG]AION`, never rebuilt. During the design of an `[ORG]AION`, the blueprint of any capability not already in the 49GAION Library is added back to it, generalised and tested.
2. Each AIOC card records its lineage: which AIOCs and versions it came from.
3. 49GAION Self-Improvement proposes merging overlapping AIOCs and splitting AIOCs that have grown too broad; it carries them out after Iman's decision. No AIOC is deleted, only replaced, and no fixed test is lost.

## 9. Blueprints and versions

1. Each kind of AIOC has a versioned default ("mother") blueprint in the Library, filled from the template in [`../template/AIOC-BLUEPRINT-TEMPLATE.md`](../template/AIOC-BLUEPRINT-TEMPLATE.md).
2. An organisation configures it in its `[ORG]AION` and records which version it took. Configuration lives in the blueprint's Configuration section; an AIOC with an empty slot does not join.
3. Lessons return to the mother blueprint as tested proposals.

## 10. Working with other AIOCs

AIOCs exchange work only through the 49GAION Operating Protocol: a card per AIOC, one Work Item per hand-off, typed ports (two inputs, two outputs, AI/HU, plus a stop door), an input check on arrival, links to sources instead of copies.
