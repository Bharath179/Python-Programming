from utility import login_shopper, make_authenticated_request


def add_products_to_cart():
    # Step 1: Log in & get token + user ID
    token, user_id = login_shopper()

    # Step 2: Prepare Cart URL
    url = f"https://www.shoppersstack.com/shopping/shoppers/{user_id}/carts"

    # Step 3: Cart payload (replace with valid productId)
    payload = {
        "productId": 27,
        "quantity": 1
    }

    # Step 4: Make POST request with correct JSON format
    response = make_authenticated_request("POST", url, json=payload)

    # Step 5: Print result
    print("Status Code:", response.status_code)
    print("Response:", response.json())

    # Step 6: Fetch cart
    get_response = make_authenticated_request("GET", url)
    cart_data = get_response.json()

    print("\nRaw Cart Response:", cart_data)

    print("\nCurrent Cart Items:")
    for idx, item in enumerate(cart_data["data"], start=1):
        print(f"{idx}. Product ID: {item['productId']} | Name: {item['productName']} | Price: ₹{item['price']}")


add_products_to_cart()
