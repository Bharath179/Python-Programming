import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

EMAIL = "bknreddy04@gmail.com"
PASSWORD = "Asdf@123"
ROLE = "SHOPPER"
LOGIN_URL = "https://www.shoppersstack.com/shopping/users/login"


def login_shopper():
    payload = {
        "email": EMAIL,
        "password": PASSWORD,
        "role": ROLE
    }

    response = requests.post(LOGIN_URL, json=payload, verify=False)

    if response.status_code != 200:
        raise Exception(f"Login failed: {response.status_code} - {response.text}")

    data = response.json()["data"]
    return data["jwtToken"], data["userId"]


def make_authenticated_request(method, url, data=None, json=None):
    token, _ = login_shopper()
    headers = {"Authorization": f"Bearer {token}"}
    method = method.upper()

    def send():
        if method == "GET":
            return requests.get(url, headers=headers, verify=False)
        elif method == "POST":
            return requests.post(url, headers=headers, data=data, json=json, verify=False)
        elif method == "PATCH":
            return requests.patch(url, headers=headers, data=data, json=json, verify=False)
        elif method == "PUT":
            return requests.put(url, headers=headers, data=data, json=json, verify=False)
        elif method == "DELETE":
            return requests.delete(url, headers=headers, verify=False)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

    response = send()

    if response.status_code == 401:
        token, _ = login_shopper()
        headers["Authorization"] = f"Bearer {token}"
        response = send()

    return response
