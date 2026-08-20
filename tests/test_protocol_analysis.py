from analysis.protocol_analysis import (
    calculate_borrowed_to_tvl,
    build_chain_summary,
)


def test_calculate_borrowed_to_tvl():

    tvl_by_chain = {
        "Ethereum": 600.0,
        "Base": 300.0,
    }

    borrowed_by_chain = {
        "Ethereum": 400.0,
        "Base": 200.0,
    }

    result = calculate_borrowed_to_tvl(
        tvl_by_chain,
        borrowed_by_chain,
    )

    assert result == {
        "Ethereum": 400 / 600,
        "Base": 200 / 300,
    }


def test_calculate_borrowed_to_tvl_zero_tvl():

    tvl_by_chain = {
        "Ethereum": 0.0,
    }

    borrowed_by_chain = {
        "Ethereum": 100.0,
    }

    result = calculate_borrowed_to_tvl(
        tvl_by_chain,
        borrowed_by_chain,
    )

    assert result == {
        "Ethereum": 0.0,
    }


def test_build_chain_summary():

    tvl_by_chain = {
        "Ethereum": 600.0,
        "Base": 300.0,
    }

    borrowed_by_chain = {
        "Ethereum": 400.0,
        "Base": 200.0,
    }

    result = build_chain_summary(
        tvl_by_chain,
        borrowed_by_chain,
    )

    assert result == {
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