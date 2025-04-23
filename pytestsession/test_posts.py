import requests


def test_get_all_posts(base_url):
    res = requests.get(f"{base_url}/posts")
    assert res.status_code == 200
    assert isinstance(res.json(), list)


def test_create_post(base_url, headers):
    data = {
        "title": "pytest is awesome",
        "body": "writing tests is fun",
        "userId": 1
    }
    res = requests.post(f"{base_url}/posts", json=data, headers=headers)
    assert res.status_code == 201
    json_res = res.json()
    assert json_res["title"] == data["title"]
    assert json_res["body"] == data["body"]


def test_invalid_post_id(base_url):
    res = requests.get(f"{base_url}/posts/9999")
    assert res.status_code in [200, 404]
