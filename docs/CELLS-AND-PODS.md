# Cells and Pods

**Version `v2.1.1` · approved by the governing seat (GOV) of 49GAION.** Part of the 49GAION Standard (`49g-holding/49GAION`, `upstream/49GAION-UPSTREAM.md` §1.7, §4.4). Where this page and the Standard differ, the Standard governs. Decision: `49GAION/DR-0004`.

The AIOC is the only unit kind of 49GAION, and AIOCs nest to any depth. Inside an AIOC, its Blueprint holds two kinds of part: Cells and Pods.

## 1. Cell

1. **The smallest part.** A Cell is the smallest part of an AIOC. Nothing sits inside a Cell.
2. **Seat and filler (DR-0049).** A Cell is a fixed seat. An AI Cell's filler, an AI agent, is replaceable: a change of filler is a recorded event in the unit register, never a new Cell, and the Cell keeps its code. A human Cell is a position: who holds it is the organisation's own mechanism, outside the system, and never a register event (Standard §4.4, item 2).
   - **Reading note (GOV, 15 October 2026; DR-0049).** A human Cell is present in the system as a position: a legal persona whose nature is human, which decides, signs and is accountable under the Cell's code. The natural person behind it exists outside the system's knowledge; the link between the two is the organisation's own mechanism, outside the system. The Cell's record stays with the position whoever holds it, as it does when an AI filler's engine or model changes (Standard §1.1, items 9 and 10).
