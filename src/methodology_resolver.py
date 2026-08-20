"""
Methodology resolution utilities.

This module resolves methodology sources for a selected protocol.

It does not calculate TVL or perform protocol analysis.
Its responsibility is to connect discovered official sources
to the methodology layer of the intelligence pipeline.
"""


def resolve_methodology_source(sources):
    """
    Resolve the best available methodology source.

    Priority:
        1. methodology
        2. documentation
        3. repository

    Args:
        sources (dict):
            Discovered protocol sources.

    Returns:
        tuple:
            (source_type, source_url)

    Raises:
        ValueError:
            If no usable source is available.
    """

    priority = [
        "methodology",
        "documentation",
        "repository",
    ]

    for source_type in priority:
        source_url = sources.get(source_type)

        if source_url:
            return source_type, source_url

    raise ValueError("No methodology source available.")


def resolve_methodology(protocol_name, sources):
    """
    Build a methodology resolution result for a protocol.

    Args:
        protocol_name (str):
            Name of the protocol.

        sources (dict):
            Discovered protocol sources.

    Returns:
        dict:
            Methodology resolution information.
    """

    source_type, source_url = resolve_methodology_source(sources)

    return {
        "protocol": protocol_name,
        "source_type": source_type,
        "source_url": source_url,
    }
