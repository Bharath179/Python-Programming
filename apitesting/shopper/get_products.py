from utility import make_authenticated_request


def get_all_products():
    url = "https://www.shoppersstack.com/shopping/products/alpha"
    response = make_authenticated_request("GET", url)

    if response.status_code == 200:
        products = response.json().get("data", [])
        print(f"\nTotal Products: {len(products)}\n")
        for i, product in enumerate(products, 1):
            print(f"{i}. ID: {product['productId']} | Name: {product['name']} | Price: {product['price']}")
    else:
        print("Failed to fetch products:", response.status_code)


get_all_products()
