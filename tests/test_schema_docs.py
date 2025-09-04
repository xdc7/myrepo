from django.test import Client


def test_schema_endpoint(client: Client) -> None:
    response = client.get("/api/schema/")
    assert response.status_code == 200
    # drf-spectacular returns OpenAPI as vnd.oai content type
    assert response["content-type"].startswith("application/vnd.oai.openapi")


def test_swagger_ui(client: Client) -> None:
    response = client.get("/api/docs/")
    assert response.status_code == 200
    assert response["content-type"].startswith("text/html")
    content_lower = response.content.lower()
    assert b"swagger" in content_lower or b"openapi" in content_lower


def test_redoc(client: Client) -> None:
    response = client.get("/api/redoc/")
    assert response.status_code == 200
    assert response["content-type"].startswith("text/html")
    content_lower = response.content.lower()
    assert b"redoc" in content_lower or b"openapi" in content_lower

