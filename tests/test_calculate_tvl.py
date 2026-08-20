from adapters.aave_v3 import calculate_tvl


def test_calculate_tvl_excludes_borrowed():
    chain_tvls = {
        "Ethereum": 1000,
        "Base": 500,
        "Ethereum-borrowed": 800,
        "Base-borrowed": 200,
        "borrowed": 10000,
    }

    result = calculate_tvl(chain_tvls)

    assert result == 1500
