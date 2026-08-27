# Protocol Risk Evidence Ledger — Data Model

## 1. Modeling Goal

The data model must preserve a strict distinction between:

```text
Source
  ↓
Evidence
  ↓
Observation
  ↓
Claim
  ↓
Interpretation
  ↓
Decision
```

The model is designed for provenance, temporal reasoning, conflict preservation, and reproducible research.

It must not collapse raw evidence into a final risk score.

---

## 2. Entity Overview

Core entities:

1. `Protocol`
2. `Component`
3. `Source`
4. `Retrieval`
5. `EvidenceItem`
6. `Observation`
7. `Claim`
8. `ClaimEvidenceLink`
9. `Interpretation`
10. `RiskIndicator`
11. `Conflict`
12. `ResearchSnapshot`

Optional later entities:

* `Address`
* `Deployment`
* `GovernanceAction`
* `AuditFinding`
* `Incident`
* `Dependency`

The MVP does not require every optional entity.

---

## 3. Protocol

Represents the protocol under research.

```text
Protocol
--------
id
name
slug
description
official_url
created_at
updated_at
```

Rules:

* `id` is stable.
* `official_url` identifies the protocol's official source domain.
* Do not treat the official URL as proof of every protocol claim.

---

## 4. Component

Represents a protocol subsystem or contract relevant to an observation.

```text
Component
---------
id
protocol_id
name
component_type
chain
address
description
created_at
updated_at
```

Possible `component_type` values:

* contract
* governance
* oracle
* bridge
* treasury
* frontend
* deployment
* dependency
* other

Rules:

* A protocol can have many components.
* An address may be unknown.
* A component can change over time; historical observations must not be overwritten.

---

## 5. Source

Represents the origin of evidence.

```text
Source
------
id
source_type
title
url
publisher
canonical_identifier
first_seen_at
last_seen_at
```

Example `source_type` values:

* on_chain
* official_docs
* governance
* audit
* incident_report
* technical_research
* secondary_reporting
* community

Rules:

* Source identity and source quality are separate concepts.
* A source must not receive a universal “truth score.”
* A source can support some claims and be irrelevant to others.

---

## 6. Retrieval

Represents a specific retrieval of a source.

```text
Retrieval
---------
id
source_id
retrieved_at
http_status
content_hash
content_location
retrieval_method
```

Purpose:

* preserve when the Ledger accessed the source,
* enable reproducibility,
* detect content changes.

`content_hash` should be generated from the retrieved representation when technically appropriate.

---

## 7. EvidenceItem

The immutable evidence record.

```text
EvidenceItem
------------
id
retrieval_id
protocol_id
component_id
evidence_type
excerpt
structured_value
locator
observed_at
published_at
retrieved_at
created_at
```

Possible `evidence_type` values:

* state_observation
* event
* governance_action
* documentation_statement
* audit_finding
* incident_statement
* deployment_change
* configuration_observation
* metric_observation
* other

Important rule:

> EvidenceItem represents what was observed from a source. It does not represent the analyst's conclusion.

`excerpt` may contain a short source passage.

`structured_value` stores machine-readable data when available.

`locator` identifies where the evidence can be found, e.g.:

* URL fragment
* document section
* page number
* transaction hash
* block number
* contract storage slot

---

## 8. Observation

Normalizes an evidence item into a structured fact.

```text
Observation
-----------
id
evidence_id
subject_type
subject_id
attribute
value
value_type
unit
observed_at
valid_from
valid_to
normalization_method
```

Example:

```text
subject = Component: lending_pool
attribute = owner
value = 0xABC...
value_type = address
observed_at = 2026-08-20T18:00:00Z
```

Rules:

* Observation must remain traceable to EvidenceItem.
* Unknown values remain unknown.
* Normalization must be deterministic and documented.

---

## 9. Claim

A proposition that can be supported or challenged.

```text
Claim
-----
id
protocol_id
component_id
claim_type
statement
status
created_at
updated_at
```

Possible `status` values:

* proposed
* supported
* disputed
* unresolved
* resolved
* deprecated

Examples:

```text
“The lending pool has a privileged owner.”
```

or:

```text
“The latest observed deployment uses implementation X.”
```

A Claim is not raw evidence.

---

## 10. ClaimEvidenceLink

Connects claims to evidence.

```text
ClaimEvidenceLink
-----------------
id
claim_id
evidence_id
relationship
rationale
created_at
```

Possible `relationship` values:

* supports
* contradicts
* contextualizes
* supersedes
* partially_supports

This is the main mechanism for conflict-aware provenance.

---

## 11. Interpretation

Represents analyst-level reasoning.

```text
Interpretation
--------------
id
claim_id
statement
interpretation_type
confidence
rationale
created_at
updated_at
```

