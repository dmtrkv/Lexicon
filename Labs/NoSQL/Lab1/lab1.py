from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# # Exercise 1
# # Print the name of every product in the Accessories category.
# # Expected: 4 names
# products = db.products.find({"category": "Accessories"})
# for product in products:
#     print(product["name"])

# # Exercise 2
# # Print the first and last name of every customer who lives in Göteborg.
# # Expected: 2 customers
# customers = db.customers.find({"city": "Göteborg"})
# for customer in customers:
#     print(customer["first_name"], customer["last_name"])

# # Exercise 3
# # Python: print the name and price of every product, one per line.
# # Expected: 12 lines
# products = db.products.find()
# for product in products:
#     print(f"Product: {product['name']:<20} Price: {product['price']:.2f}")

# # Exercise 4
# # Python: how many customers live in Uppsala? Use count_documents.
# # Expected: 3
# print(db.customers.count_documents({"city": "Uppsala"}))

# # Exercise 5
# # Python: find the product named Sandals with find_one and print how many are in stock.
# # Expected: 22
# sandals = db.products.find_one({"name": "Sandals"})
# print(sandals["stock"])

# # Exercise 6
# # Python: print the first name of every customer who gets the newsletter (newsletter is True).
# # Expected: 3 names
# subscribed_customers = db.customers.find({"newsletter": True})
# pprint(list(subscribed_customers))

# # Exercise 7
# # Python: add yourself as a customer with insert_one, without an _id. Print the inserted_id. Then find
# # yourself again with find_one and your email, and print yourself with pprint.
# # Expected: an ObjectId, then your document
# result = db.customers.insert_one({"first_name": "D",
#                                   "last_name": "M",
#                                   "email": "d.m@example.com",
#                                   "city": "Stockholm",
#                                   "joined": {
#                                       "$date": "2026-09-07T00:00:00.000Z"
#                                   },
#                                   "newsletter": True})
# print(result)
# pprint(db.customers.find_one({"email": "d.m@example.com"}))

# # Exercise 8
# # Python: add two new products with insert_many (give them _id 13 and 14, and include tags). Then
# # print how many products there are.
# # Expected: 14
# db.products.insert_many([{
#     "_id": 13,
#     "name": "Blue Cap",
#     "category": "Caps",
#     "price": 199,
#     "stock": 10,
#     "tags": [
#         "summer"
#     ],
#     "details": {
#         "color": "blue",
#         "material": "cotton"
#     }
# }, {
#     "_id": 14,
#     "name": "Green Cap",
#     "category": "Caps",
#     "price": 199,
#     "stock": 10,
#     "tags": [
#         "spring"
#     ],
#     "details": {
#         "color": "green",
#         "material": "cotton"
#     }
# }])

# print(db.products.count_documents({}))

# Exercise 9
# Python: print every customer as 'First Last (City)'. Customers without a city should show
# (unknown). Hint: dict.get().
# Expected: 10 lines
customers = db.customers.find()
for customer in customers:
    print(f"{customer.get('first_name')} {customer.get('last_name')} ({customer.get('city', 'Unknown')})")

# Exercise 10
# Challenge: print every order as 'Order 1: 2 items'. Hint: an order's items is a list, and len() works
# on lists.
# Expected: 15 lines
orders = db.orders.find()
for i, order in enumerate(orders, start=1):
    print(f"Order {i}: {len(order['items'])} items")
