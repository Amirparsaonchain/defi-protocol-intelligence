# Protocol Risk Evidence Ledger

## 1. Concept

Protocol Risk Evidence Ledger is an evidence-first infrastructure for recording, normalizing, and tracing protocol-risk observations over time.

Its purpose is **not** to declare whether a protocol is safe or unsafe.

Its purpose is to answer a narrower and more defensible question:

> **What risk-relevant evidence was observed, when was it observed, where did it come from, what exactly does it support, and what remains unresolved?**

The system is designed for DeFi research, protocol monitoring, and analyst workflows where evidence is fragmented across official documentation, governance, audits, incident reports, deployments, and on-chain observations.

The core design principle is:

> **Record facts and provenance first; derive interpretations second; never silently turn uncertainty into certainty.**

---

## 2. The Problem

Protocol-risk research commonly suffers from five problems:

1. **Evidence fragmentation**
   Relevant information exists across many sources and formats.

2. **Temporal ambiguity**
   A statement that was true yesterday may no longer describe the current protocol.

3. **Weak provenance**
   Analysts often retain conclusions without preserving the exact evidence that produced them.

4. **Observation / interpretation conflation**
   “The contract changed” can become “the protocol is compromised” without a defensible intermediate layer.

5. **Unresolved uncertainty disappearing from the report**
   Missing evidence is often mistaken for evidence of safety.

The Ledger addresses these problems by making evidence and its provenance first-class objects.

---

## 3. What the System Should Solve

The system should solve problems that are fundamentally about **evidence integrity and traceability**.

### 3.1 Evidence capture

Capture a risk-relevant observation together with:

* source
* source type
* retrieval time
* observation time, when known
* protocol / component
* claim or observation
* evidence excerpt or structured value
* source locator
* confidence / evidence quality metadata

### 3.2 Evidence normalization

Represent heterogeneous observations in a common schema so that analysts can compare:

* governance changes
* contract/deployment changes
* admin-control observations
* audit findings
* incidents
* documentation changes
* oracle / dependency observations
* operational signals

without pretending that these signals are equivalent.

### 3.3 Temporal traceability

Preserve the difference between:

* when an event happened,
* when it was published,
* when it was retrieved,
* and when the system observed it.

The system must not overwrite historical evidence merely because newer evidence exists.

### 3.4 Provenance

Every material claim should be traceable to one or more evidence records.

A reviewer should be able to move:

`Conclusion → Claim → Evidence → Source`

without relying on undocumented analyst memory.

### 3.5 Conflict and uncertainty representation

The Ledger should preserve conflicting evidence instead of forcing an immediate winner.

Example:

* Source A: admin key is controlled by a multisig.
* Source B: a newer deployment introduces a different owner.
* Current state: unresolved until verified.

The system records the conflict and exposes it.

### 3.6 Evidence-backed risk indicators

The system may derive structured indicators such as:

* evidence freshness
* source diversity
* unresolved conflicts
* concentration of privileged control
* presence of known unresolved findings
* change frequency

But these indicators must remain traceable to their underlying evidence.

---

## 4. What the System Should NOT Solve

This boundary is critical.

### 4.1 It should NOT declare protocol safety

The Ledger must not produce a simplistic:

> SAFE / UNSAFE

verdict.

Protocol safety is context-dependent and cannot be established from a finite evidence ledger alone.

### 4.2 It should NOT replace expert risk assessment

The system supports analysts.

It does not claim to replace:

* security researchers
* auditors
* protocol engineers
* governance experts
* legal/compliance professionals

### 4.3 It should NOT infer incidents from weak signals alone

For example:

> “Contract changed” ≠ “exploit occurred.”

The system may flag the change as risk-relevant evidence, but incident classification requires stronger evidence.

### 4.4 It should NOT treat missing evidence as negative evidence

Absence of a source or observation means:

> **Not observed / unknown**

not:

> **Safe / absent**

### 4.5 It should NOT create false precision

Risk scores are dangerous when their mathematical meaning is unclear.

Any derived score must have:

* explicit inputs
* deterministic calculation
* documented interpretation
* visible uncertainty

The MVP should prefer explainable indicators over a single opaque risk score.

