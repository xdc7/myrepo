import json

import pytest
from django.test import Client


@pytest.mark.django_db
def test_html_health(client: Client) -> None:
    response = client.get("/health/")
    assert response.status_code == 200
    assert b"OK" in response.content


@pytest.mark.django_db
def test_api_health(client: Client) -> None:
    response = client.get("/api/health/")
    assert response.status_code == 200
    data = json.loads(response.content.decode())
    assert data == {"status": "ok"}
