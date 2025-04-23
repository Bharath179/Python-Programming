import random

import requests

user_id = None


# Bearer Token(OAuth 2)
def test_bearer_token():
    response = requests.get("https://gorest.co.in/public/v2/users")
    print("Response Body:", response.json())


def test_post_user():
    global user_id
    unique_email = f"bharath{random.randint(10, 99)}@example.com"

    data = {
        'name': 'Bharath Kumar',
        'email': unique_email,
        'gender': 'male',
        'status': 'active'
    }

    token = "a439eb27ee99cfa518f05151420f6ea084153f3f3fb4c843407b2cac62930e2d"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.post("https://gorest.co.in//public/v2/users", headers=headers, json=data)
    assert response.status_code == 201
    response_data = response.json()
    user_id = response_data.get('id')
    print(response_data)
    assert user_id is not None
    