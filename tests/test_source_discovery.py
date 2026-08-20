from src.source_discovery import discover_sources


def test_discover_aave_sources():
    sources = discover_sources("Aave V3")

    assert len(sources) >= 1

    assert any(
        source["type"] == "documentation"
        for source in sources
    )

    assert any(
        source["type"] == "repository"
        for source in sources
    )


def test_discover_morpho_sources():
    sources = discover_sources("Morpho Blue")

    assert len(sources) >= 1

    assert any(
        source["type"
        ] == "documentation"
        for source in sources
    )

    assert any(
        source["type"] == "repository"
        for source in sources
    )


def test_sources_are_official():
    sources = discover_sources("Aave V3")

    assert all(
        source["official"] is True
        for source in sources
    )


def test_unknown_protocol_returns_empty_list():
    sources = discover_sources("Unknown Protocol")

    assert sources == []
