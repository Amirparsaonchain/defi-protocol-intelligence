"""
Methodology evidence utilities.

This module creates a structured evidence package from
methodology pipeline output.

It does not interpret methodology.
It does not calculate TVL.
It does not use AI.

Its responsibility is to preserve the provenance and
content that will later be provided to the methodology
interpreter.
"""


def build_methodology_evidence(methodology_record):
    """
    Build a structured methodology evidence package.

    Args:
        methodology_record (dict):
            Methodology record produced by the methodology pipeline.

    Returns:
        dict:
            Structured evidence package.

    Raises:
        ValueError:
            If required methodology information is missing.
    """

    required_fields = [
        "protocol",
        "source_type",
        "source_url",
        "methodology_text",
    ]

    for field in required_fields:
        if field not in methodology_record:
            raise ValueError(
                f"Missing methodology field: {field}"
            )

    return {
        "protocol": methodology_record["protocol"],
        "source": {
            "type": methodology_record["source_type"],
            "url": methodology_record["source_url"],
        },
        "content": methodology_record["methodology_text"],
    }
