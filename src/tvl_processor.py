import pandas as pd

"""
TVL processing utilities.

This module transforms protocol chainTvls data into
a normalized analytical structure and calculates TVL
according to protocol-specific inclusion rules.
"""


def classify_metric(key):
    """
    Classify a chainTvls key by its metric type.

    Args:
        key (str):
            A key from the chainTvls dictionary.

    Returns:
        tuple:
            (chain, metric_type)

    Examples:
        "Ethereum" -> ("Ethereum", "chain")
        "Ethereum-borrowed" -> ("Ethereum", "borrowed")
        "borrowed" -> (None, "borrowed")
    """

    if key == "borrowed":
        return None, "borrowed"

    if key.endswith("-borrowed"):
        chain = key.removesuffix("-borrowed")
        return chain, "borrowed"

    return key, "chain"


def normalize_chain_tvls(chain_tvls):
    """
    Normalize a chainTvls dictionary into a list of records.

    Args:
        chain_tvls (dict):
            Mapping of metric keys to numeric values.

    Returns:
        list[dict]:
            Normalized records containing:
            key, chain, metric_type, value,
            and included_in_tvl.
    """

    normalized = []

    for key, value in chain_tvls.items():

        chain, metric_type = classify_metric(key)

        if value is None:
            continue

        included_in_tvl = metric_type == "chain"

        normalized.append(
            {
                "key": key,
                "chain": chain,
                "metric_type": metric_type,
                "value": float(value),
                "included_in_tvl": included_in_tvl,
            }
        )

    return normalized


def normalized_to_dataframe(normalized_data):
    """
    Convert normalized TVL records into a Pandas DataFrame.

    Args:
        normalized_data (list[dict]):
            Normalized chainTvls records.

    Returns:
        pandas.DataFrame:
            Tabular representation of normalized TVL metrics.
    """

    return pd.DataFrame(normalized_data)


def calculate_tvl(normalized_data):
    """
    Calculate TVL from normalized metric records.

    Borrowed metrics are excluded from TVL.

    Args:
        normalized_data (list[dict]):
            Normalized chainTvls records.

    Returns:
        float:
            Calculated TVL in USD.
    """

    total_tvl = 0.0

    for record in normalized_data:

        if not record["included_in_tvl"]:
            continue

        total_tvl += record["value"]

    return total_tvl
