from src.source_discovery import discover_sources
from src.methodology_resolver import resolve_methodology
from src.research_context import build_research_context
from analysis.methodology_analysis import (
    apply_methodology,
    calculate_methodology_tvl,
)



def test_research_pipeline_for_aave():
    protocol_name = "Aave V3"

    sources = discover_sources(protocol_name)

    source_map = {
        source["type"]: source["url"]
        for source in sources
    }

    resolution = resolve_methodology(
        protocol_name,
        source_map,
    )

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
        "name": "test methodology",
        "include_metric_types": ["chain"],
    }

    analyzed_data = apply_methodology(
        normalized_data,
        methodology,
    )

    methodology_tvl = calculate_methodology_tvl(
        normalized_data,
        methodology,
    )

    context = build_research_context(
        protocol_name,
        sources,
        resolution,
        analyzed_data,
    )

    assert context["protocol"] == protocol_name
    assert context["sources"] == sources
    assert context["methodology"] == resolution
    assert context["analysis"] == analyzed_data

    assert analyzed_data[0]["methodology_included"] is True
    assert analyzed_data[1]["methodology_included"] is False

    assert methodology_tvl == 1000.0

