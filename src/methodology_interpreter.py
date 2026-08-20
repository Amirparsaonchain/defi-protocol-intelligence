"""
Methodology interpretation utilities.

This module defines the interface for interpreting protocol
methodology evidence.

The interpreter converts evidence into a structured
methodology specification.

It does not calculate TVL.

The actual AI implementation can be connected later without
changing the downstream analytical pipeline.
"""


def interpret_methodology(evidence):
    """
    Interpret methodology evidence into a structured specification.

    This is currently a placeholder for the future AI interpreter.

    Args:
        evidence (dict):
            Structured methodology evidence.

    Returns:
        dict:
            Methodology specification.

    Raises:
        ValueError:
            If required evidence is missing.
    """

    required_fields = [
        "protocol",
        "source",
        "content",
    ]

    for field in required_fields:
        if field not in evidence:
            raise ValueError(
                f"Missing evidence field: {field}"
            )

    return {
        "protocol": evidence["protocol"],
        "source": evidence["source"],
        "methodology": {
            "raw_content": evidence["content"],
        },
    }
