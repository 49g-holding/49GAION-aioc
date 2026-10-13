# Fixture: a complete card block (must pass template-fill)

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
```
