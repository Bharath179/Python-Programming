from utility import login_shopper, make_authenticated_request
from datetime import datetime


def post_review():
    token, user_id = login_shopper()
    product_id = 27
    url = f"https://www.shoppersstack.com/shopping/reviews?productId={product_id}"

    payload = {
        "dateTime": datetime.now().isoformat(),
        "description": "Good quality product.",
        "heading": "Very Satisfied!",
        "rating": 5,
        "shopperId": user_id,
        "shopperName": "Kumar"
    }

    response = make_authenticated_request("POST", url, json=payload)

    print("Status Code:", response.status_code)
    print("Raw Response Text:", response.text)

    try:
        print("JSON Response:", response.json())
    except Exception as exception:
        print("Error parsing JSON:", exception)


post_review()
