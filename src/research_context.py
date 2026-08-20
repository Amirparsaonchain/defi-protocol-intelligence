"""
Research context utilities.

This module builds a structured research context for a protocol
from discovered sources and resolved methodology information.

It does not perform web research, AI analysis, or TVL calculation.

Its responsibility is to provide a stable data structure that
later research and AI layers can consume.
"""


def build_research_context(
    protocol_name,
    sources,
    methodology_resolution,
    methodology_analysis,
):
    """
    Build a structured research context for a protocol.

    Args:
        protocol_name (str):
            Name of the protocol.

        sources (list[dict]):
            Official sources discovered for the protocol.

        methodology_resolution (dict):
            Result produced by the methodology resolver.

        methodology_analysis (dict):
            Result produced by the methodology analysis layer.

    Returns:
        dict:
            Structured research context.
    """

    return {
        "protocol": protocol_name,
        "sources": sources,
        "methodology": methodology_resolution,
        "analysis": methodology_analysis,
    }
