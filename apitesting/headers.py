import requests


def test_get_headers():
    response = requests.get("https://www.google.com")
    headers = response.headers

    # print all headers
    print("Response Headers:")
    for name, value in headers.items():
        print(f"name={name}, value={value}")

    # Validate the headers
    assert 'Content-Type' in response.headers
    assert headers['Content-Type'] == 'text/html; charset=ISO-8859-1'
    assert headers['X-Frame-Options'] == 'SAMEORIGIN'
    assert 'gws' in response.headers['Server']


# Test 2: Log everything from the reqres.in endpoint
def test_log_headers_and_body():
    response = requests.get("https://www.google.com")

    print("\nResponse Body:")
    print(response.text)

    print("\nResponse Headers:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")

    print("\nCookies:")
    print(response.cookies)
    assert response.status_code == 200


# Test 3: Test for path and query parameters
def test_path_query_params():
    # https://reqres.in/api/users?page=2&id=5
    my_path = 'users'
    query_params = {
        'page': 2,
        'id': 5
    }
    url = f"https://reqres.in/api/{my_path}"
    response = requests.get(url, params=query_params)
    assert response.status_code == 200
    print("Response Body:", response.json())
    print("Query params sent:", response.url)
