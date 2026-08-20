from analysis.methodology_analysis import (
    apply_methodology,
    calculate_methodology_tvl,
)


def test_apply_methodology():

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

    methodology = {
        "name": "test_methodology",
        "include_metric_types": ["chain"],
    }

    result = apply_methodology(
        normalized_data,
        methodology,
    )

    assert result[0]["methodology_included"] is True
    assert result[1]["methodology_included"] is False
    assert result[2]["methodology_included"] is True


def test_methodology_does_not_change_original_records():

    normalized_data = [
        {
            "key": "Ethereum",
            "chain": "Ethereum",
            "metric_type": "chain",
            "value": 1000.0,
            "included_in_tvl": True,
        }
    ]

    methodology = {
        "name": "test_methodology",
        "include_metric_types": ["chain"],
    }

    result = apply_methodology(
        normalized_data,
        methodology,
    )

    assert "methodology_included" not in normalized_data[0]
    assert result[0]["methodology_included"] is True


def test_calculate_methodology_tvl():

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

    methodology = {
        "name": "test_methodology",
        "include_metric_types": ["chain"],
    }

    result = calculate_methodology_tvl(
        normalized_data,
        methodology,
    )

    assert result == 1500.0


def test_methodology_can_define_different_inclusion_rules():

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
    ]

    methodology = {
        "name": "custom_methodology",
        "include_metric_types": ["borrowed"],
    }

    result = calculate_methodology_tvl(
        normalized_data,
        methodology,
    )

    assert result == 400.0


def test_unknown_metric_types_are_excluded():

    normalized_data = [
        {
            "key": "Ethereum",
            "chain": "Ethereum",
            "metric_type": "chain",
            "value": 1000.0,
            "included_in_tvl": True,
        },
        {
            "key": "Ethereum-staking",
            "chain": "Ethereum",
            "metric_type": "staking",
            "value": 200.0,
            "included_in_tvl": True,
        },
    ]

    methodology = {
        "name": "test_methodology",
        "include_metric_types": ["chain"],
    }

    result = apply_methodology(
        normalized_data,
        methodology,
    )

    assert result[0]["methodology_included"] is True
    assert result[1]["methodology_included"] is False
