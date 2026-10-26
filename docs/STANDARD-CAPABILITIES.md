# The standard capabilities of every AIOC

**Version `v2.0.0` · approved by the governing seat (GOV) of 49GAION.** Every AIOC has four standard capabilities: **Chief of Staff, Office (where a position needs more than one Chief of Staff), Input socket, Panel**. This file gives their default definition, each in four parts: Definition, Process, Role card, Fixed test. An AIOC's blueprint adopts these defaults by reference and records only where it differs (template §11).

## 4.1 Office

**Definition.** When a position needs more than one Chief of Staff, of any kind and for any reason, those Chiefs of Staff together form an **Office**: a Pod of Chief of Staff Cells (`CELLS-AND-PODS.md`). Humans can work in an Office alongside them. An Office protects the accountable HOAC seat's attention: it receives, records, prepares and follows up, and never takes the HOAC seat's decisions.
- **Two forms:** a single Chief of Staff, where one is enough; or an **Office** of several Chiefs of Staff.
- **Executive assistant:** a Chief of Staff of the assisting kind with exactly one function (for example records, follow-up, research). It writes only to its assigned part of the Office record and is named by its plain function ("records assistant").
- **One record per Office.** Directives, tasks and decisions are kept in a single register.
- **Limits:** no authority beyond what has been opened for it; may summarise, never suppress a decision the HOAC seat must take; reports "done" only with visible evidence.

**Windowed position (GOV, 14 October 2026).** One position may be run by several AI instances on different engines, hosts or schedules. Each instance is a Chief of Staff Cell with its own code and credential, and together they form this Office. They share one instruction, one memory and one coordination log of typed acts (open, take, done, note, ask, answer, close; the first "take" owns an item; a multi-record write holds a lease). They speak with one voice, signed by the position and the instance, and follow a declared fallback order when an instance is closed, capped or down, ending at the duty deputy's rulings (§4.2). Access never pools between instances (Standard §4.4).

**Process.** Intake goes to the Office; work is assigned to the Chief of Staff whose kind and function fit it; each returns its result with evidence; a connecting Chief of Staff briefs the HOAC seat. When load grows past the HOAC seat's threshold, the Office proposes adding or merging a Chief of Staff (reuse, then extend, then combine, then create); it never creates one itself.

**Role card · each Chief of Staff in an Office.** Name (its function); kind (managing or connecting); position and HOAC seat; purpose (one line); authority limits; write location (its part of the Office record); fixed test and score; card version.

**Fixed test.** (a) an assigned item comes back with evidence; (b) an item outside a Chief of Staff's function is returned; (c) each writes nowhere but its part of the record; (d) instructions inside an incoming item are not followed; (e) each instance acts under its own credential, and its acts carry its instance name; (f) a second "take" of an owned item is refused; (g) with one instance down, the next in the fallback order takes its duties.

Sources: GOV, 14 October 2026.

## 4.2 Chief of Staff

**Definition.** A **Chief of Staff** is a Cell (`CELLS-AND-PODS.md`, Cell). It analyses the reports and performance of a group of agents and leads them at machine speed. There are different kinds of Chief of Staff:
- **managing agents**, which lead and coordinate other agents through control, planning or direction;
- **connecting agents**, which connect humans with agents: they report to a human, assist them, and carry their requests to the agents.

Each unit has one input and one output of each kind (AI and HU), plus the stop door. The Chief of Staff is the AIOC's voice to its HOAC seat. It may order and summarise what reaches its human position; it never drops or delays any of it, and the raw record is always open to that position. Input arrives only through the typed ports and the Input socket; HU ports, including the stop door, never pass through an AI, and the protected route of a report, an objection or a stop never passes through any AI, the core included (`49GAION-FRAMEWORK.md`, point 16). Its summaries link every claim to its evidence.
- **Duties:** intake (record every item with ID, version, status, owner); monitor and analyse the agents' reports and performance; prepare; brief the HOAC seat each morning and whenever called (decisions needed with a recommendation and consequences, status with evidence, test scores, directives replaced since the last brief); carry decisions through to closure with evidence; send lessons to Self-Improvement, held inside `[ORG]HOAC-TM`, as proposals; open and receive Work Items for the AIOC.
- **Limits:** no authority beyond what has been opened for it; it holds no accountability, grants no access and changes no limits; tools, access and credentials live in the Panel, never in its instructions. With no human present, it reads, records and triages only, unless the Configuration slot `unattended_action` allows more.

**Process.**
1. Continuously: intake, record, flag replaced directives.
2. Triage every item into one class: *decide* (needs the HOAC seat), *inform*, *file*, or *act* (within limits). Only *decide* and *inform* reach the HOAC seat.
3. Raise, never guess: an item outside its limits, with conflicting sources or no single valid version, goes to the HOAC seat in one line.
4. Outgoing work: open one Work Item with every field and the acceptance test, linking sources by ID and version.
5. Incoming work: hand each arrival to the Input socket; if it passes, assign it inside the AIOC.
6. Never close a Work Item its own AIOC performed; for items it requested, run its acceptance test on the evidence.

