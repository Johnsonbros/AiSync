"""Simple wrapper around the Housecall Pro API."""

from __future__ import annotations

import os
from typing import Any

import requests


class HousecallClient:
    """A minimal client for the Housecall Pro API."""

    BASE_URL = "https://api.housecallpro.com"  # v1 base

    def __init__(self, api_token: str | None = None) -> None:
        self.api_token = api_token or os.getenv("HOUSECALL_API_TOKEN")
        if not self.api_token:
            raise ValueError("Missing Housecall Pro API token")

    def _headers(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self.api_token}", "Accept": "application/json"}

    def get(self, endpoint: str, **params: Any) -> Any:
        url = f"{self.BASE_URL}/{endpoint.lstrip('/') }"
        resp = requests.get(url, headers=self._headers(), params=params, timeout=30)
        resp.raise_for_status()
        return resp.json()

    def get_customer(self, customer_id: int) -> Any:
        """Fetch a customer by ID."""
        return self.get(f"v1/customers/{customer_id}")
