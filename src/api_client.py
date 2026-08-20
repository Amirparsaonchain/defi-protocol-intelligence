import requests

from src.config import BASE_URL, PROTOCOLS_ENDPOINT, REQUEST_TIMEOUT


def get_protocols():
    url = f"{BASE_URL}{PROTOCOLS_ENDPOINT}"

    response = requests.get(
        url,
        timeout=REQUEST_TIMEOUT
    )

    response.raise_for_status()

    return response.json()
