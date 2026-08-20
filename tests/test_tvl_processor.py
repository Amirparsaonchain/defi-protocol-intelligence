from src.tvl_processor import (
    classify_metric,
    normalize_chain_tvls,
    normalized_to_dataframe,
    calculate_tvl,
)


def test_classify_metric():
    assert classify_metric("Ethereum") == ("Ethereum", "chain")
    assert classify_metric("Ethereum-borrowed") == (
        "Ethereum",
        "borrowed",
    )
    assert classify_metric("borrowed") == (None, "borrowed")


def test_normalize_chain_tvls():
    chain_tvls = {
        "Ethereum": 1000,
        "Ethereum-borrowed": 400,
        "Base": 500,
        "borrowed": 600,
    }

    result = normalize_chain_tvls(chain_tvls)

    assert result == [
        {
            "key": "Ethereum",
            "chain": "Ethereum",
            "metric_type": "chain",
            "value": 1000.0,
            "included_in_tvl": True,
        },
        {
            "key": "Ethereum-borrowed",
            "chain": "Ethereum",
            "metric_type": "borrowed",
            "value": 400.0,
            "included_in_tvl": False,
        },
        {
            "key": "Base",
            "chain": "Base",
            "metric_type": "chain",
            "value": 500.0,
            "included_in_tvl": True,
        },
        {
            "key": "borrowed",
            "chain": None,
            "metric_type": "borrowed",
            "value": 600.0,
            "included_in_tvl": False,
        },
    ]


def test_calculate_tvl():
    normalized_data = [
        {
            "key": "Ethereum",
            "chain": "Ethereum",
            "metric_type": "chain",
            "value": 1000.0,
            "included_in_tvl": True,
        },
        {
            "key": "Ethereum-borrowed",
            "chain": "Ethereum",
            "metric_type": "borrowed",
            "value": 400.0,
            "included_in_tvl": False,
        },
        {
            "key": "Base",
            "chain": "Base",
            "metric_type": "chain",
            "value": 500.0,
            "included_in_tvl": True,
        },
        {
            "key": "borrowed",
            "chain": None,
            "metric_type": "borrowed",
            "value": 600.0,
            "included_in_tvl": False,
        },
    ]

    result = calculate_tvl(normalized_data)

    assert result == 1500.0


def test_normalized_to_dataframe():
    chain_tvls = {
        "Ethereum": 1000,
        "Ethereum-borrowed": 400,
        "Base": 500,
    }

    normalized_data = normalize_chain_tvls(chain_tvls)

    df = normalized_to_dataframe(normalized_data)

    assert list(df.columns) == [
        "key",
        "chain",
        "metric_type",
        "value",
        "included_in_tvl",
    ]

    assert len(df) == 3
    assert df.loc[0, "key"] == "Ethereum"
    assert df.loc[1, "metric_type"] == "borrowed"
    assert not df.loc[1, "included_in_tvl"]


def test_tvl_matches_included_metrics():
    chain_tvls = {
        "Ethereum": 1000,
        "Ethereum-borrowed": 400,
        "Base": 500,
        "Base-borrowed": 200,
    }

    normalized_data = normalize_chain_tvls(chain_tvls)

    calculated_tvl = calculate_tvl(normalized_data)

    assert calculated_tvl == 1500.0