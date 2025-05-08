import requests


def test_validate_http_response_header():
    url = "https://reqres.in/api/users/2"
    response = requests.get(url)

    try:
        connection_header = response.headers.get("Connection")
        print("Connection Header:", connection_header)

        # Print all headers
        for key, value in response.headers.items():
            print(f"{key}: {value}")

        # Validate Content-Type header
        expected = "application/json; charset=utf-8"
        actual = response.headers.get("Content-Type")
        assert actual == expected, f"Expected Content-Type '{expected}' but got '{actual}'"

    except Exception as e:
        raise AssertionError(f"Header validation failed: {str(e)}")


def test_validate_json_body():
    url = "https://reqres.in/api/users?page=2"
    response = requests.get(url)

    try:
        print("Response Body:", response.text)

        # Parse JSON
        json_data = response.json()

        # Extract fields
        first_name = json_data['data'][4]['first_name']
        avatar_url = json_data['data'][4]['avatar']

        print("First Name:", first_name)
        print("Avatar URL:", avatar_url)

        # Validate first name
        expected_name = "George"
        assert first_name == expected_name, f"Expected name '{expected_name}' but got '{first_name}'"

    except Exception as e:
        raise AssertionError(f"JSON body validation failed: {str(e)}")


def test_read_all_first_names():
    url = "https://reqres.in/api/users?page=2"
    response = requests.get(url)

    try:
        json_data = response.json()
        users = json_data['data']

        for index, user in enumerate(users):
            first_name = user['first_name']
            print(f"User {index + 1}: {first_name} (Type: {type(first_name).__name__})")

        first_names = [user['first_name'] for user in users]
        last_names = [user['last_name'] for user in users]
        avatars = [user['avatar'] for user in users]
        print("Last Names:", last_names)
        print("First Names:", first_names)
        print("Avatars:", avatars)
        assert len(first_names) > 0, "Not able to print first names"

    except Exception as e:
        raise AssertionError(f"Error reading first names: {str(e)}")
