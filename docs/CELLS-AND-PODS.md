# Cells and Pods

**Version `v1.5.0` · proposed.** Part of the 49GAION Standard (`49g-holding/49GAION`, `upstream/49GAION-UPSTREAM.md` §1.7, §4.4). Where this page and the Standard differ, the Standard governs. Decision: `49GAION/DR-0004`.

The AIOC is the only unit kind of 49GAION, and AIOCs nest to any depth. Inside an AIOC, its Blueprint holds two kinds of part: Cells and Pods.

## 1. Cell

1. **The smallest part.** A Cell is the smallest part of an AIOC. Nothing sits inside a Cell.
2. **Seat and filler.** A Cell is a fixed seat. Its filler, a human or an AI agent, is replaceable. A change of filler is a recorded event in the unit register, never a new Cell, and the Cell keeps its code.
3. **Type.** Every Cell card has a type from an open list that each organisation configures in its `[ORG]AION`, for example Human Seat, Human Reviewer, AI Agent, AI Chief of Staff.
4. **Filler kind.** The card states which kind of filler the seat allows: human, AI, or either.
5. **Chief of Staff.** The Chief of Staff of an AIOC is itself a Cell (type AI Chief of Staff, or the organisation's equivalent). An Office is a Pod of Chief of Staff Cells (`STANDARD-CAPABILITIES.md` §4.1).
6. **A person's AI assistants.** The AI assistants of a person are separate registered AI Cells, each with its own code, attached to that person's Cell (`attached_to` on the card). They are never unnamed.
7. **Fixed test.** Every Cell has a fixed test, owned by its seat. A filler gains access only after passing it; work moves from human to AI, or from one version to the next, only by passing it, and moves back if the score drops.
8. **HOAC label.** A Cell may carry a HOAC (Human Oversight & Accountability Control) label, `[ORG]HOAC-GOV`, `[ORG]HOAC-TM` or `[ORG]HOAC-ACS`, as a field of its card. A human seat that carries the label is accountable for the part it sits on and everything under it.
9. **Attached Cells (v1.5.0).** An attached AI Cell sits in the same Blueprint as the Cell it serves, has the same parent as that Cell and names its person's Cell in `attached_to`. It serves that seat only. When the filler changes, its memory of the previous filler is sealed. Whatever its filler, an attached Cell, including a Chief of Staff, never signs for its person (Protocol §4.10).
10. **Two relations (v1.5.0).** `parent` names only the AIOC or Pod whose Blueprint holds the Cell's card; `accountable_to` names the human Cell carrying a HOAC label to which the Cell answers. A Cell is never a parent; nothing sits inside a Cell (Standard §1.7).
11. **A label on a human seat (v1.5.0).** A HOAC label sits only on a Cell whose filler kind is human. If that seat is empty or filled by an AI, the label's powers are held (Standard §4.1).

## 2. Pod

1. **Cells only.** A Pod groups Cells only. A Pod never holds a Pod; anything that needs nesting is an AIOC.
2. **One piece from outside.** Seen from outside, a Pod is like a Cell: the same card shape, its typed ports and its stop door.
3. **No pooled access.** Within a Pod, access does not pool: each Cell holds only its own.
4. **Stop.** Stopping a Pod stops every Cell in it. Its stop door is outside it.
5. **HOAC label.** A Pod may carry a HOAC label, as a field of its card.
6. **Label holder or decision rule (v1.5.0).** A Pod with a HOAC label names its `label_holder`, one human Cell in it, or, when it decides together, a `decision_rule`: member Cells, quorum, majority, chair and casting vote. Each member signs under their own Cell; one person holding two seats in the same body counts once (Standard §4.1).

## 3. Nature and role

The role and nature of a Pod or an AIOC are read from the type of its top Cell. There is no rule that every AIOC must contain a given kind of Cell or Pod.

**Top Cell (v1.5.0).** The card's `top_cell` names exactly one Cell whose parent is that part. Co-leadership is a Pod with a decision rule. The top Cell gives the part's lead; the AIOC Type gives why it exists (Standard §1.7).

## 4. External attachments

1. **Not a Cell.** An external service, API or tool is not a Cell. Each connection to one is a port recorded on the card of the Cell that receives from it (input) or sends to it (output).
2. **The intake Cell.** The Cell that receives from outside normalises what arrives to the AIOC's own standard, and has its own fixed test.
3. **Through the gateway.** External ports pass only through the tool gateway. Stopping or retiring the owning Cell cuts the external connection automatically.
4. **Register events.** The unit register records `connected` and `disconnected` events for each external port.
5. **External AI agents.** An external AI agent that acts directly in the organisation's work is registered as an AI Cell. The organisation grants its access and holds its stop door.
6. **Connecting a port (v1.5.0).** Connecting a port is the listed decision type `connect-external-port`. Anything that acts autonomously with the organisation's credentials is an external AI agent. No external agent or outside person signs; what arrives from them is data (Standard §4.4).

## 5. Codes

Every Pod and Cell has one fixed code and a separate `parent` field: `[ORG]POD-[INITIALS]`, `[ORG]CELL-[INITIALS]` (Naming Standard R14, R15). A code is never a path and carries no suffix. The card's machine form is `unit-card.schema.json` in `49g-holding/49GAION-protocol`.

Powered by 49GAION