Example:

```text
Claim:
“The lending pool has a privileged owner.”

Interpretation:
“Privileged control may create governance concentration risk.”
```

Rules:

* Interpretations must cite the claims they depend on.
* Interpretation confidence must not be confused with source truth.
* An interpretation may be revised without rewriting evidence.

---

## 12. RiskIndicator

Represents a deterministic, explainable derived signal.

```text
RiskIndicator
-------------
id
protocol_id
indicator_type
value
unit
calculated_at
method_version
inputs
```

Examples:

* unresolved_claim_count
* evidence_age
* source_diversity
* privileged_control_count
* conflicting_evidence_count

Rules:

* Every indicator must have explicit inputs.
* `method_version` identifies the calculation logic.
* Indicators are not equivalent to a global protocol safety score.

---

## 13. Conflict

Represents an unresolved or resolved disagreement.

```text
Conflict
--------
id
claim_id
status
description
opened_at
resolved_at
resolution_method
resolution_note
```

Possible `status`:

* open
* resolved
* superseded

A conflict should preserve the evidence on both sides through `ClaimEvidenceLink`.

---

## 14. ResearchSnapshot

Represents a reproducible research state at a point in time.

```text
ResearchSnapshot
----------------
id
protocol_id
created_at
as_of
model_version
source_set
claim_set
indicator_set
```

Purpose:

> Reproduce what the analyst knew at a particular point in time.

A snapshot should reference immutable IDs rather than copying all underlying data.

---

## 15. Relationship Diagram

```text
Protocol
  │
  ├── Component
  │
  ├── Claim
  │     │
  │     ├── ClaimEvidenceLink ─── EvidenceItem
  │     │                              │
  │     │                              ├── Retrieval ─── Source
  │     │                              │
  │     │                              └── Observation
  │     │
  │     ├── Interpretation
  │     │
  │     └── Conflict
  │
  ├── RiskIndicator
  │
  └── ResearchSnapshot
```

---

## 16. Provenance Chain

Every material conclusion should be traversable as:

```text
Interpretation
      ↓
Claim
      ↓
ClaimEvidenceLink
      ↓
EvidenceItem
      ↓
Retrieval
      ↓
Source
```

For structured facts:

```text
Interpretation
      ↓
Claim
      ↓
Observation
      ↓
EvidenceItem
      ↓
Source
```

This chain is a core acceptance criterion.

---

## 17. Temporal Semantics

The model intentionally separates:

### observed_at

When the underlying observation was made.

### published_at

When the source published the information.

### retrieved_at

When the Ledger retrieved it.

### valid_from / valid_to

When the observation is known to apply.

These fields must never be silently substituted for one another.

If a timestamp is unavailable:

```text
NULL / unknown
```

is preferable to fabrication.

---

## 18. Immutability Rules

### Immutable

* EvidenceItem
* Retrieval
* source content hash
* historical Observation records

### Revisable

* Claim status
* Interpretation
* Conflict resolution
* RiskIndicator calculation versions

A new observation should create a new record rather than mutate historical evidence.

---

## 19. Uncertainty Rules

The model must distinguish:

```text
Observed
Not observed
Unknown
Conflicting
Inferred
```

These states must never be collapsed into a binary true/false field when doing so would destroy meaning.

Example:

> No audit was found.

This means:

```text
audit_found = unknown
```

unless the search process itself establishes a sufficiently scoped negative result.

---

## 20. MVP Implementation Strategy

Do not immediately build a full database.

Start with:

```text
Python domain models
        ↓
JSON / JSONL persistence
        ↓
Deterministic validation
        ↓
Evidence → Claim → Report pipeline
```

Once the model is stable, storage can evolve toward SQLite/PostgreSQL or another appropriate backend.

The data model is more important than the storage engine at this stage.

---

## 21. MVP Acceptance Tests

The implementation should be able to demonstrate:

### Test 1 — Evidence creation

Create an evidence item with source and retrieval metadata.

### Test 2 — Observation normalization

Convert evidence into a structured observation.

### Test 3 — Claim creation

Create a claim supported by evidence.

### Test 4 — Provenance traversal

Start at a claim and retrieve its evidence and source.

### Test 5 — Conflict

Attach one supporting and one contradicting evidence item to the same claim.

### Test 6 — Temporal update

Add newer evidence without deleting older evidence.

### Test 7 — Unknown state

Represent missing information as unknown rather than safe.

### Test 8 — Reproducibility

Generate the same indicator from the same versioned inputs.

---

## 22. Design Constraint

The database should never answer:

> “Is this protocol safe?”

It should answer:

> “What evidence do we have, how strong and current is it, what claims does it support or contradict, and what remains unresolved?”

That distinction is the architectural boundary of the project.
