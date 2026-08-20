"""
Protocol selection utilities.

This module provides reusable functions for selecting
protocol records from the protocol DataFrame.
"""


def select_protocol(df, protocol_name):
    """
    Select a single protocol by name.

    Args:
        df (pandas.DataFrame):
            Protocol dataset.

        protocol_name (str):
            Exact protocol name to select.

    Returns:
        pandas.Series:
            Selected protocol record.

    Raises:
        ValueError:
            If the protocol does not exist or multiple
            records match the requested name.
    """

    matches = df[df["name"] == protocol_name]

    if len(matches) == 0:
        raise ValueError(f"Protocol not found: {protocol_name}")

    if len(matches) > 1:
        raise ValueError(
            f"Multiple protocols found: {protocol_name}"
        )

    return matches.iloc[0]
