import requests

session = requests.Session()


def test_set_cookies():
    session.cookies.set("session_id", "abc123")
    session.cookies.set("theme", "dark")
    print("\nCookies set:")
    print(session.cookies.get_dict())


def test_view_cookies():
    response = session.get("https://httpbin.org/cookies")
    print("\nCookies from server:")
    print(response.json())


def test_delete_cookies():
    session.cookies.set("session_id", None)
    session.cookies.clear()
    print("\nCookies deleted.")
    print(session.cookies.get_dict())


def test_set_headers():
    session.headers.update({
        "User-Agent": "MyTestAgent/1.0",
        "Authorization": "Bearer fake_token_123"
    })
    print("\nHeaders set:")
    print(session.headers)


def test_view_headers():
    response = session.get("https://httpbin.org/headers")
    print("\nHeaders from server:")
    print(response.json())


def test_delete_headers():
    if "Authorization" in session.headers:
        del session.headers["Authorization"]
    print("\nAuthorization header deleted.")
    print(session.headers)


# Headers
test_set_headers()
test_view_headers()
test_delete_headers()
test_view_headers()

# Cookies
test_set_cookies()
test_view_cookies()
test_delete_cookies()
test_view_cookies()
