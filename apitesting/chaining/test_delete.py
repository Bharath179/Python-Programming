import pytest
import requests


@pytest.mark.order(4)
def test_delete_user(base_url, shared_data):
    user_id = shared_data.get("user_id")
    response = requests.delete(f"{base_url}/users/{user_id}")
    assert response.status_code == 204
