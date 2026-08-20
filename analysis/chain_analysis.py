"""
Chain-level analysis utilities.

This module transforms normalized protocol metrics into
chain-level analytical summaries.

The module does not calculate protocol TVL.
It analyzes already-normalized metrics.
"""


def calculate_tvl_by_chain(normalized_data):
    """
    Calculate included TVL for each chain.

    Only metrics marked as included_in_tvl are aggregated.

    Args:
        normalized_data (list[dict]):
            Normalized protocol metrics.

    Returns:
        dict:
            Mapping of chain names to TVL values.
    """

    tvl_by_chain = {}

    for record in normalized_data:

        if not record["included_in_tvl"]:
            continue

        chain = record["chain"]

        if chain is None:
            continue

        tvl_by_chain[chain] = (
                tvl_by_chain.get(chain, 0.0)
                + record["value"]
        )

    return tvl_by_chain


def calculate_borrowed_by_chain(normalized_data):
    """
    Calculate borrowed value for each chain.

    Borrowed metrics are analyzed separately from TVL.

    Args:
        normalized_data (list[dict]):
            Normalized protocol metrics.

    Returns:
        dict:
            Mapping of chain names to borrowed values.
    """

    borrowed_by_chain = {}

    for record in normalized_data:

        if record["metric_type"] != "borrowed":
            continue

        chain = record["chain"]

        if chain is None:
            continue

        borrowed_by_chain[chain] = (
                borrowed_by_chain.get(chain, 0.0)
                + record["value"]
        )

    return borrowed_by_chain


"""
Chain-level analysis utilities.

This module groups normalized protocol metrics by blockchain
so that TVL and borrowed values can be analyzed separately.
"""


def group_metrics_by_chain(normalized_data):

    """
    Group normalized metrics by blockchain.

    Args:
        normalized_data (list[dict]):
            Normalized protocol metrics.

    Returns:
        dict:
            Mapping of chain names to their metrics.
    """

    grouped = {}

    for record in normalized_data:
        chain = record["chain"]

        if chain is None:
            continue

        if chain not in grouped:
            grouped[chain] = []

        grouped[chain].append(record)

    return grouped


def get_chain_tvl(metrics):
    """
    Extract the TVL value for a chain.

    Args:
        metrics (list[dict]):
            Metrics belonging to one chain.

    Returns:
        float:
            Chain TVL, or 0.0 if no TVL metric exists.
    """

    for metric in metrics:
        if metric["metric_type"] == "chain":
            return metric["value"]

    return 0.0


def get_chain_borrowed(metrics):
    """
    Extract the borrowed value for a chain.

    Args:
        metrics (list[dict]):
            Metrics belonging to one chain.

    Returns:
        float:
            Borrowed value, or 0.0 if no borrowed metric exists.
    """

    for metric in metrics:
        if metric["metric_type"] == "borrowed":
            return metric["value"]

    return 0.0