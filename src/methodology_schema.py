"""
Methodology specification utilities.

This module defines the structured representation of a protocol's
methodology.

It does not fetch sources.
It does not interpret methodology.
It does not calculate TVL.

Its responsibility is to define and validate the contract
between the AI methodology interpreter and downstream analysis.
"""


REQUIRED_FIELDS = [
    "protocol",
    "source",
    "claims",
    "included_metrics",
    "excluded_metrics",
    "aggregation_logic",
    "confidence",
]


def validate_methodology_specification(specification):
    """
    Validate a structured methodology specification.

    Args:
        specification (dict):
            Methodology specification.

    Returns:
        bool:
            True when the specification is valid.

    Raises:
        ValueError:
            If a required field is missing.
    """

    for field in REQUIRED_FIELDS:
        if field not in specification:
            raise ValueError(
                f"Missing methodology field: {field}"
            )

    return True
