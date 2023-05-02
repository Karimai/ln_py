import pytest
import requests


@pytest.fixture(scope="session")
def api():
    print("Setting up API client")
    api = requests.Session()
    api.headers.update({"Content-Type": "application/json"})
    yield api
    print("Tearing down API client")
    api.close()


@pytest.fixture
def user(api):
    user_data = {"username": "testuser", "password": "testpass"}
    response = api.post("https://httpbin.org/post", json=user_data)
    assert response.status_code == 200, "Authentication failed"
    token = response.json().get("token")
    api.headers.update({"Authorization": f"Bearer {token}"})
    yield
    api.delete("https://httpbin.org/delete")


def test_user_creation(user, api):
    user_data = {"username": "testuser", "email": "testuser@example.com"}
    response = api.post("https://httpbin.org/post", json=user_data)
    assert response.status_code == 200, "User creation failed"
    assert response.json().get("json").get("username") == "testuser", "Wrong username"
    assert (
        response.json().get("json").get("email") == "testuser@example.com"
    ), "Wrong email"
