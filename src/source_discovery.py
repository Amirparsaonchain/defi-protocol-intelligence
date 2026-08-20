"""
Protocol source discovery utilities.

This module identifies official research sources associated
with a protocol.

The current implementation uses a deterministic source registry.
Future versions can extend this layer with automated discovery
and AI-assisted source verification.
"""


OFFICIAL_SOURCES = {
    "Aave V3": [
        {
            "type": "documentation",
            "name": "Aave Documentation",
            "url": "https://aave.com/docs",
            "official": True,
        },
        {
            "type": "repository",
            "name": "Aave GitHub",
            "url": "https://github.com/aave",
            "official": True,
        },
    ],
    "Morpho Blue": [
        {
            "type": "documentation",
            "name": "Morpho Documentation",
            "url": "https://docs.morpho.org/",
            "official": True,
        },
        {
            "type": "repository",
            "name": "Morpho GitHub",
            "url": "https://github.com/morpho-org",
            "official": True,
        },
    ],
}


def discover_sources(protocol_name):
    """
    Discover official sources associated with a protocol.

    Args:
        protocol_name (str):
            Name of the protocol.

    Returns:
        list[dict]:
            Official sources registered for the protocol.

        If the protocol is not registered, an empty list is returned.
    """

    return OFFICIAL_SOURCES.get(protocol_name, []).copy()
