"""
Methodology pipeline utilities.

This module connects methodology resolution, source fetching,
and methodology extraction into a single reusable workflow.

It does not calculate TVL.
It does not perform protocol analysis.
It does not interpret methodology with AI.

Its responsibility is to produce a structured methodology
record with preserved source provenance.
"""

from src.methodology_resolver import resolve_methodology
from src.source_fetcher import fetch_source
from src.methodology_extractor import build_methodology_record


def build_methodology_pipeline(protocol_name, sources):
    """
    Resolve, fetch, and extract a protocol's methodology.

    Args:
        protocol_name (str):
            Name of the protocol.

        sources (dict):
            Official sources discovered for the protocol.

    Returns:
        dict:
            Structured methodology record containing:
            protocol,
            source_type,
            source_url,
            methodology_text.
    """

    resolved = resolve_methodology(
        protocol_name,
        sources,
    )

    source_content = fetch_source(
        resolved["source_url"]
    )

    return build_methodology_record(
        protocol_name=resolved["protocol"],
        source_type=resolved["source_type"],
        source_url=resolved["source_url"],
        methodology_text=source_content,
    )
