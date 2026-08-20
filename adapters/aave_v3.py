"""
Aave V3 TVL adapter.

This module currently provides the structure for reconstructing
Aave V3 TVL from protocol-specific data.

The final implementation will connect:
DeFiLlama methodology
        ↓
Aave V3 data
        ↓
eligible assets
        ↓
token balances
        ↓
token prices
        ↓
USD valuation
        ↓
TVL
"""


def calculate_tvl(chain_tvls):
    """
    Calculate Aave V3 TVL from chain-level data.

    Borrowed values are excluded because borrowed assets
    represent active loans rather than protocol TVL.

    Args:
        chain_tvls (dict):
            Mapping of chain/metric names to USD values.

    Returns:
        float:
            Calculated TVL in USD.
    """

    total_tvl = 0.0

    for key, value in chain_tvls.items():

        # Exclude aggregate and chain-specific borrowed metrics.
        if key == "borrowed" or key.endswith("-borrowed"):
            continue

        # Ignore missing values.
        if value is None:
            continue

        # Add eligible chain-level TVL.
        total_tvl += float(value)

    return total_tvl
