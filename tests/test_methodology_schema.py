"""
Tests for methodology specification validation.
"""

import pytest

from src.methodology_schema import (
    validate_methodology_specification,
)


def test_validate_methodology_specification():
    specification = {
        "protocol": "Aave V3",
        "source": {
            "type": "documentation",
            "url": "https://aave.com/docs",
        },
        "claims": [
            "Supplied assets are included in TVL."
        ],
        "included_metrics": [
            "chain"
        ],
        "excluded_metrics": [
            "borrowed"
        ],
        "aggregation_logic": (
            "Sum included metrics across chains."
        ),
        "confidence": "high",
    }

    assert (
        validate_methodology_specification(
            specification
        )
        is True
    )


def test_missing_protocol_is_rejected():
    specification = {
        "source": {},
        "claims": [],
        "included_metrics": [],
        "excluded_metrics": [],
        "aggregation_logic": "",
        "confidence": "high",
    }

    with pytest.raises(ValueError):
        validate_methodology_specification(
            specification
        )


def test_missing_claims_is_rejected():
    specification = {
        "protocol": "Aave V3",
        "source": {},
        "included_metrics": [],
        "excluded_metrics": [],
        "aggregation_logic": "",
        "confidence": "high",
    }

    with pytest.raises(ValueError):
        validate_methodology_specification(
            specification
        )


def test_missing_aggregation_logic_is_rejected():
    specification = {
        "protocol": "Aave V3",
        "source": {},
        "claims": [],
        "included_metrics": [],
        "excluded_metrics": [],
        "confidence": "high",
    }

    with pytest.raises(ValueError):
        validate_methodology_specification(
            specification
        )
