import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def send_forgot_password_email():
    url = "https://www.shoppersstack.com/shopping/users/forgot-password"

    headers = {
        "email": "bharathkn179@gmail.com",
        "role": "SHOPPER"
    }

    response = requests.post(url, headers=headers, verify=False)

    print("Status Code:", response.status_code)
    try:
        print("Response:", response.json())
    except Exception as exception:
        print("Non-JSON Response:", response.text, exception)


send_forgot_password_email()
