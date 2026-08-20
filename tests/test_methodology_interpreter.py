"""
Tests for methodology interpretation utilities.
"""

import pytest

from src.methodology_interpreter import (
    interpret_methodology,
)


def test_interpret_methodology():
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

    result = interpret_methodology(evidence)

    assert result == {
        "protocol": "Aave V3",
        "source": {
            "type": "documentation",
            "url": "https://aave.com/docs",
        },
        "methodology": {
            "raw_content": (
                "TVL includes supplied assets."
            ),
        },
    }


def test_interpret_methodology_requires_protocol():
    evidence = {
        "source": {
            "type": "documentation",
            "url": "https://aave.com/docs",
        },
        "content": "TVL methodology.",
    }

    with pytest.raises(ValueError):
        interpret_methodology(evidence)


def test_interpret_methodology_requires_source():
    evidence = {
        "protocol": "Aave V3",
        "content": "TVL methodology.",
    }

    with pytest.raises(ValueError):
        interpret_methodology(evidence)


def test_interpret_methodology_requires_content():
    evidence = {
        "protocol": "Aave V3",
        "source": {
            "type": "documentation",
            "url": "https://aave.com/docs",
        },
    }

    with pytest.raises(ValueError):
        interpret_methodology(evidence)
