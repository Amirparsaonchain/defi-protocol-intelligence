"""
Tests for methodology evidence utilities.
"""

import pytest

from src.methodology_evidence import (
    build_methodology_evidence,
)


def test_build_methodology_evidence():
    methodology_record = {
        "protocol": "Aave V3",
        "source_type": "documentation",
        "source_url": "https://aave.com/docs",
        "methodology_text": (
            "TVL includes supplied assets."
        ),
    }

    result = build_methodology_evidence(
        methodology_record
    )

    assert result == {
        "protocol": "Aave V3",
        "source": {
            "type": "documentation",
            "url": "https://aave.com/docs",
        },
        "content": (
            "TVL includes supplied assets."
        ),
    }


def test_build_methodology_evidence_requires_protocol():
    methodology_record = {
        "source_type": "documentation",
        "source_url": "https://aave.com/docs",
        "methodology_text": "TVL methodology.",
    }

    with pytest.raises(ValueError):
        build_methodology_evidence(
            methodology_record
        )


def test_build_methodology_evidence_requires_source_url():
    methodology_record = {
        "protocol": "Aave V3",
        "source_type": "documentation",
        "methodology_text": "TVL methodology.",
    }

    with pytest.raises(ValueError):
        build_methodology_evidence(
            methodology_record
        )
