import pandas as pd
import pytest

from src.protocol_selector import select_protocol


def test_select_protocol():
    df = pd.DataFrame(
        {
            "name": ["Aave V3", "Lido", "Uniswap"],
            "value": [100, 200, 300],
        }
    )

    result = select_protocol(df, "Aave V3")

    assert result["name"] == "Aave V3"
    assert result["value"] == 100


def test_select_protocol_not_found():
    df = pd.DataFrame(
        {
            "name": ["Aave V3", "Lido"],
            "value": [100, 200],
        }
    )

    with pytest.raises(ValueError, match="Protocol not found"):
        select_protocol(df, "Unknown")


def test_select_protocol_duplicate():
    df = pd.DataFrame(
        {
            "name": ["Aave V3", "Aave V3", "Lido"],
            "value": [100, 150, 200],
        }
    )

    with pytest.raises(ValueError, match="Multiple protocols found"):
        select_protocol(df, "Aave V3")
