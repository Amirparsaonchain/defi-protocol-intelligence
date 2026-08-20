"""
Methodology extraction utilities.

This module extracts structured methodology information
from methodology source content.

It does not calculate TVL.
It does not perform protocol analysis.
It does not use AI.

Its responsibility is to transform methodology text
into a structured representation that can later be
interpreted by an intelligent methodology layer.
"""


def extract_methodology_text(source_content):
    """
    Extract methodology text from source content.

    Args:
        source_content (str):
            Text retrieved from an official methodology,
            documentation, or repository source.

    Returns:
        str:
            Cleaned methodology text.

    Raises:
        ValueError:
            If the source content is empty.
    """

    if not source_content:
        raise ValueError("Methodology source content is empty.")

    if not isinstance(source_content, str):
        raise TypeError("Methodology source content must be a string.")

    return source_content.strip()


def build_methodology_record(
    protocol_name,
    source_type,
    source_url,
    methodology_text,
):
    """
    Build a structured methodology record.

    Args:
        protocol_name (str):
            Name of the protocol.

        source_type (str):
            Type of official source.

        source_url (str):
            URL of the source.

        methodology_text (str):
            Extracted methodology text.

    Returns:
        dict:
            Structured methodology record.
    """

    cleaned_text = extract_methodology_text(
        methodology_text
    )

    return {
        "protocol": protocol_name,
        "source_type": source_type,
        "source_url": source_url,
        "methodology_text": cleaned_text,
    }
