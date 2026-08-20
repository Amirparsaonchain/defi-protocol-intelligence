from src.api_client import get_protocols
from src.data_loader import protocols_to_dataframe
from src.validators import validate_protocol_dataframe


def test_get_protocols_returns_data():
    protocols = get_protocols()

    assert protocols is not None
    assert isinstance(protocols, list)
    assert len(protocols) > 0


def test_protocol_dataframe_has_required_columns():
    protocols = get_protocols()
    df = protocols_to_dataframe(protocols)

    validate_protocol_dataframe(df)

    required_columns = {
        "name",
        "category",
        "chain",
        "tvl"
    }

    assert required_columns.issubset(df.columns)