"""
Tests for the methodology pipeline.
"""

from src.methodology_pipeline import (
    build_methodology_pipeline,
)


def test_build_methodology_pipeline(monkeypatch):
    sources = {
        "documentation": "https://example.com/docs",
        "repository": "https://github.com/example",
    }

    def fake_fetch_source(url):
        assert url == "https://example.com/docs"

        return "TVL includes supplied assets."

    monkeypatch.setattr(
        "src.methodology_pipeline.fetch_source",
        fake_fetch_source,
    )

    result = build_methodology_pipeline(
        "Aave V3",
        sources,
    )

    assert result == {
        "protocol": "Aave V3",
        "source_type": "documentation",
        "source_url": "https://example.com/docs",
        "methodology_text": (
            "TVL includes supplied assets."
        ),
    }
