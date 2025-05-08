import random

import requests
import json


# 1. Basic Auth
def test_basic_auth():
    url = "https://postman-echo.com/basic-auth"
    response = requests.get(url, auth=("postman", "password"))
    print("Response status:", response.status_code)
    print("Response body:", response.text)


# 2. Digest Auth
def test_digest_auth():
    from requests.auth import HTTPDigestAuth

    url = "http://httpbin.org/digest-auth/undefined/bharath/bharath"
    response = requests.get(url, auth=HTTPDigestAuth('bharath', 'bharath'))
    print("Response status:", response.status_code)
    print("Response body:", response.text)


# 3. Bearer Token
def test_bearer_token():
    url = "https://gorest.co.in/public/v2/users"
    email = f"bharath{random.randint(10, 99)}@example.com"
    payload = {
        "name": "bharath",
        "gender": "male",
        "email": email,
        "status": "active"
    }

    headers = {
        "Authorization": "Bearer a439eb27ee99cfa518f05151420f6ea084153f3f3fb4c843407b2cac62930e2d",
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print("Response status:", response.status_code)
    print("Response body:", response.text)


# 4. API Key in Query Param
def test_api_key():
    url = "https://openweathermap.org/data/2.5/weather"
    params = {
        "q": "delhi",
        "appid": "70018b4eb6299f09522aa449128b2c97"
    }

    response = requests.get(url, params=params)
    print("Response status:", response.status_code)
    print("Response body:", response.text)


# Run tests
test_basic_auth()
test_digest_auth()
test_bearer_token()
test_api_key()