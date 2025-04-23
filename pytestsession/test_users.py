import requests
import logging


logger = logging.getLogger(__name__)


def test_get_all_users(base_url):
    res = requests.get(f"{base_url}/users")
    assert res.status_code == 200
    # assert len(res.json()) > 0

    users = res.json()
    assert len(users) > 0

    logger.info(f"\nTotal Users: {len(users)}\n")

    for user in users:
        logger.info("USER INFO")
        logger.info(f"ID       : {user['id']}")
        logger.info(f"Name     : {user['name']}")
        logger.info(f"Username : {user['username']}")
        logger.info(f"Email    : {user['email']}")
        logger.info(f"Phone    : {user['phone']}")
        logger.info(f"Website  : {user['website']}")
        logger.info(f"Company  : {user['company']['name']}")
        logger.info(f"City     : {user['address']['city']}")
        logger.info("-" * 40)


def test_get_single_user(base_url):
    res = requests.get(f"{base_url}/users/1")
    assert res.status_code == 200
    assert res.json()["id"] == 1


def test_invalid_user(base_url):
    res = requests.get(f"{base_url}/users/9999")
    assert res.status_code == 404 or res.status_code == 200
