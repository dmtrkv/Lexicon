import sqlite3
# conn = sqlite3.connect("./Labs/webshop.db") # 1. connect
# conn.execute("PRAGMA foreign_keys = ON") # 1.1. turn on FKs
# cursor = conn.cursor() # 2. get a cursor
# cursor.execute("SELECT first_name, last_name, city FROM customers") # 3. run SQL
# rows = cursor.fetchall() # 4. get the answer
# conn.commit() / conn.rollback() # 4.1. commit or rollback
# conn.close()

# Exercise 1
# Write a script that prints all customers as 'First Last (City)'.
# Expected: 10 lines
# conn = sqlite3.connect("./Labs/webshop.db")
# cursor = conn.cursor()
# cursor.execute("SELECT first_name, last_name, city FROM customers")
# rows = cursor.fetchall()
# for idx, (first_name, last_name, city) in enumerate(rows, start=1):
#     print(f"{idx}. {first_name} {last_name} ({city})")
# conn.close()

# Exercise 2
# Ask the user for a max price and show all products cheaper than that. Use a ? placeholder.
# conn = sqlite3.connect("./Labs/webshop.db")
# cursor = conn.cursor()
# price = input("Enter max price: ")
# cursor.execute("SELECT name, price FROM products WHERE price < ?", (price,))
# rows = cursor.fetchall()
# for idx, (name, price) in enumerate(rows, start=1):
#     print(f"{idx}. {name} {price} kr")
# conn.close()

# Exercise 3
# Ask the user for a category and print how many products it has. Use COUNT and fetchone().
# conn = sqlite3.connect("./Labs/webshop.db")
# cursor = conn.cursor()
# category = input("Enter category: ")
# cursor.execute("SELECT count(*) FROM products WHERE category = ?", (category,))
# result = cursor.fetchone()
# print(f"Category '{category}' has {result[0]} products")
# conn.close()

# Exercise 4
# Explain in your own words: why is building SQL with an f-string dangerous, and why is a ?
# placeholder safe?
# Expected: a few sentences
# With f-string any SQL can be injected.
# With `?` it cannot be, as such input is considered as value not executable code.

# Exercise 5
# Add a menu option 4 to shop.py: change the stock of a product. Ask for the product id and the new
# stock.
# See: shop.py

# Exercise 6
# Add a menu option 5 to shop.py: show an order's receipt. Ask for the order_id and use a JOIN to
# show product names.
# See: shop.py

# Exercise 7
# What happens in add_product if the user types abc as the price? Fix it with try/except.
# See: shop.py

# Exercise 8
# Challenge: add a menu option 6, 'top 3 best-selling products'. Use GROUP BY, ORDER BY and
# LIMIT.
# Expected: 3 lines
# See: shop.py
