# # Part A - List comprehensions

# # Create squares for numbers 1-20 using a normal loop, then a list comprehension.
# for number in range(1, 21):
#     print(number * number)
# print([number * number for number in range(1, 21)])

# # Create a list containing only even numbers from 1-100.
# pass

# # Convert a list of names to stripped, title-cased names.
# pass

# # Given scores, create a list containing only passing scores.
# pass

# # Create labels such as 'PASS'/'FAIL' for every score using a conditional expression in a comprehension.
# scores = [70, 60, 80]
# scores_labels = [{"score": score, "label": "PASS" if score >=
#                   70 else "FAIL"} for score in scores]
# print(scores_labels)

# # Rewrite three earlier loop-based transformations from Lessons 2-4 as comprehensions.
# pass


# # Part B - Dictionary and set comprehensions

# # Create a dictionary mapping numbers 1-10 to their squares.
# squares_dict = {number: number * number for number in range(1, 11)}
# print(squares_dict)

# # Given a list of words, create a dictionary mapping each word to its length.
# words = ["one", "two", "three"]
# word_lenght_dict = {word: len(word) for word in words}
# print(word_lenght_dict)

# # Given a list with duplicates, create a set comprehension containing lowercase normalized values.
# print({word.lower() for word in ["One", "Two", "Two"]})

# # Create a dictionary of only products whose price is below a chosen threshold.
# pass

# # Create a dictionary mapping student names to PASS/FAIL from a list of student dictionaries.
# names = ["Alice", "Bob"]
# scores = [99, 69]
# students = dict(zip(names, scores))
# print({name: "PASS" if score > 70 else "FAIL" for name, score in students.items()})


# # Part C - enumerate

# # Print a playlist with numbering starting at 1 using enumerate.
# print(*enumerate(["song 1", "song 2"], start=1))

# # Given a list of tasks, print Task 1:, Task 2:, etc.
# pass

# # Find and print indexes of all values above a threshold.
# values = [0, 1, 2]
# threshold = 1
# for i, value in enumerate(values):
#     if (i > threshold):
#         print(i)

# # Rewrite a range(len(...)) loop using enumerate and explain why the new version is clearer.
# for i in range(len(values)):
#     print(f"{i}: {values[i]}")

# for i, value in (enumerate(values)):
#     print(f"{i}: {value}") # value is ready


# # Part D - zip and unpacking

# # Combine separate name and score lists using zip and print each pair.
# pass

# # Create a dictionary using dict(zip(keys, values)).
# pass

# # Combine three lists: product name, price and stock.
# products = ["Laptop", "Phone", "Tablet"]
# prices = [999, 699, 399]
# stock = [10, 25, 15]

# combined = list(zip(products, prices, stock))

# print(combined)

# # Investigate what happens when zipped lists have different lengths.
# # Tuples length = shortest list length

# # Use tuple unpacking directly in a for loop over zipped data.
# for product, price, stock in zip(products, prices, stock):
#     print(f"Product: {product}, price: {price:.2f}, stock: {stock}")

# # Swap two variables without a temporary variable.
# x = 1
# y = 2
# y, x = x, y
# print(x, y)


# # Part E - sorted and lambda

# # Sort a list of words by length using sorted(..., key=...).
# print(sorted(["a", "abc", "ab"], key=len))

# # Sort a list of student dictionaries by score ascending and descending.
# students = [{"name": "Willy", "score": 80}, {
#     "name": "Billy", "score": 90}, {"name": "Dilly", "score": 70}]


# def get_score(student):
#     return student["score"]


# print(sorted(students, key=get_score))
# print(sorted(students, key=get_score, reverse=True))

# # Sort products by price using a lambda.
# products = [{"name": "Laptop", "price": 999.99},
#             {"name": "Phone", "price": 599.99}]
# print(sorted(products, key=lambda product: product["price"]))

# # Sort people by last name when each item is a dictionary containing first_name and last_name.
# pass

# # Write a normal named function for a sort key, then replace it with lambda. Compare when each is clearer.
# # Build-in functions are good candidates for lambdas.
# # If sorting logic is not trivial a named function looks clearer.


# # Part F - Applied challenge: Data cleanup

