from src.api_client import get_protocols
from src.data_loader import protocols_to_dataframe
from src.validators import validate_protocol_dataframe
from src.protocol_selector import select_protocol

from src.tvl_processor import (
    normalize_chain_tvls,
    calculate_tvl,
)

from analysis.chain_analysis import (
    calculate_tvl_by_chain,
    calculate_borrowed_by_chain,
)

from analysis.protocol_analysis import (
    build_chain_summary,
)

from analysis.protocol_report import (
    summary_to_dataframe,
    sort_summary_by_tvl,
)

from analysis.methodology_analysis import (
    calculate_methodology_tvl,
)

from src.source_discovery import discover_sources

from src.methodology_resolver import (
    resolve_methodology,
)


def main():
    """
    Run the DeFi protocol intelligence pipeline.

    Program flow:

    API
    ↓
    Raw protocol data
    ↓
    DataFrame
    ↓
    Validation
    ↓
    Protocol selection
    ↓
    Official source discovery
    ↓
    Methodology resolution
    ↓
    Metric normalization
    ↓
    Methodology-aware analysis
    ↓
    Chain-level analysis
    ↓
    Protocol-level analysis
    ↓
    Research-ready report
    """

    # ---------------------------------------------------------
    # 1. Fetch protocol data
    # ---------------------------------------------------------

    protocols = get_protocols()

    # ---------------------------------------------------------
    # 2. Convert raw data to DataFrame
    # ---------------------------------------------------------

    df = protocols_to_dataframe(protocols)

    # ---------------------------------------------------------
    # 3. Validate the protocol dataset
    # ---------------------------------------------------------

    validate_protocol_dataframe(df)

    # ---------------------------------------------------------
    # 4. Select protocol
    # ---------------------------------------------------------

    protocol = select_protocol(
        df,
        "Aave V3",
    )

    protocol_name = protocol["name"]

    chain_tvls = protocol["chainTvls"]

    # ---------------------------------------------------------
    # 5. Discover official protocol sources
    # ---------------------------------------------------------

    sources = discover_sources(
        protocol_name
    )

    print(
        f"\n=== {protocol_name.upper()} OFFICIAL SOURCES ==="
    )

    for source in sources:
        print(
            f"{source['type']}: "
            f"{source['name']} - "
            f"{source['url']}"
        )

    # ---------------------------------------------------------
    # 6. Prepare sources for methodology resolution
    # ---------------------------------------------------------

    methodology_sources = {}

    for source in sources:
        methodology_sources[source["type"]] = source["url"]

    methodology = resolve_methodology(
        protocol_name,
        methodology_sources,
    )

    print(
        f"\n=== {protocol_name.upper()} METHODOLOGY SOURCE ==="
    )

    print(
        f"Type: {methodology['source_type']}"
    )

    print(
        f"URL: {methodology['source_url']}"
    )
    # ---------------------------------------------------------
    # 7. Normalize protocol metrics
    # ---------------------------------------------------------

    normalized_data = normalize_chain_tvls(
        chain_tvls
    )

    print(
        f"\n=== {protocol_name.upper()} NORMALIZATION ==="
    )

    # ---------------------------------------------------------
    # 8. Apply resolved methodology
    # ---------------------------------------------------------

    methodology_tvl = calculate_methodology_tvl(
        normalized_data,
        methodology,
    )

    # ---------------------------------------------------------
    # 9. Analyze metrics by chain
    # ---------------------------------------------------------

    tvl_by_chain = calculate_tvl_by_chain(
        normalized_data
    )

    borrowed_by_chain = calculate_borrowed_by_chain(
        normalized_data
    )

    # ---------------------------------------------------------
    # 10. Build analytical chain summary
    # ---------------------------------------------------------

    summary = build_chain_summary(
        tvl_by_chain,
        borrowed_by_chain,
    )

    # ---------------------------------------------------------
    # 11. Convert analytical summary to DataFrame
    # ---------------------------------------------------------

    summary_df = summary_to_dataframe(
        summary
    )

    summary_df = sort_summary_by_tvl(
        summary_df
    )

    # ---------------------------------------------------------
    # 12. Calculate baseline protocol TVL
    # ---------------------------------------------------------

    baseline_tvl = calculate_tvl(
        normalized_data
    )

    # ---------------------------------------------------------
    # 13. Display research output
    # ---------------------------------------------------------

    print(
        f"\n=== {protocol_name.upper()} CHAIN ANALYSIS ==="
    )

    print(summary_df)

    print(
        f"\n=== {protocol_name.upper()} BASELINE TVL ==="
    )

    print(
        f"TVL: ${baseline_tvl:,.2f}"
    )

    print(
        f"\n=== {protocol_name.upper()} METHODOLOGY TVL ==="
    )

    print(
        f"TVL: ${methodology_tvl:,.2f}"
    )


if __name__ == "__main__":
    main()
