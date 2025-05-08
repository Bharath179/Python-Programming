import pytest
import requests


@pytest.mark.order(2)
def test_get_user(base_url, shared_data):
    user_id = shared_data.get("user_id")
    assert user_id is not None, "User ID not found"
    response = requests.get(f"{base_url}/users/{user_id}")
    assert response.status_code == 200 or response.status_code == 404
