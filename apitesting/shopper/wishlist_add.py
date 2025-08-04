from utility import login_shopper, make_authenticated_request


def add_products_to_wishlist():
    # Step 1: Login & get token + user ID
    token, user_id = login_shopper()

    # Step 2: Prepare Wishlist URL
    url = f"https://www.shoppersstack.com/shopping/shoppers/{user_id}/wishlist"

    # Step 3: Wishlist payload (replace with valid productId)
    payload = {
        "productId": 27,
        "quantity": 1
    }

    # Step 4: Make POST request with correct JSON format
    response = make_authenticated_request("POST", url, json=payload)

    # Step 5: Print result
    print("Status Code:", response.status_code)
    print("Response:", response.json())

    # Step 6: Fetch wishlist
    get_response = make_authenticated_request("GET", url)
    wishlist_data = get_response.json()

    print("\nRaw Wishlist Response:", wishlist_data)

    print("\nCurrent Wishlist Items:")
    for idx, item in enumerate(wishlist_data["data"], start=1):
        print(f"{idx}. Product ID: {item['productId']} | Name: {item['productName']} | Price: ₹{item['price']}")


add_products_to_wishlist()
