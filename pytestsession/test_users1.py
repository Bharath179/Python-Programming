import requests


def test_get_all_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")
    assert response.status_code == 200

    users = response.json()
    print(f"Total Users: {len(users)}")
    assert isinstance(users, list)

    for i, user in enumerate(users, start=1):
        print(f"\nUser {i}:")
        if isinstance(user, dict):
            for key, value in user.items():
                print(f"  {key}: {value}")
        else:
            print(f"  Unexpected user format: {user}")
