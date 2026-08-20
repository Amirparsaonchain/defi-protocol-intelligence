"""
Tests for source fetching utilities.
"""

import pytest

from src.source_fetcher import fetch_source


class FakeResponse:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def read(self):
        return b"Official methodology content."


def test_fetch_source(monkeypatch):
    def fake_urlopen(request):
        return FakeResponse()

    monkeypatch.setattr(
        "src.source_fetcher.urlopen",
        fake_urlopen,
    )

    result = fetch_source(
        "https://example.com/methodology"
    )

    assert result == "Official methodology content."


def test_fetch_source_rejects_empty_url():
    with pytest.raises(ValueError):
        fetch_source("")


def test_fetch_source_raises_runtime_error(monkeypatch):
    def fake_urlopen(request):
        raise OSError("Network failure")

    monkeypatch.setattr(
        "src.source_fetcher.urlopen",
        fake_urlopen,
    )

    with pytest.raises(RuntimeError):
        fetch_source(
            "https://example.com/methodology"
        )
