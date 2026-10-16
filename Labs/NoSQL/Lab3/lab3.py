from pprint import pprint
from pymongo import MongoClient
from pymongo.errors import PyMongoError
client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# Exercise 1
# Design: a library app shows a book page with the book's title, author and all its reviews. Many
# members borrow the same book. Would you embed or reference the reviews? The members?
# Explain in two sentences.
# Expected: written answer
print("""
I would reference both. The number of reviews can grow indefinitely (in theory), 
and members should be modeled as separate entities.
""")

# Exercise 2
# Our orders copy the product name into each item. Give one advantage and one disadvantage of
# that copy.
# Expected: written answer
print("""
Advantage: order history contains exact product names for audit.
Disadvantage: if a product name changes, it must be copied again - otherwise, it will remain outdated.
""")

# # Exercise 3
# # Create a collection newsletter_signups with validation: email is required and must be a string, and
# # source can only be "web" or "store" (look up enum). Insert one valid and one invalid document.
# # Expected: the second insert fails
# db.create_collection(
#     "newsletter_signups",
#     validator={
#         "$jsonSchema": {
#             "bsonType": "object",
#             "required": ["email", "source"],
#             "properties": {
#                 "email": {
#                     "bsonType": "string",
#                     "description": "Email is required and must be a string"
#                 },
#                 "source": {
#                     "bsonType": "string",
#                     "enum": ["web", "store"],
#                     "description": "Source must be web or store"
#                 }
#             }
#         }
#     }
# )

# db.newsletter_signups.create_index("email", unique=True)

# db.newsletter_signups.insert_one(
#     {
#         "email": "test@mail.com",
#         "source": "web"
#     }
# )

# pprint(list(
#     db.newsletter_signups.find()
# ))

# try:
#     db.newsletter_signups.insert_one(
#         {
#             "email": "test@mail.com",
#             "source": "unknown"
#         }
#     )
# except PyMongoError as e:
#     print("Validation failed!")

# # Exercise 4
# # How many customers live in each city? Use $group. Biggest city first.
# # Expected: 6 rows (one with _id None)
# pprint(list(
#     db.customers.aggregate([
#         {
#             "$group": {
#                 "_id": "$city",
#                 "customers": {"$sum": 1}
#             }
#         },
#         {
#             "$sort": {"customers": -1}
#         },
#         # {
#         #     "$project": {
#         #         "_id": 0,
#         #         "city": "$_id",
#         #         "customers": 1
#         #     }
#         # }
#     ])
# ))

# # Exercise 5
# # What is the cheapest and the most expensive product in each category? Use $min and $max.
# # Expected: 3 rows
# pprint(list(
#     db.products.aggregate([
#         {
#             "$group": {
#                 "_id": "$category",
#                 "min_price": {"$min": "$price"},             
#                 "max_price": {"$max": "$price"}
#             }
#         }
#     ])
# ))

# # Exercise 6
# # How many orders does each customer have (all statuses)? Show only customers with 2 or more
# # orders. Hint: $match after $group works like HAVING.
# # Expected: 5 rows
# pprint(list(
#     db.orders.aggregate([
#         {
#             "$group": {
#                 "_id": "$customer_id",
#                 "total_orders": {"$sum": 1}
#             }
#         },
#         {
#             "$match": {
#                 "total_orders": {"$gte": 2}
#             }
#         }
#     ])
# ))

# Exercise 7
# For each order, show the _id and the number of items in it. Use $project with $size.
# Expected: 15 rows
pprint(list(
    db.orders.aggregate([
        {
            "$project": {
                "items": {"$size": "$items"}
            }
        }
    ])
))