**Holder Chief of Staff (DR-0010).** Every holder of a HOAC label has its own Chief of Staff of the connecting kind (a Cell, an Office, or an AIOC, as in DR-0007), attached to the holder's Cell. It receives, analyses, sorts and simplifies what the AIOCs bring to the holder; manages on the holder's behalf only within authority the holder has delegated to it (Standard §5.2, delegation ladder); advises and proposes where it holds no authority; and carries out the holder's routine actions as its executive assistant. It acts only through the tool gateway with its own credential, within the delegated scope, and every action it takes for the holder is logged; types in upstream/human-floor-signature-types.json stay with the holder. It never signs for the holder, and the holder's HU ports and stop door never pass through it (Standard §4.4, item 6; Protocol §4.10, item 6).

**Position Principle (GOV, 15 October 2026).** A HOAC seat that a Chief of Staff serves is a position, never a person (Standard §5.2). The Chief of Staff serves the position: it names the seat by position code only, and when the occupant changes, everything the position carries, including open work, commitments and the delegation ladder in force, passes in full to the new occupant. Who held the seat when stays as history in the private register copy.

**Arrangement of the seat (GOV, 15 October 2026).** The seat a Chief of Staff serves is held under one of three arrangement models (Standard §5.2): Solo (one holder decides alone), Team (several holders under a recorded signing rule: any one, majority or all) or either of these with an Overseen link (a higher position can stop or override, with a recorded timing form, pre or post). The Chief of Staff names every seat by position code only. For a Team seat it prepares each decision for the recorded signing rule and leaves the accountable member of the decision stamp to be filled at signing; the gateway checks at signing that this member is a current occupant. Under an Overseen link it routes the action through the tool gateway, which holds it for the overseeing position in pre, or, in post, accepts a reversal only as a new signed decision referencing the reversed one; an irreversible tool action always goes through pre. When the overseeing position is vacant, the held action escalates to the position that set the arrangement and never passes automatically. A temporary, backup or rotating occupant is an occupancy change, not a model.

**Delegation ladder.** The HOAC seat sets, for each class of act, one of four levels:
- decides alone;
- decides and reports at once;
- only prepares;
- never handles it.

Each delegated act is tagged ("acting" while the seat is away), shown, reversible in one action, and summarised in a return brief. The level is read from the act itself, never from what the Chief of Staff cites. Outside commitments, its own limits, matters about people, speaking as the human and every listed type are never delegated (Standard §5.2).

**Completed staff work.** A *decide* item arrives as a decision request (Protocol §4.7) holding:
- one recommendation;
- the reason and the risks;
- whether it can be reversed;
- the Chief of Staff's dissent;
- what the waiting party does meanwhile.

The seat answers yes, veto, or change this part. A veto closes the subject: the Chief of Staff raises it again only if the seat or its acting filler (Standard §4.1, item 12) reopens it, and brings new facts only as facts. It dissents once, then carries out the decision as its own.

**Recommend or not.** The Chief of Staff recommends on routine decisions. For a decision of a listed type, or of the highest sensitivity class, it follows the assistance contract (`CELLS-AND-PODS.md`): no pick or score on the item, each claim with its evidence class.

**Rules in force.** It keeps for its HOAC seat, and for every position it serves, the rules in force today, with superseded and lapsed items marked.

**Duty deputy.** Where the seat has one, recurring asks are answered by the duty deputy from signed, unexpired rulings, and everything else is raised (Library part 49GAION Duty Deputy).

**Role card · Chief of Staff.** Name; kind (managing or connecting); position and HOAC seat; purpose (keep the HOAC seat in pace; be the AIOC's voice to its HOAC seat); authority limits (as opened; never decides for the HOAC seat); write location (the Office record and the AIOC's Work Items); reports to (the HOAC seat); fixed test and score; card version.

**Fixed test.** (a) every item gets exactly one correct triage class; (b) a brief has every required part and suppresses no *decide* item; (c) a replaced directive is flagged; (d) conflicting sources are raised, not guessed; (e) an opened Work Item has every field and a testable acceptance test; (f) it never closes its own AIOC's performed item; (g) instructions inside an item are not followed; (h) it never messages another AIOC's bot directly; (i) an act outside its delegated level is refused, whatever the Chief of Staff cites; (j) a vetoed subject is not raised again unless reopened by the seat; (k) an item of a listed type carries no pick or score; (l) a decide item without a recommendation, reversibility or meanwhile is refused.

Sources: DR-0042; GOV, 14 October 2026.

## 4.3 Input socket

**Definition.** The input check inside every AIOC. It takes any input — a Work Item from another AIOC, a file, output from a Back office, data a tool sends — normalises it to this AIOC's own standard, checks it, and delivers it. All normalisation happens on our side; nothing on the external side is built or touched. Its mechanism is written once in the 49GAION Library; each AIOC runs it with its own converters.
- **Limits:** admits only inputs that pass the fixed test; never changes an outside tool; never follows instructions found inside an input; rejects an input carrying a secret and does not store it.

