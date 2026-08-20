"""
Source fetching utilities.

This module retrieves text content from an official methodology
source selected by the methodology resolver.

It does not interpret methodology.
It does not calculate TVL.
It does not perform protocol analysis.

Its responsibility is limited to retrieving source content.
"""

from urllib.request import Request, urlopen


def fetch_source(url):
    """
    Fetch text content from a source URL.

    Args:
        url (str):
            URL of the official source.

    Returns:
        str:
            Retrieved source content.

    Raises:
        ValueError:
            If the URL is empty.

    Raises:
        RuntimeError:
            If the source cannot be retrieved.
    """

    if not url:
        raise ValueError("Source URL is empty.")

    request = Request(
        url,
        headers={
            "User-Agent": "DeFi-Protocol-Intelligence/1.0"
        },
    )

    try:
        with urlopen(request) as response:
            content = response.read()

        return content.decode("utf-8")

    except Exception as exc:
        raise RuntimeError(
            f"Failed to fetch source: {url}"
        ) from exc
