REQUIRED_PROTOCOL_COLUMNS = {
    "name",
    "category",
    "chain",
    "tvl"
}


def validate_protocol_dataframe(df):
    missing_columns = REQUIRED_PROTOCOL_COLUMNS - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    return True
