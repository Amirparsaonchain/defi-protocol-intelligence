"""
Protocol reporting utilities.

This module converts analytical protocol metrics into
a research-ready tabular representation.

It does not fetch, normalize, classify, or calculate
raw protocol metrics.
"""

import pandas as pd


def summary_to_dataframe(summary):
    """
    Convert a protocol chain summary into a Pandas DataFrame.

    Args:
        summary (dict):
            Mapping of chain names to analytical metrics.

    Returns:
        pandas.DataFrame:
            One row per chain with TVL, borrowed value,
            and borrowed-to-TVL ratio.
    """

    records = []

    for chain, metrics in summary.items():

        records.append(
            {
                "chain": chain,
                "tvl": metrics["tvl"],
                "borrowed": metrics["borrowed"],
                "borrowed_to_tvl": metrics["borrowed_to_tvl"],
            }
        )

    return pd.DataFrame(records)


def sort_summary_by_tvl(summary_df):
    """
    Sort a protocol summary by TVL in descending order.

    Args:
        summary_df (pandas.DataFrame):
            Protocol chain summary.

    Returns:
        pandas.DataFrame:
            Summary sorted from highest to lowest TVL.
    """

    return summary_df.sort_values(
        "tvl",
        ascending=False,
    ).reset_index(drop=True)