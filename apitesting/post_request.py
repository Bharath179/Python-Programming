import requests


def test_post_request():
    body = {"id": 500,
            "email": "bharath@reqres.in",
            "first_name": "Bharath",
            "last_name": "Reddy",
            "avatar": "https://reqres.in/img/faces/7-image.jpg"
            }
    response = requests.post("https://reqres.in/api/users", json=body)
    print("Response Body:", response.json())
    assert response.status_code == 201
    assert "id" in response.json()


def test_get_user_by_id():
    user_id = 2
    url = f"https://reqres.in/api/users/{user_id}"
    response = requests.get(url)

    print("Status Code:", response.status_code)

    if response.status_code == 404:
        print(f"User ID {user_id} not found.")
        assert response.status_code == 404
    else:
        user_data = response.json()["data"]
        print("User Data:", user_data)
        assert user_data["id"] == user_id


def test_update_user():
    body = {
        "first_name": "Bharath",
        "last_name": "Weaver",
        "email": "bharath.weaver@reqres.in",
        "avatar": "https://reqres.in/img/faces/2-image.jpg"
    }

    response = requests.put("https://reqres.in/api/users/2", json=body)

    print("Response Body:", response.json())
    assert response.status_code == 200
    assert response.json()["first_name"] == "Bharath"


def test_delete_user():
    user_id = 2
    url = "https://reqres.in/api/users/2"
    response = requests.delete(f"{url}/{user_id}")
    print("DELETE Status:", response.status_code)
    assert response.status_code == 204