# # Start with a list of at least twelve messy dictionaries representing products:
# # inconsistent name casing/spacing, category, price and stock.
# products = [
#     {"name": "  laptop", "category": "Electronics", "price": 999.99, "stock": 10},
#     {"name": "PHONE", "category": "electronics", "price": 699.50, "stock": 25},
#     {"name": " wireless mouse ", "category": " Electronics ",
#         "price": 29.99, "stock": 50},
#     {"name": "KEYBOARD", "category": "ELECTRONICS", "price": 79.99, "stock": 0},
#     {"name": "  coffee mug", "category": "Home", "price": 12.50, "stock": 100},
#     {"name": "COFFEE MUG ", "category": " home ", "price": 14.00, "stock": 75},
#     {"name": "desk lamp", "category": "HOME", "price": 45.99, "stock": 0},
#     {"name": " NOTEBOOK", "category": " Stationery", "price": 5.99, "stock": 200},
#     {"name": "notebook  ", "category": "stationery", "price": 6.50, "stock": 150},
#     {"name": "  BACKPACK", "category": "Stationery", "price": 39.99, "stock": 30},
#     {"name": "water bottle ", "category": " SPORTS", "price": 19.99, "stock": 60},
#     {"name": " YOGA MAT", "category": "sports", "price": 24.99, "stock": 40},
# ]

# # Create a cleaned list where names/categories are normalized. Use comprehensions where readable.


# def normalize(string):
#     return string.strip().title() if string else ''


# products = [{**product, "name": normalize(product["name"])}
#             for product in products]
# print(products)

# # Create a list of in-stock products.
# in_stock_products = [{**product}
#                      for product in products if product["stock"] > 0]
# print(products)

# # Create a set of unique normalized categories.
# normalized_categories = {
#     normalize(product["category"]) for product in products}
# print(normalized_categories)

# # Create a dictionary mapping product name to inventory value (price * stock).
# inventory = {product["name"]: round(
#     product["price"] * product["stock"], 2) for product in products}
# print(inventory)

# # Sort products by inventory value from highest to lowest.
# # key=inventory.get
# print(sorted(inventory, key=lambda product: inventory[product], reverse=True))

# # Use enumerate to print a ranked report.
# for i, inventory_item in enumerate(inventory, start=1):
#     print(f"{i}. {inventory_item} - {inventory[inventory_item]}")

# # Use zip to combine at least one pair of separate derived lists in a meaningful way.
# pass

# # Write both a deliberately over-complicated comprehension and a clearer alternative.
# # Explain why the clearer version is preferable.
# valuable_products = [
#     (normalize(p["name"]), round(p["price"] * p["stock"], 2))
#     for p in products
#     if p["stock"] > 0
#     if round(p["price"] * p["stock"], 2) > 500
# ]

# valuable_products = []
# for product in products:
#     name = normalize(product["name"])
#     value = round(product["price"] * product["stock"], 2)

#     if product["stock"] > 0 and value > 500:
#         valuable_products.append((name, value))

# # Second variant has much better readability


# Part G - Stretch challenges

# Flatten a simple list of lists using a comprehension.
seasons = [
    ["December", "January", "February"],
    ["March", "April", "May"],
    ["June", "July", "August"],
    ["September", "October", "November"]
]

print([month for season in seasons for month in season])

# Create a multiplication table structure using a nested comprehension,
# then decide whether the result is readable enough.
table = [[row * column for row in range(1, 11)] for column in range(1, 11)]

print(table)

# Given names and scores, create only passing student dictionaries in one readable comprehension.
names = ["Billy", "Dilly", "Willy"]
scores = [70, 80, 90]

print({name: score for name, score in zip(names, scores) if score >= 70})

# Use any() and all() to answer useful questions about a score list, after first solving them with loops.
for score in scores:
    if score < 70:
        print("Someone failed")
        break

print(f"Any failed? {any(score < 70 for score in scores)}")
print(f"All passed? {all(score >= 70 for score in scores)}")

# Create five examples where Pythonic syntax reduces boilerplate without reducing clarity.
squares = [x**2 for x in range(5)]
doubled = {x: x * 2 for x in range(5)}
print(*enumerate(squares, start=1))
print(sorted(doubled, reverse=True))
print(dict(zip(names, scores)))