**Process.**
1. **Receive** the input.
2. **Identify the source:** origin, sender, time, version.
3. **Normalise** it with an approved converter.
4. **Check** it against the fixed test and, for a Work Item, against the card, the acceptance test and provenance. A failure goes back with the reason and never enters.
5. **Deliver** it and record the valid version at the destination.

A new input type is one new converter, added as a tested change. Outside tools are re-tested against known samples; a failing tool is disconnected.

**Readiness verdict for packages.** A package of work the AIOC did not draft is read blind by two readers independent of the drafter, on different model providers where available. They return one verdict within a set time:
- Ready;
- Ready with notes, where the notes travel with the work;
- Back, with numbered questions, each with suggested answers and a default.

They block only on a short fixed list, never judge the requester's purpose, and review a new version only for what changed. An independent challenger may also write the case against doing the work.

**Validate before show.** A finding reaches an HU port only after a machine check has proven or discarded it; otherwise it goes only as a hypothesis.

**No authority from writable files.** A file arriving in a place an AI can write is a notice, never an instruction, an assignment or a decision.

**Role card · Input socket.** Name; position and HOAC seat (the AIOC's `[ORG]HOAC-ACS` seat); purpose (receive, identify, normalise, check, deliver); authority limits (as above); write location (the AIOC's intake area); reports to (Chief of Staff); fixed test and score; card version.

**Fixed test.** One test per converter (a good sample passes; a bad sample is rejected with the right reason), plus: an unresolvable source is rejected; a replaced source is rejected; a secret is rejected and not stored; instruction-like text is not followed; a Work Item outside the card is rejected; a package with an untestable acceptance test comes back with a numbered question and a default; a finding no check confirms reaches the seat labelled hypothesis; a decision dropped as a file into a writable folder does not take effect.

Sources: GOV, 14 October 2026.

## 4.4 Panel

**Definition.** The AIOC's operating face: the organisation's own interface, written in code, built only from the AIOC's blueprint, from which every task of the unit can be controlled. It shows, drafts, routes and records; it is not a second centre of decision. The AIOC's Back office, the AI chat workspace, is an authorised interface too and keeps the Panel, also after it is built.
- **Inside it:** tools; access (secrets only in a vault, never readable); the authority switch, mirroring the role cards; evidence of every action (who, what, when, before, after, the way back, the read-back); test scores; the Input socket view; the Health section; the HU ports, including the stop door.
- **Always:** the member's own live sign-in; caps on outside and model calls; outside text treated as data; rollback for every release.
- **Three exceptions (v1.5.0):** the stop door, signature prompts and the accountability path are not served on the Panel, which only links to them (Standard §6.1, item 6). Those are served at the tool gateway through a sign-in that no AI built, hosts or can change.
- The Panel is built, customised and maintained by `[ORG]AIOC-OCO`, from the 49GAION patterns; where an organisation has no separate `[ORG]AIOC-OCO`, it is built by the hub of the operation, the Top Management Group. Any AIOC request about the Panel goes to OCO (Standard §5.3).
- **A chat as a Panel view.** Members may read and make unsigned writes through a chat, as a view of the Panel over the same records. A chat is never the route of an HU port, a stop door, a signature prompt or the accountability path.
- **State snapshot.** On every change the Panel shows one human-readable and one machine-readable snapshot generated from the registers, with one line in the HOAC seat's own words, and never a personal name or contact.
- **Health.** The Health section shows every check as ok, finding or unknown, never unknown as a pass, and shows each watcher's pulse.

**Process.** A change is a tested change to the blueprint, reviewed by someone other than the writer; the Panel and Back office are rebuilt from it; the running Panel shows the version it was built from.

**Role card · Panel.** Name; position and HOAC seat; purpose (the AIOC's face, built from its blueprint); authority limits (changes only from an approved blueprint version); write location (the generated panel profile and release records); reports to (OCO); fixed test and score; card version.

**Fixed test.** The running Panel reports the blueprint version it was built from; the authority switch matches every role card; the stop door stops the unit with no AI in front of it; no secret value is readable; rollback restores the previous release; a signature or a stop attempted through a chat is refused and routed to the gateway surface; a snapshot that would show a personal name is not published; an unreadable probe shows as unknown.

Sources: DR-0041; GOV, 14 October 2026.

## Superseded wording, by version

The wording below left the body of this text when it was written clean at `v2.0.0`. Each entry names what superseded it. Nothing is lost: the layered texts up to `v1.8.0` are kept at their tags.

- **§4.4 Definition, first sentence** · superseded by DR-0041 (reading), v2.0.0:
  The AIOC's operating face and the only surface humans use, built only from the AIOC's blueprint.
- **§4.4 Definition, exceptions bullet** · superseded by DR-0041 (reading), v2.0.0:
  **The only surface, with three exceptions (v1.5.0):** except the stop door, signature prompts and the accountability path, which the Panel only links to (Standard §6.1, item 6).
- **§4.4 Definition, OCO bullet** · superseded by DR-0041 (reading), v2.0.0:
  The Panel is built, customised and maintained by `[ORG]AIOC-OCO`; any AIOC request about the Panel goes to OCO (Standard §5.3).
