# ==================================================
# TASK 1
# ==================================================

products = [
    {"name": "Laptop", "price": 12000, "stock": 4},
    {"name": "Mouse", "price": 350, "stock": 0},
    {"name": "Keyboard", "price": 800, "stock": 6},
    {"name": "Monitor", "price": 3200, "stock": 3},
    {"name": "Headset", "price": 950, "stock": 0},
    {"name": "Webcam", "price": 1100, "stock": 5}
]

# 1. Loop through the products.
# 2. Print the name of every product that is in stock.
# 3. Calculate the total value of all products in stock.
#    The value of a product is price * stock.
# 4. Print the total value.
# 5. Keep track of which in-stock product has the highest price
#    without using max(), and print its name.


# Write your solution below:
total = 0
most_expensive_product = {}

for product in products:
    stock = product["stock"]

    if stock > 0:
        print(product["name"])
        price = product["price"]
        total += price * stock
        if (price > most_expensive_product.get("price", 0)):
            most_expensive_product = product

print(f"Total: {total}")

if (most_expensive_product):
    print(f"Most expensive product: {most_expensive_product["name"]}")


# ==================================================
# TASK 2
# ==================================================

scores = [78, 92, 55, 81, 67, 95, 73]

# Create a function called calculate_average that:
# - receives a list of scores
# - calculates and returns the average score
#
# Create another function called create_result that:
# - receives a list of scores
# - uses calculate_average()
# - returns "PASS" if the average is 70 or higher
# - otherwise returns "FAIL"
#
# Call create_result() using the scores above.
# Print both the average score and the final result.


# Write your solution below:
def calculate_average(scores):
    if not scores:
        raise ValueError("At least one score is required")
    return sum(scores) / len(scores)


def create_result(scores):
    return "PASS" if calculate_average(scores) >= 70 else "FAIL"


print(f"Average score: {calculate_average(scores):.2f}")
print(f"Result: {create_result(scores)}")


# ==================================================
# TASK 3
# ==================================================

product_prices = [250, 400, 150, 700]

order_settings = {
    "discount": 10,
    "shipping": 49,
    "priority": True
}

# Create a function called calculate_order that:
# - receives a customer name as a normal parameter
# - receives any number of product prices using *args
# - receives optional settings using **kwargs
# - calculates the subtotal of all product prices
# - applies the discount percentage if "discount" exists
# - adds shipping if "shipping" exists
# - returns a dictionary containing:
#       customer
#       subtotal
#       final_total
#       settings
#
# Call the function using:
# - customer name "Anna"
# - the values from product_prices using unpacking
# - the values from order_settings using dictionary unpacking
#
# Print the returned dictionary.


# Write your solution below:
def calculate_order(customer, *prices, **settings):
    subtotal = sum(prices)
    discount = subtotal * settings.get("discount", 0) / 100.00
    shipping = settings.get("shipping", 0)
    final_total = subtotal - discount + shipping

    return {
        "customer": customer,
        "subtotal": subtotal,
        "final_total": final_total,
        "settings": settings
    }


print(calculate_order("Anna", *product_prices, **order_settings))

# ==================================================
# TASK 4
# ==================================================

players = [
    {"name": "  anna", "score": 85, "active": True},
    {"name": "DAVID ", "score": 72, "active": False},
    {"name": " sara ", "score": 94, "active": True},
    {"name": "LEO", "score": 67, "active": True},
    {"name": " emma", "score": 88, "active": True},
    {"name": "OSCAR ", "score": 76, "active": False}
]

# 1. Create a new list containing normalized player names.
#    Remove unnecessary whitespace and use consistent capitalization.
#    Use a list comprehension.
#
# 2. Create a new list containing only the active players
#    with a score of 80 or higher.
#    Use a list comprehension.
#
# 3. Sort the original players by score from highest to lowest.
#    Use sorted() with a lambda.
#
# 4. Print the ranking in the following format:
#
#    1. Sara - 94
#    2. Emma - 88
#    ...
#
#    Generate the ranking numbers using enumerate().
#
# 5. Create a separate list containing the player names and
#    another list containing their scores.
#    Combine them using zip() and print each name together
#    with its score.


# Write your solution below:
# 1
players_names = [player["name"].strip().title() for player in players]
print(players_names)

# 2
active_players = [
    player for player in players
    if player["active"] and player["score"] >= 80]
print(active_players)

# 3
print(sorted(players, key=lambda player: player["score"], reverse=True))

# 4
for i, player in enumerate(players, start=1):
    print(f"{i}. {player["name"]} - {player["score"]}")

# 5
players_scores = [player["score"] for player in players]
for player in zip(players_names, players_scores):
    print(f"Name: {player[0]}, score: {player[1]}")
