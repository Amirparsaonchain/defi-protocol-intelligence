import pandas as pd

from analysis.protocol_report import (
    summary_to_dataframe,
    sort_summary_by_tvl,
)


def test_summary_to_dataframe():

    summary = {
        "Ethereum": {
            "tvl": 600.0,
            "borrowed": 400.0,
            "borrowed_to_tvl": 400 / 600,
        },
        "Base": {
            "tvl": 300.0,
            "borrowed": 200.0,
            "borrowed_to_tvl": 200 / 300,
        },
    }

    result = summary_to_dataframe(summary)

    assert isinstance(result, pd.DataFrame)

    assert list(result.columns) == [
        "chain",
        "tvl",
        "borrowed",
        "borrowed_to_tvl",
    ]

    assert len(result) == 2


def test_summary_to_dataframe_values():

    summary = {
        "Ethereum": {
            "tvl": 600.0,
            "borrowed": 400.0,
            "borrowed_to_tvl": 400 / 600,
        },
    }

    result = summary_to_dataframe(summary)

    assert result.loc[0, "chain"] == "Ethereum"
    assert result.loc[0, "tvl"] == 600.0
    assert result.loc[0, "borrowed"] == 400.0
    assert result.loc[0, "borrowed_to_tvl"] == 400 / 600


def test_sort_summary_by_tvl():

    summary = {
        "Base": {
            "tvl": 300.0,
            "borrowed": 200.0,
            "borrowed_to_tvl": 200 / 300,
        },
        "Ethereum": {
            "tvl": 600.0,
            "borrowed": 400.0,
            "borrowed_to_tvl": 400 / 600,
        },
    }

    summary_df = summary_to_dataframe(summary)

    result = sort_summary_by_tvl(summary_df)

    assert list(result["chain"]) == [
        "Ethereum",
        "Base",
    ]

    assert list(result["tvl"]) == [
        600.0,
        300.0,
    ]