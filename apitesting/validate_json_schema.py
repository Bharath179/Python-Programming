import requests
import pytest

# Base URL
BASE_URL = "http://localhost:3000/store"


@pytest.fixture(scope="module")
def response_data():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    return response.json()


def test_books_key_exists(response_data):
    assert "books" in response_data


def test_books_is_list(response_data):
    assert isinstance(response_data["books"], list)


def test_books_are_not_empty(response_data):
    assert len(response_data["books"]) > 0


def test_each_book_has_required_fields(response_data):
    required_fields = {"id", "title", "author", "price", "available"}
    for book in response_data["books"]:
        assert required_fields.issubset(book)


def test_field_types(response_data):
    for book in response_data["books"]:
        assert isinstance(book["id"], int)
        assert isinstance(book["title"], str)
        assert isinstance(book["author"], str)
        assert isinstance(book["price"], (int, float))
        assert isinstance(book["available"], bool)


def test_non_empty_strings(response_data):
    for book in response_data["books"]:
        assert book["title"].strip() != ""
        assert book["author"].strip() != ""


def test_unique_ids(response_data):
    ids = [book["id"] for book in response_data["books"]]
    assert len(ids) == len(set(ids))


def test_price_greater_than_zero(response_data):
    for book in response_data["books"]:
        assert book["price"] > 0


def test_conditional_logic(response_data):
    for book in response_data["books"]:
        if not book["available"]:
            assert book["price"] < 30


def test_specific_book_titles(response_data):
    titles = [book["title"] for book in response_data["books"]]
    assert "Learn Python" in titles


def test_total_price_not_zero(response_data):
    total_price = sum(book.get("price", 0.0) for book in response_data["books"])
    assert total_price > 0
