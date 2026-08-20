"""
Protocol-level analytical utilities.

This module combines already-processed chain-level metrics
into reusable analytical summaries.

It does not fetch, normalize, or classify raw data.
"""


def calculate_borrowed_to_tvl(tvl_by_chain, borrowed_by_chain):
    """
    Calculate the borrowed-to-TVL ratio for each chain.

    Args:
        tvl_by_chain (dict):
            Mapping of chain names to TVL values.

        borrowed_by_chain (dict):
            Mapping of chain names to borrowed values.

    Returns:
        dict:
            Mapping of chain names to borrowed/TVL ratios.
    """

    ratios = {}

    for chain, tvl in tvl_by_chain.items():

        borrowed = borrowed_by_chain.get(chain, 0.0)

        if tvl == 0:
            ratios[chain] = 0.0
            continue

        ratios[chain] = borrowed / tvl

    return ratios


def build_chain_summary(tvl_by_chain, borrowed_by_chain):
    """
    Build a unified analytical summary for each chain.

    Args:
        tvl_by_chain (dict):
            Mapping of chain names to TVL values.

        borrowed_by_chain (dict):
            Mapping of chain names to borrowed values.

    Returns:
        dict:
            Mapping of chain names to analytical metrics.
    """

    ratios = calculate_borrowed_to_tvl(
        tvl_by_chain,
        borrowed_by_chain,
    )

    summary = {}

    for chain, tvl in tvl_by_chain.items():

        summary[chain] = {
            "tvl": tvl,
            "borrowed": borrowed_by_chain.get(chain, 0.0),
            "borrowed_to_tvl": ratios[chain],
        }

    return summary