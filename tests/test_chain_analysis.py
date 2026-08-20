from src.tvl_processor import normalize_chain_tvls

from analysis.chain_analysis import (
    group_metrics_by_chain,
    get_chain_tvl,
    get_chain_borrowed, calculate_tvl_by_chain, calculate_borrowed_by_chain,
)


def test_calculate_tvl_by_chain():
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
    ]

    result = calculate_tvl_by_chain(normalized_data)

    assert result == {
        "Ethereum": 1000.0,
        "Base": 500.0,
    }


def test_calculate_borrowed_by_chain():
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
            "key": "Base-borrowed",
            "chain": "Base",
            "metric_type": "borrowed",
            "value": 200.0,
            "included_in_tvl": False,
        },
    ]

    result = calculate_borrowed_by_chain(normalized_data)

    assert result == {
        "Ethereum": 400.0,
        "Base": 200.0,
    }


def test_group_metrics_by_chain():
    chain_tvls = {
        "Ethereum": 600,
        "Ethereum-borrowed": 400,
        "Base": 300,
        "Base-borrowed": 200,
    }

    normalized_data = normalize_chain_tvls(chain_tvls)

    grouped = group_metrics_by_chain(normalized_data)

    assert set(grouped.keys()) == {"Ethereum", "Base"}

    assert len(grouped["Ethereum"]) == 2
    assert len(grouped["Base"]) == 2


def test_get_chain_tvl():
    chain_tvls = {
        "Ethereum": 600,
        "Ethereum-borrowed": 400,
        "Base": 300,
        "Base-borrowed": 200,
    }

    normalized_data = normalize_chain_tvls(chain_tvls)
    grouped = group_metrics_by_chain(normalized_data)

    assert get_chain_tvl(grouped["Ethereum"]) == 600
    assert get_chain_tvl(grouped["Base"]) == 300


def test_get_chain_borrowed():
    chain_tvls = {
        "Ethereum": 600,
        "Ethereum-borrowed": 400,
        "Base": 300,
        "Base-borrowed": 200,
    }

    normalized_data = normalize_chain_tvls(chain_tvls)
    grouped = group_metrics_by_chain(normalized_data)

    assert get_chain_borrowed(grouped["Ethereum"]) == 400
    assert get_chain_borrowed(grouped["Base"]) == 200
