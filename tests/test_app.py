import http

from fastapi.testclient import TestClient

from src.app import app


def test_app_hello_world():
    client = TestClient(app)
    response = client.get('/')

    assert response.status_code == http.HTTPStatus.OK
    assert response.json() == {'message': 'Hello World'}
