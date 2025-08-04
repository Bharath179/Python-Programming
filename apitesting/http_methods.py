import requests
import pytest

base_url = "https://reqres.in/api/users"

# global-like variable for user ID
user_id = None


def test_get_users():
    response = requests.get(f"{base_url}?page=2")
    assert response.status_code == 200
    assert response.json()["page"] == 2
    print(response.json())


@pytest.mark.dependency(name="create_user")
def test_create_user():
    global user_id
    data = {
        "name": "bharath",
        "job": "QA"
    }
    response = requests.post(base_url, json=data)
    assert response.status_code == 201
    response_data = response.json()
    user_id = response_data.get("id")
    print(response_data)
    assert user_id is not None


@pytest.mark.dependency(depends=["create_user"])
def test_update_user():
    data = {
        "name": "Kumar",
        "job": "Software Engineer"
    }
    response = requests.put(f"{base_url}/{user_id}", json=data)
    assert response.status_code == 200
    print(response.json())


def test_delete_user():
    response = requests.delete(f"{base_url}/{user_id}")
    assert response.status_code == 204
    print("User deleted successfully")
 