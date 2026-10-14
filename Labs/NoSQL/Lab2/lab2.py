from datetime import datetime
from pprint import pprint
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# # Exercise 1
# # Show the name and price of all products that cost more than 1000 kr.
# # Expected: 3 products
# pprint(list(
#     db.products.find({"price": {'$gt': 1000.00}})
# ))

# # Exercise 2
# # Show all orders that are not delivered. Use $ne. Print the _id and status.
# # Expected: 8 orders
# pprint(list(
#     db.orders.find({"status": {'$ne': 'delivered'}}, {"status": 1})
# ))

# # Exercise 3
# # Show customers who live in Stockholm or Malmö, using $in.
# # Expected: 3 customers
# pprint(list(
#     db.customers.find({"city": {'$in': ['Stockholm', 'Malmö']}})
# ))

# # Exercise 4
# # Which products are white? Use dot notation.
# # Expected: 3 products
# pprint(list(
#     db.products.find({"details.color": "white"}, {"name": 1})
# ))

# # Exercise 5
# # Which products have the tag sport? Show only name and tags, without _id.
# # Expected: 3 products
# pprint(list(
#     db.products.find({"tags": "sport"}, {"_id": 0, "name": 1, "tags": 1})
# ))

# # Exercise 6
# # Show the 5 cheapest products, cheapest first. Only name and price.
# # Expected: 5 products
# pprint(list(
#     db.products.find({}, {"_id": 0, "name": 1, "price": 1}).sort({"price": 1}).limit(5)
# ))

# # Exercise 7
# # Which orders contain product 2 (T-shirt White)? Hint: dot notation works on arrays of objects too:
# # "items.product_id".
# # Expected: 4 orders
# pprint(list(
#     db.orders.find({"items.product_id": {'$eq': 2}})
# ))

# # Exercise 8
# # Raise the price of all Accessories by 20 kr with $inc. Then print the Accessories with their new
# # prices.
# # Expected: 4 products, each 20 kr more
# products = db["products"]

# pprint(list(
#     products.find({"category": "Accessories"})
# ))

# products.update_many({"category": "Accessories"}, {'$inc': {'price': 20}})

# pprint(list(
#     products.find({"category": "Accessories"})
# ))

# # Exercise 9
# # Add the tag "new" to the Rain Jacket without creating duplicates, and give it a field restock_date
# # with today's date (use datetime.now()).
# # Expected: 1 product with the new tag and field (the time will be yours)
# products = db["products"]

# pprint(products.find_one({"name": "Rain Jacket"}))

# products.update_one({"name": "Rain Jacket"}, {'$addToSet': {'tags': 'new'}})
# pprint(products.find_one({"name": "Rain Jacket"}))

# products.update_one({"name": "Rain Jacket"}, {'$set': {'restock_date': datetime.now()}})
# pprint(products.find_one({"name": "Rain Jacket"}))

# Exercise 10
# Challenge: delete all orders with status new placed before 2026-03-20. Count them first. Hint:
# dates in filters are datetime objects, like datetime(2026, 3, 20).
# Expected: 2, then 2 deleted
orders = db["orders"]

print("To delete: ", orders.count_documents({
    "status": "new", 
    "order_date": {'$lt': datetime(2026, 3, 20)}})
)

result = orders.delete_many({
    "status": "new", 
    "order_date": {'$lt': datetime(2026, 3, 20)}})
print("Deleted: ", result.deleted_count)

client.close