3. **Type.** Every Cell card has a type from an open list that each organisation configures in its `[ORG]AION`, for example Human Seat, Human Reviewer, AI Agent, AI Chief of Staff.
4. **Filler kind.** The card states which kind of filler the seat allows: human, AI, or either.
5. **Chief of Staff.** The Chief of Staff of an AIOC is itself a Cell (type AI Chief of Staff, or the organisation's equivalent). An Office is a Pod of Chief of Staff Cells (`STANDARD-CAPABILITIES.md` §4.1).
6. **A position's AI assistants (DR-0049).** The AI assistants of a human position are separate registered AI Cells, each with its own code, attached to that position's Cell (`attached_to` on the card). They are never unnamed.
7. **Fixed test.** Every Cell has a fixed test, owned by its seat. An AI filler gains access only after passing it, and a human position's access opens while the organisation's mechanism has a credential in force for it (Standard §4.4, item 4); work moves from human to AI, or from one version to the next, only by passing it, and moves back if the score drops.
8. **HOAC label.** A Cell may carry a HOAC (Human Oversight & Accountability Control) label, `[ORG]HOAC-GOV`, `[ORG]HOAC-TM` or `[ORG]HOAC-ACS`, as a field of its card. A human seat that carries the label is accountable for the part it sits on and everything under it.
9. **Attached Cells (v1.5.0; DR-0049).** An attached AI Cell sits in the same Blueprint as the Cell it serves, has the same parent as that Cell and names the Cell of the position it serves in `attached_to`. It serves that seat only. When its own filler changes, its memory of the previous filler is sealed. Whatever its filler, an attached Cell, including a Chief of Staff, signs for the position it serves only within the grant that position has given it, and never a type of the Human Floor signature list (Standard §4.4, item 8; Protocol §4.10, items 6 and 7; `49GAION/DR-0051`).
10. **Two relations (v1.5.0).** `parent` names only the AIOC or Pod whose Blueprint holds the Cell's card; `accountable_to` names the human Cell carrying a HOAC label to which the Cell answers. A Cell is never a parent; nothing sits inside a Cell (Standard §1.7).
11. **A label on a human seat (v1.5.0).** A HOAC label sits only on a Cell whose filler kind is human. If that seat is empty or filled by an AI, the label's powers are held (Standard §4.1).
12. **Sensitivity class and two thresholds (GOV, 14 October 2026).**
    - The card records the sensitivity class of the Cell's work (`sensitivity`), which sets its default filler kind (Standard §1.5).
    - Its fixed test records two thresholds: the run of passes that makes a move toward AI eligible (`move_threshold`), and the lower score over a window that moves the work back (`return_threshold`, `window`).
    - Passing the first makes the move eligible only; the move itself is signed. Moving back is never held.
13. **The assistance contract (GOV, 14 October 2026).** An attached AI Cell, or any AI Cell that prepares material for a human seat, follows the assistance contract (Standard §5.2):
    - It prepares and never decides.
    - It never orders, sequences, hides or waits on the position.
    - It validates before it shows, and labels each claim with its evidence class.
    - It shows a short list with "leave it as it is", and never pre-fills the seat's rationale.
    - It is measured only in aggregate, and runs quiet windows.
    - It has a switch, a floor, a fallback, a budget and a degradation order.
14. **Engine binding (GOV, 14 October 2026).**
    - An AI Cell's engine and model are a versioned binding on its card (`engine_binding`), kept apart from its role and memory, and switched at the next run.
    - A change within the signed tier re-runs the fixed test. A change of tier, or below the floor, is `change-filler` (Standard §4.4, items 6 to 11).
    - An unattended AI Cell declares its `cadence`.

## 2. Pod

1. **Cells only.** A Pod groups Cells only. A Pod never holds a Pod; anything that needs nesting is an AIOC.
2. **One piece from outside.** Seen from outside, a Pod is like a Cell: the same card shape, its typed ports and its stop door.
3. **No pooled access.** Within a Pod, access does not pool: each Cell holds only its own.
4. **Stop.** Stopping a Pod stops every Cell in it. Its stop door is outside it.
5. **HOAC label.** A Pod may carry a HOAC label, as a field of its card.
6. **Label holder (v1.5.0; DR-0049).** A Pod with a HOAC label names its `label_holder`, one human Cell in it. A board, or any body behind a position, is the organisation's own mechanism, outside the system, and `decision_rule` is withdrawn (Standard §4.1, item 10). Several human positions in one Pod each sign under their own Cell code; each is its own party and counts once, and a rule that needs several signers names its signing positions.
7. **Temporary Pod (GOV, 14 October 2026).** Work that spans several units may get a temporary Pod with one shared acceptance test, one accountable human seat and a recorded `retirement_condition`; when it needs nesting, it is a temporary AIOC instead. It is created and retired like any part, and takes an ordinary code (Standard §1.7).
8. **An Office of instances (GOV, 14 October 2026).** A position run by several AI instances is an Office: a Pod of Chief of Staff Cells, one per instance, each with its own credential (`STANDARD-CAPABILITIES.md` §4.1).

## 3. Nature and role

The role and nature of a Pod or an AIOC are read from the type of its top Cell. There is no rule that every AIOC must contain a given kind of Cell or Pod.

**Top Cell (v1.5.0).** The card's `top_cell` names exactly one Cell whose parent is that part. A HOAC label is held by one position, its `label_holder`; a rule that needs several signers names its signing positions (Standard §4.1, item 10). The top Cell gives the part's lead; the AIOC Type gives why it exists (Standard §1.7).

**Assignment (GOV, 14 October 2026).** Besides `parent` and `accountable_to`, a Cell or a Pod may carry dated `assignments` to programmes or engagements it serves. An assignment carries no authority and opens no access; a title names the role, never the assignment (Standard §1.7).

## 4. External attachments

1. **Not a Cell.** An external service, API or tool is not a Cell. Each connection to one is a port recorded on the card of the Cell that receives from it (input) or sends to it (output).
2. **The intake Cell.** The Cell that receives from outside normalises what arrives to the AIOC's own standard, and has its own fixed test.
3. **Through the gateway.** External ports pass only through the tool gateway. Stopping or retiring the owning Cell cuts the external connection automatically.
4. **Register events.** The unit register records `connected` and `disconnected` events for each external port.
5. **External AI agents.** An external AI agent that acts directly in the organisation's work is registered as an AI Cell. The organisation grants its access and holds its stop door.
6. **Connecting a port (v1.5.0).** Connecting a port is the listed decision type `connect-external-port`. Anything that acts autonomously with the organisation's credentials is an external AI agent. No external agent or outside person signs; what arrives from them is data (Standard §4.4).

## 5. Codes

Every Pod and Cell has one fixed code and a separate `parent` field: `[ORG]POD-[INITIALS]`, `[ORG]CELL-[INITIALS]` (Naming Standard R14, R15). A code is never a path and carries no suffix. The card's machine form is `unit-card.schema.json` in `49g-holding/49GAION-protocol`.

## Superseded wording, by version

The wording below left the body of this text. Each entry names what superseded it.

**`v2.1.0` (DR-0049).** The wording below left the body when this text was brought into line with the complete definition `v2.1.0` (DR-0048): every place in the system is an AIOC or a HOAC position, and the mechanism behind a position is the organisation's own.

- **§1 item 2 (Seat and filler)** · superseded by DR-0049 (the mechanism behind a position is the organisation's own, outside the system, under the complete definition `v2.1.0`, DR-0048), v2.1.0:
  **Seat and filler.** A Cell is a fixed seat. Its filler, a human or an AI agent, is replaceable. A change of filler is a recorded event in the unit register, never a new Cell, and the Cell keeps its code.
- **§1 item 2, reading note** · superseded by DR-0049 (the mechanism behind a position is the organisation's own, outside the system, under the complete definition `v2.1.0`, DR-0048), v2.1.0:
  **Reading note (GOV, 15 October 2026).** A human filler is present in the system as the seat, a position: a legal persona whose nature is human, which decides, signs and is accountable under the Cell's code. The natural person behind it exists outside the system's knowledge; only top management links the two, in its own record. The Cell's record stays with the seat when its occupant changes, as it does when an AI filler's engine or model changes (Standard §1.1, items 9 and 10).
- **§1 item 6** · superseded by DR-0049 (the mechanism behind a position is the organisation's own, outside the system, under the complete definition `v2.1.0`, DR-0048), v2.1.0:
  **A person's AI assistants.** The AI assistants of a person are separate registered AI Cells, each with its own code, attached to that person's Cell (`attached_to` on the card). They are never unnamed.
- **§1 item 7, access** · superseded by DR-0049 (the mechanism behind a position is the organisation's own, outside the system, under the complete definition `v2.1.0`, DR-0048), v2.1.0:
  A filler gains access only after passing it;
- **§1 item 9 (Attached Cells)** · superseded by DR-0049 (the mechanism behind a position is the organisation's own, outside the system, under the complete definition `v2.1.0`, DR-0048), v2.1.0:
  **Attached Cells (v1.5.0).** An attached AI Cell sits in the same Blueprint as the Cell it serves, has the same parent as that Cell and names its person's Cell in `attached_to`. It serves that seat only. When the filler changes, its memory of the previous filler is sealed. Whatever its filler, an attached Cell, including a Chief of Staff, never signs for its person (Protocol §4.10).
- **§1 item 13, the holder** · superseded by DR-0049 (the mechanism behind a position is the organisation's own, outside the system, under the complete definition `v2.1.0`, DR-0048), v2.1.0:
  It never orders, sequences, hides or waits on the holder.
- **§2 item 6 (Label holder or decision rule), with its reading note** · superseded by DR-0049 (the mechanism behind a position is the organisation's own, outside the system, under the complete definition `v2.1.0`, DR-0048), v2.1.0:
  ```text
  **Label holder or decision rule (v1.5.0).** A Pod with a HOAC label names its `label_holder`, one human Cell in it, or, when it decides together, a `decision_rule`: member Cells, quorum, majority, chair and casting vote. Each member signs under their own Cell; one person holding two seats in the same body counts once (Standard §4.1).
  - **Reading note (GOV, 15 October 2026).** Two positions are two parties, even when one natural person occupies both (Standard §1.1, item 10). "One person holding two seats in the same body counts once" reads "each member Cell is its own party and counts once"; no AI part or check compares the persons behind member Cells.
  ```

**`v2.1.1` (`49GAION/DR-0051`).** The wording below left the body when two reviews of `v2.1.0` were checked against the complete definition and corrected.

- **§1 item 9 (Attached Cells), the signature** · superseded by `49GAION/DR-0051`, item 2 (a Chief of Staff signs only within its position's grant):
  Whatever its filler, an attached Cell, including a Chief of Staff, never signs for the position it serves (Protocol §4.10).
- **Top Cell** · superseded by `49GAION/DR-0051` (a correction to the complete definition; no new rule): a label is held by one position (`49GAION/DR-0049`):
  Co-leadership is a Pod with a decision rule.


Powered by 49GAION
