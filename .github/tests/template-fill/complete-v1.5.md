# Fixture: a complete card block for the v1.5.0 unit card schema (must pass template-fill)

```yaml
cell:
  unit_kind: "CELL"
  code: "<[ORG]CELL-INITIALS>"
  full_name: "<Full name>"
  parent: "<code of this AIOC or of its Pod>"
  type: "<from the organisation's list>"
  filler_kind: "<human | ai | human-or-ai>"
  card_version: "<vN.N.N>"
  version: "<N.N.N>"
  lineage: { id: "<code it derives from>", version: "<N.N.N>", relation: "<original | derived | merged | split>" }
  lifecycle_state: "<proposed | designed | built | joined | live | replaced | retired>"
  fixed_test: { id: "<test ID>", version: "<vN>", owner: "<code of the seat>" }
  accountable_to: "<code of the human Cell that this Cell answers to>"
  ports:
    - { unit: "<code>", port: "ai-in", direction: "input", type: "AI", identification: "technical-key", accepted_content: ["<content>"], authority_limit: "<limit>", audit_trail: "<where>", required_tests: ["<test>"], enforcement: "shared-gateway-outside-unit" }
    - { unit: "<code>", port: "stop", direction: "input", type: "HU", identification: "live-human-sign-in-at-gateway", accepted_content: ["stop"], authority_limit: "stop only", audit_trail: "<where>", required_tests: ["<test>"], enforcement: "shared-gateway-outside-unit", stop_door: true }
```

Superseded (fixture) by the block above; kept as written:

```yaml
cell:
  unit_kind: "CELL"
```