### 4.6 It should NOT become a generic blockchain database

The goal is not to ingest everything.

Data should enter the Ledger only when it contributes to protocol-risk evidence or its provenance.

---

## 5. What the System Should Record

The Ledger should record **observations and evidence**, not unsupported conclusions.

Examples:

### Record

> “On 2026-08-20, the observed owner address for component X was Y.”

### Do not record as fact

> “The protocol is centralized and unsafe.”

The second statement may be an analyst interpretation derived from multiple observations, but it must not masquerade as a raw fact.

---

## 6. Evidence Hierarchy

Evidence should carry quality metadata rather than a universal hard-coded truth ranking.

Useful source categories include:

1. **Direct on-chain observation**
2. **Official protocol source**
3. **Governance record**
4. **Security audit / formal report**
5. **Incident disclosure**
6. **Independent technical research**
7. **Reputable secondary reporting**
8. **Unverified community claim**

Source quality and claim relevance are separate dimensions.

A high-quality source can still be irrelevant to a particular claim.

---

## 7. Core Data Flow

```text
Source
  ↓
Retrieval
  ↓
Evidence Item
  ↓
Normalized Observation
  ↓
Claim
  ↓
Relationship / Support
  ↓
Analyst Interpretation
  ↓
Risk Indicator / Report
```

The system must preserve the distinction between each layer.

---

## 8. Claim vs Observation

This distinction is central.

### Observation

Something directly represented by the evidence.

Example:

> “The owner field returned address 0xABC.”

### Claim

A proposition supported by one or more observations.

Example:

> “Component X currently has a privileged owner.”

### Interpretation

An analyst-level inference.

Example:

> “The observed privileged control represents a governance concentration risk.”

### Decision

A human or downstream workflow decision.

Example:

> “Require additional verification before allocating capital.”

The Ledger should support all four layers while preventing them from being silently collapsed.

---

## 9. Conflict Model

Conflicts are first-class.

If two evidence items disagree, the system should represent:

```text
Claim
├── Evidence A → supports
└── Evidence B → contradicts
```

The Ledger does not automatically delete or overwrite either item.

Resolution can occur later through:

* newer evidence
* stronger source
* direct verification
* analyst review

A resolved conflict must retain its history.

---

## 10. Temporal Model

At minimum, the system should distinguish:

### observed_at

When the underlying state/event was observed or occurred.

### published_at

When the source published the information, if available.

### retrieved_at

When the Ledger retrieved the source.

### effective_from / effective_to

Optional validity interval for claims whose applicability can be established.

Unknown timestamps must remain unknown.

Do not fabricate timestamps.

---

## 11. MVP

The MVP should demonstrate one complete evidence lifecycle.

Example:

```text
Aave
↓
official source / on-chain observation
↓
evidence item
↓
normalized observation
↓
claim
↓
support relationship
↓
research report
```

The MVP should prioritize:

* deterministic behavior
* reproducibility
* provenance
* temporal awareness
* explicit uncertainty
* testability

over feature count.

---

## 12. Judge-Facing Value Proposition

The strongest claim is not:

> “We predict protocol risk.”

It is:

> **“We make protocol-risk evidence traceable, time-aware, conflict-aware, and reproducible.”**

This is a narrower claim, but it is technically defensible.

A judge should be able to inspect an output and ask:

* Where did this fact come from?
* When was it observed?
* What exactly does the source say?
* Which claim does it support?
* Is there conflicting evidence?
* What is known versus unknown?
* Can the result be reproduced?

The Ledger should answer these questions explicitly.

---

## 13. Design Principle

> **Evidence is immutable history; interpretation is revisable.**

Raw evidence should not be silently rewritten.

Interpretations may change when new evidence arrives.

This allows the system to evolve without destroying the historical research trail.

---

## 14. Success Criteria

A successful prototype demonstrates that a protocol-risk observation can be:

1. captured,
2. sourced,
3. timestamped,
4. normalized,
5. linked to a claim,
6. challenged by conflicting evidence,
7. interpreted without overstating certainty,
8. reproduced from the underlying records.

That is the core product.

Everything else is secondary.
