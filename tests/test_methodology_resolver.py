"""
Tests for methodology resolution utilities.
"""

import pytest

from src.methodology_resolver import (
    resolve_methodology_source,
    resolve_methodology,
)


def test_resolve_methodology_source_prefers_methodology():
    sources = {
        "methodology": "https://example.com/methodology",
        "documentation": "https://example.com/docs",
        "repository": "https://github.com/example",
    }

    result = resolve_methodology_source(sources)

    assert result == (
        "methodology",
        "https://example.com/methodology",
    )


def test_resolve_methodology_source_falls_back_to_documentation():
    sources = {
        "documentation": "https://example.com/docs",
        "repository": "https://github.com/example",
    }

    result = resolve_methodology_source(sources)

    assert result == (
        "documentation",
        "https://example.com/docs",
    )


def test_resolve_methodology_source_falls_back_to_repository():
    sources = {
        "repository": "https://github.com/example",
    }

    result = resolve_methodology_source(sources)

    assert result == (
        "repository",
        "https://github.com/example",
    )


def test_resolve_methodology_source_raises_when_no_source_exists():
    sources = {}

    with pytest.raises(ValueError):
        resolve_methodology_source(sources)


def test_resolve_methodology():
    sources = {
        "documentation": "https://aave.com/docs",
        "repository": "https://github.com/aave",
    }

    result = resolve_methodology(
        "Aave V3",
        sources,
    )

    assert result == {
        "protocol": "Aave V3",
        "source_type": "documentation",
        "source_url": "https://aave.com/docs",
    }
