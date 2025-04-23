import requests


def test_cookie_value():
    response = requests.get("https://www.google.com")
    cookie_value = response.cookies.get("AEC")
    print("Cookie Value is:", cookie_value)


def test_all_cookies():
    response = requests.get("https://www.google.com")
    cookies = response.cookies.get_dict()
    for key, value in cookies.items():
        print(f"key={key}, value={value}")
    assert 'AEC' in cookies
    #assert cookies['AEC'] == 'AVcja2eMlm_OxM-Od4BGFMhOdqs9HzxVrirS_1YGbVjedddD8le8AgRP0w'
    assert len(cookies) > 0
