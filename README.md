# DeFi Protocol Intelligence

**Protocol-aware DeFi research and data intelligence**

DeFi Protocol Intelligence is a Python-based research pipeline for analyzing DeFi protocols from raw protocol-level data while preserving the methodology and provenance behind the resulting metrics.

The project currently uses the **DeFiLlama API** as its primary data source and is designed so that the analytical layer can remain independent from the underlying acquisition source.

## Why this project exists

A raw DeFi metric is not automatically a meaningful analytical metric.

For example, a protocol may expose multiple values through a dataset:

* chain-level TVL
* borrowed value
* aggregate metrics
* protocol-specific components

Simply summing these values can produce misleading results.

This project therefore separates:

**data acquisition → validation → normalization → methodology → analysis → reporting**

The goal is to make analytical results more transparent, reproducible, and traceable.

---

## Current pipeline

```text
DeFiLlama API
      │
      ▼
Raw protocol data
      │
      ▼
DataFrame conversion
      │
      ▼
Validation
      │
      ▼
Protocol selection
      │
      ▼
Official source discovery
      │
      ▼
Methodology resolution
      │
      ▼
Metric normalization
      │
      ▼
Methodology-aware analysis
      │
      ├── Chain-level analysis
      │
      └── Protocol-level analysis
      │
      ▼
Research-ready output
```

The current implementation runs the pipeline against **Aave V3**.

---

## Core research principles

### 1. Methodology before interpretation

A numerical value should not automatically be given a financial interpretation.

For example:

```text
borrowed / TVL
```

may be analytically useful, but it should not automatically be interpreted as protocol utilization without establishing the accounting definitions behind the underlying values.

### 2. Missing ≠ zero

A missing value means the required information is unavailable.

A zero means the source explicitly reports zero.

The pipeline therefore avoids silently converting missing observations into zeros.

### 3. Preserve provenance

Analytical metrics should remain traceable through:

```text
Source dataset
      ↓
Original field
      ↓
Normalization rule
      ↓
Transformation
      ↓
Formula
      ↓
Final analytical value
```

### 4. Separate acquisition from analysis

The analytical layer is designed to remain independent from the current data source.

This makes it possible to evolve the acquisition layer toward:

* RPC data
* blockchain indexers
* protocol-specific APIs
* direct on-chain queries

without requiring the entire analytical layer to be rewritten.

---

## Example: methodology-aware TVL

For Aave V3, the project treats eligible collateral/deposit balances as the basis for TVL and excludes borrowed coins from the TVL calculation.

Conceptually:

```text
TVL = Σ(eligible token balance × token price)
```

The project also keeps borrowed values separate rather than automatically incorporating them into TVL.

See:

* [`methodology/aave_v3.md`](methodology/aave_v3.md)
* [`methodology/metrics.md`](methodology/metrics.md)

---

## Repository structure

```text
defi-protocol-intelligence/
│
├── adapters/          # Data-source / integration adapters
├── analysis/          # Analytical layer
├── data/              # Local data and analytical artifacts
├── methodology/       # Protocol and metric methodology
├── notebooks/         # Exploratory analysis
├── reports/           # Research outputs
├── src/               # Core pipeline components
├── tests/              # Automated tests
│
├── main.py            # Pipeline entry point
├── requirements.txt   # Python dependencies
└── README.md
```

---

## Main components

### Data acquisition

Retrieves protocol data from the current external data source.

### Validation

Checks that the acquired protocol dataset satisfies the expected structural requirements before analysis.

### Protocol selection

Selects the protocol to analyze from the acquired dataset.

### Source discovery

Identifies official protocol sources that can be used to establish methodology.

### Methodology resolution

Connects the protocol with the relevant methodology used to interpret its metrics.

### Metric normalization

Transforms heterogeneous protocol metric structures into normalized analytical categories.

For example:

```text
Ethereum            → chain
Base                → chain
Ethereum-borrowed   → borrowed
Base-borrowed       → borrowed
borrowed            → borrowed aggregate
```

### Chain-level analysis

Produces metrics such as:

* TVL by chain
* borrowed value by chain

### Protocol-level analysis

Combines normalized chain-level information into protocol-level analytical summaries.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Amirparsaonchain/defi-protocol-intelligence.git
cd defi-protocol-intelligence
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
source .venv/Scripts/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the pipeline

```bash
python main.py
```

The current pipeline selects **Aave V3**, resolves its methodology sources, normalizes its chain-level metrics, performs chain-level analysis, and produces baseline and methodology-aware TVL outputs.

---

## Run tests

```bash
pytest
```

The test suite is intended to protect the contracts between the pipeline's acquisition, validation, normalization, methodology, and analysis layers.

---

## Research outputs

The repository is intended to evolve beyond raw numerical output toward research artifacts that make the following explicit:

* What was observed?
* Where did the observation come from?
* How was it normalized?
* Which methodology supports its interpretation?
* What transformation produced the final metric?
* What limitations remain?

This distinction is important because a reproducible number is not necessarily a valid interpretation.

---

## Current limitations

This project is still under active development.

Current limitations include:

* DeFiLlama remains the primary acquisition source.
* The current implementation focuses on Aave V3.
* Some analytical metrics depend on assumptions that require protocol-specific methodology validation.
* Direct on-chain verification is not yet the primary acquisition path.
* Research outputs and evidence tracking are still being expanded.

These limitations are intentionally documented rather than hidden.

---

## Research direction

The project is evolving toward a broader **protocol intelligence and evidence architecture**.

The intended direction is:

```text
Raw observations
      ↓
Normalized data
      ↓
Protocol methodology
      ↓
Analytical claims
      ↓
Evidence / provenance
      ↓
Research-ready intelligence
```

A separate experimental branch explores an **evidence-ledger architecture** for preserving protocol observations, claims, and supporting evidence.

---

## Status

**Active research / portfolio project**

The current priority is to strengthen:

1. protocol-aware data modeling
2. methodology resolution
3. metric normalization
4. analytical validation
5. provenance and evidence tracking
6. research-ready reporting

---

## License

License to be added.
