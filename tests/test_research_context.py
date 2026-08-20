from src.research_context import build_research_context


def test_build_research_context():
    sources = [
        {
            "type": "documentation",
            "name": "Aave Documentation",
            "url": "https://aave.com/docs",
            "official": True,
        },
        {
            "type": "repository",
            "name": "Aave GitHub",
            "url": "https://github.com/aave",
            "official": True,
        },
    ]

    methodology_resolution = {
        "protocol": "Aave V3",
        "source_type": "documentation",
        "source_url": "https://aave.com/docs",
    }

    methodology_analysis = {
        "protocol": "Aave V3",
        "methodology_source": "https://aave.com/docs",
    }

    result = build_research_context(
        "Aave V3",
        sources,
        methodology_resolution,
        methodology_analysis,
    )

    assert result["protocol"] == "Aave V3"
    assert result["sources"] == sources
    assert result["methodology"] == methodology_resolution
    assert result["analysis"] == methodology_analysis


def test_research_context_preserves_sources():
    sources = [
        {
            "type": "documentation",
            "name": "Test Docs",
            "url": "https://example.com/docs",
            "official": True,
        }
    ]

    methodology_resolution = {
        "protocol": "Test Protocol",
        "source_type": "documentation",
        "source_url": "https://example.com/docs",
    }

    methodology_analysis = {
        "protocol": "Test Protocol",
        "methodology_source": "https://example.com/docs",
    }

    result = build_research_context(
        "Test Protocol",
        sources,
        methodology_resolution,
        methodology_analysis,
    )

    assert result["sources"] is sources


def test_research_context_keeps_methodology_resolution():
    methodology_resolution = {
        "protocol": "Morpho Blue",
        "source_type": "documentation",
        "source_url": "https://docs.morpho.org/",
    }

    result = build_research_context(
        "Morpho Blue",
        [],
        methodology_resolution,
        {},
    )

    assert result["methodology"] == methodology_resolution


def test_research_context_keeps_methodology_analysis():
    methodology_analysis = {
        "protocol": "Morpho Blue",
        "methodology_source": "https://docs.morpho.org/",
    }

    result = build_research_context(
        "Morpho Blue",
        [],
        {},
        methodology_analysis,
    )

    assert result["analysis"] == methodology_analysis
