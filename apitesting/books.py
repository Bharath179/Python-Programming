import requests
from apitesting.json_validation import JSONValidator


def test_books_api():
    response = requests.get("http://localhost:3000/store")
    assert response.status_code == 200

    data = response.json()
    books = data.get("books", [])

    required_fields = {"id", "title", "author", "price", "available"}
    expected_types = {
        "id": int,
        "title": str,
        "author": str,
        "price": float,
        "available": bool
    }

    JSONValidator.check_unique_ids(books)
    JSONValidator.check_total_sum(books, "price")

    for book in books:
        JSONValidator.check_required_fields(book, required_fields)
        JSONValidator.check_field_types(book, expected_types)
        JSONValidator.check_non_empty_strings(book, ["title", "author"])
        JSONValidator.check_value_range(book["price"], min_value=0)
