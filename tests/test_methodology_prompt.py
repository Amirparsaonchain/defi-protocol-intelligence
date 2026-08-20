"""
Tests for methodology prompt utilities.
"""

import pytest

from src.methodology_prompt import (
    build_methodology_prompt,
)


def test_build_methodology_prompt():
    evidence = {
        "protocol": "Aave V3",
        "source": {
            "type": "documentation",
            "url": "https://aave.com/docs",
        },
        "content": (
            "TVL includes supplied assets."
        ),
    }

    result = build_methodology_prompt(evidence)

    assert "Aave V3" in result
    assert "documentation" in result
    assert "https://aave.com/docs" in result
    assert "TVL includes supplied assets." in result


def test_prompt_requires_protocol():
    evidence = {
        "source": {
            "type": "documentation",
            "url": "https://aave.com/docs",
        },
        "content": "TVL methodology.",
    }

    with pytest.raises(ValueError):
        build_methodology_prompt(evidence)


def test_prompt_requires_source():
    evidence = {
        "protocol": "Aave V3",
        "content": "TVL methodology.",
    }

    with pytest.raises(ValueError):
        build_methodology_prompt(evidence)


def test_prompt_requires_content():
    evidence = {
        "protocol": "Aave V3",
        "source": {
            "type": "documentation",
            "url": "https://aave.com/docs",
        },
    }

    with pytest.raises(ValueError):
        build_methodology_prompt(evidence)


def test_prompt_requires_evidence_based_interpretation():
    evidence = {
        "protocol": "Aave V3",
        "source": {
            "type": "documentation",
            "url": "https://aave.com/docs",
        },
        "content": "TVL includes supplied assets.",
    }

    result = build_methodology_prompt(evidence)

    assert "Do not invent methodology rules" in result
    assert "evidence" in result
    assert "unknown" in result

