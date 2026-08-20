# Metric Methodology

## Purpose

This document defines the analytical metrics produced by the
DeFi Protocol Intelligence pipeline.

The project currently uses DeFiLlama API data as its data source.

The analytical layer is designed to remain independent from
the underlying data source so that it can later be adapted
to direct on-chain data.

---

## 1. Reconstructed TVL

### Definition

Reconstructed TVL is the sum of normalized protocol metrics
classified as eligible `chain` metrics.

### Formula

TVL = Σ eligible chain metrics

### Current implementation

The normalization layer classifies:

- `Ethereum` → chain
- `Base` → chain
- `Ethereum-borrowed` → borrowed
- `Base-borrowed` → borrowed
- `borrowed` → borrowed aggregate

Only metrics classified as `chain` are currently included
in the reconstructed TVL.

### Important limitation

This is a reconstruction based on the available DeFiLlama
`chainTvls` structure.

It is not yet claimed to reproduce the underlying accounting
methodology used by the protocol itself.

---

## 2. Borrowed Value

### Definition

Borrowed value represents metrics classified as `borrowed`
in the normalized protocol data.

### Examples

`Ethereum-borrowed`

`Base-borrowed`

`borrowed`

### TVL treatment

Borrowed metrics are currently excluded from reconstructed TVL.

They are analyzed separately.

---

## 3. Borrowed-to-TVL Ratio

### Formula

borrowed_to_tvl = borrowed / TVL

### Interpretation

This metric measures the relative magnitude of the reported
borrowed metric compared with the reported chain metric.

### Important distinction

This metric must not currently be interpreted as protocol
utilization.

The accounting scope and definitions of the underlying metrics
must first be established through protocol methodology research.

### Example

If:

TVL = 600

Borrowed = 400

Then:

borrowed_to_tvl = 400 / 600
                 = 0.667

---

## 4. Missing Values

Missing values are not automatically converted to zero.

A missing value means that the required information is not
available.

Zero means that the source explicitly reports a value of zero.

Replacing missing values with zero would modify the source data
and could invalidate downstream research.

---

## 5. Data Provenance

Every analytical metric should remain traceable to:

1. Source dataset
2. Original field
3. Normalization rule
4. Transformation
5. Formula
6. Final analytical value

---

## 6. Current Data Source

The current implementation uses the DeFiLlama API.

The architecture is intentionally separated so that the
acquisition layer can later be replaced by:

- RPC data
- blockchain indexers
- protocol-specific APIs
- direct on-chain queries

without requiring the analytical layer to be completely
rewritten.