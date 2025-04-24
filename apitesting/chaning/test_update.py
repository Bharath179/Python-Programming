import pytest
import requests


@pytest.mark.order(3)
def test_update_user(base_url, shared_data):
    user_id = shared_data.get("user_id")
    payload = {"name": "John Mack", "job": "Manager"}
    response = requests.put(f"{base_url}/users/{user_id}", json=payload)
    assert response.status_code == 200
