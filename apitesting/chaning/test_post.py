import pytest
import requests


@pytest.mark.order(1)
def test_create_user(base_url, shared_data):
    payload = {"name": "John", "job": "Engineer"}
    response = requests.post(f"{base_url}/users", json=payload)
    assert response.status_code == 201
    user_id = response.json()["id"]
    shared_data["user_id"] = user_id
    print("Created User ID:", user_id)
