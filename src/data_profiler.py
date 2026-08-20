import pandas as pd


def get_overview(df):
    print("=== DATASET OVERVIEW ===")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print()

    print("=== COLUMNS ===")
    for column in df.columns:
        print(column)


def get_dtypes(df):
    print("=== DATA TYPES ===")
    print(df.dtypes)


def get_missing_values(df):
    print("=== MISSING VALUES ===")

    missing = df.isna().sum()

    result = missing[missing > 0].sort_values(
        ascending=False
    )

    print(result)


def get_category_values(df):
    print("=== CATEGORIES ===")
    print(df["category"].value_counts(dropna=False))


def get_chain_values(df):
    print("=== CHAINS ===")
    print(df["chain"].value_counts(dropna=False))


def inspect_column(df, column_name, n=5):
    print(f"=== INSPECTING: {column_name} ===")

    values = df[column_name].dropna().head(n)

    for index, value in values.items():
        print(f"\nINDEX: {index}")
        print(f"TYPE: {type(value)}")
        print(f"VALUE: {value}")


def inspect_protocol(df, protocol_name):
    matches = df[df["name"].str.contains(
        protocol_name,
        case=False,
        na=False
    )]

    print(f"=== PROTOCOL: {protocol_name} ===")
    print(matches.to_string())


def profile_nested_column(df, column_name):
    print(f"=== NESTED COLUMN PROFILE: {column_name} ===")

    type_counts = (
        df[column_name]
        .map(lambda x: type(x).__name__)
        .value_counts(dropna=False)
    )

    print(type_counts)


def profile_empty_nested_values(df, column_name):
    values = df[column_name]

    empty_count = values.apply(
        lambda x: x is None
                  or x != x
                  or x == {}
                  or x == []
    ).sum()

    print(
        f"{column_name} empty values: {empty_count}"
    )


def classify_nested_keys(df, column_name):
    keys = set()

    for value in df[column_name]:
        if isinstance(value, dict):
            keys.update(value.keys())

    print(f"=== KEY ANALYSIS: {column_name} ===")
    print(f"Unique keys: {len(keys)}")

    borrowed = [
        key for key in keys
        if "borrowed" in key.lower()
    ]

    print(f"\nKeys containing 'borrowed': {len(borrowed)}")
    print(borrowed[:50])


def analyze_key_suffixes(df, column_name):
    keys = set()

    for value in df[column_name]:
        if isinstance(value, dict):
            keys.update(value.keys())

    suffixes = {}

    for key in keys:
        if "-" in key:
            suffix = key.rsplit("-", 1)[1]

            suffixes.setdefault(suffix, 0)
            suffixes[suffix] += 1

    print("=== KEY SUFFIX ANALYSIS ===")

    for suffix, count in sorted(
            suffixes.items(),
            key=lambda x: x[1],
            reverse=True
    ):
        print(f"{suffix}: {count}")


def analyze_suffix_structure(df, column_name):
    keys = set()

    for value in df[column_name]:
        if isinstance(value, dict):
            keys.update(value.keys())

    suffixes = [
        "borrowed",
        "staking",
        "pool2",
        "vesting",
        "offers",
        "treasury"
    ]

    print("=== SUFFIX STRUCTURE ANALYSIS ===")

    for suffix in suffixes:
        matching = [
            key for key in keys
            if key.lower().endswith(f"-{suffix}")
        ]

        exact = [
            key for key in keys
            if key.lower() == suffix
        ]

        print(f"\n--- {suffix} ---")
        print(f"suffix pattern: {len(matching)}")
        print(f"exact key:      {len(exact)}")

        print("examples:")
        print(matching[:10])

        if exact:
            print("exact matches:", exact)


def analyze_protocol_metric_diversity(df):
    records = []

    for _, row in df.iterrows():
        chain_tvls = row["chainTvls"]

        if not isinstance(chain_tvls, dict):
            continue

        keys = list(chain_tvls.keys())

        records.append({
            "id": row["id"],
            "name": row["name"],
            "category": row["category"],
            "key_count": len(keys),
            "borrowed_count": sum(
                key.lower().endswith("-borrowed")
                or key.lower() == "borrowed"
                for key in keys
            ),
            "staking_count": sum(
                key.lower().endswith("-staking")
                or key.lower() == "staking"
                for key in keys
            ),
            "pool2_count": sum(
                key.lower().endswith("-pool2")
                or key.lower() == "pool2"
                for key in keys
            ),
            "vesting_count": sum(
                key.lower().endswith("-vesting")
                or key.lower() == "vesting"
                for key in keys
            ),
        })

    result = pd.DataFrame(records)

    print("=== PROTOCOL METRIC DIVERSITY ===")
    print(result.sort_values("key_count", ascending=False).head(20))

    return result


def analyze_unknown_keys(df, column_name):
    keys = set()

    for value in df[column_name]:
        if isinstance(value, dict):
            keys.update(value.keys())

    known_suffixes = {
        "borrowed",
        "staking",
        "pool2",
        "vesting",
        "offers",
        "treasury"
    }

    unknown_keys = []

    for key in keys:
        key_lower = key.lower()

        is_known = (
                key_lower in known_suffixes
                or any(
                    key_lower.endswith(f"-{suffix}")
                    for suffix in known_suffixes
                )
        )

        if not is_known:
            unknown_keys.append(key)

    print("=== UNKNOWN KEY ANALYSIS ===")
    print(f"Total unknown keys: {len(unknown_keys)}")
    print("\nExamples:")

    for key in sorted(unknown_keys)[:100]:
        print(key)

    return unknown_keys
