# python -m API.Lab1.lab1

from ..api import get_json
from pprint import pprint

import requests

# products = requests.get(
# "https://api.github.com"
# )
# print(products.status_code) # 200

url = "https://fakestoreapi.com"

# GET /products
# GET /products/categories
# GET /products/category/<name>
# POST /products
# PATCH /products/<id>

# # 1 Sort the products by price
# # Fetch /products with get_json. You get a list of dictionaries. Sort the list so the
# # cheapest product comes first and print one line per product with the price and the title.
# # Hint: sorted(products, key=...), where the key function takes one product and
# # returns its price.
# products = get_json(
#    f"{url}/products"
# )
# if products:
#     sorted_products = sorted(products, key=lambda product: product["price"])
#     for product in sorted_products:
#         print(f'{product["price"]} - {product["title"]}')

# # 2 Look at the categories
# # Fetch /products/categories and print the result. Then ask the user to type one of the
# # categories with input(). Fetch /products/category/<name> and print how many
# # products it has and which one is the cheapest. Think about what happens if the user
# # types a category that does not exist. Note: the category is spelled jewelery in this API.
# # That is not your mistake.
# categories = get_json(
#     f"{url}/products/categories"
# )
# pprint(categories)
# category_name = input("Type category: ")
# products_in_category = get_json(
#     f"{url}/products/category/{category_name}"
# )
# pprint(products_in_category)
# print(f"Number of products: {len(products_in_category)}")
# if products_in_category:
#     print(f"The cheapest product: {min(products_in_category, key=lambda product: product["price"])}")

# 3 Move get_json to its own file
# Create a file called api_client.py and move the get_json function there. In your lab
# file, import it with from api_client import get_json. Run the lab again. It should
# work exactly as before. You will reuse this file in Lab 2.
# Implemented with modules

# 4 Create and change a product
# Build a dictionary for a new product (title, price, description, image, category, but no id).
# Send it with requests.post(..., json=...) and print the status code and the answer.
# Then change the price of an existing product, for example product 7, with
# requests.patch and a body that only contains the price. Print the answer. get_json
# only does GET, so here you call requests directly. Remember the timeout and check the
# status code.
new_product = {
    "title": "Wireless Headphones",
    "price": 49.99,
    "description": "Comfortable wireless headphones with high-quality sound.",
    "image": "https://sample_products.com/1",
    "category": "electronics"
}
response = requests.post(
    f"{url}/products",
    json=new_product,
    timeout=5
)
print(response.status_code)
print(response.json())

response = requests.patch(
    f"{url}/products/7",
    json={"price": 59.99},
    timeout=5
)
print(response.status_code)
print(response.json())

# 5 Break it on purpose
# Call your function with a wrong URL, with timeout=0.001, and with a made-up domain.
# For each one, read the message you get. The program must not crash, and every
# problem should give a short message that a human can read.
get_json(
    f"{url}/pproducts"
) # The server said no: 404 
get_json(
    f"{url}/pproducts",
    timeout=0.001
) # The requesst took too long
get_json(
    f"https://this-domain-does-not-exist.com"
) # Could not connect to the server

print("The app is not crashed!")
