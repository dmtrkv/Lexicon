import sqlite3
 
 
def connect():
    conn = sqlite3.connect("./Labs/webshop/webshop.db")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn
 
 
def list_products(conn):
    cursor = conn.execute("SELECT product_id, name, price, stock FROM products")
    for pid, name, price, stock in cursor.fetchall():
        print(f"{pid:>3}  {name:<20} {price:>8.2f} kr  ({stock} in stock)")
 
 
def search_customers(conn):
    city = input("City: ")
    cursor = conn.execute(
        "SELECT first_name, last_name FROM customers WHERE city = ?", (city,))
    rows = cursor.fetchall()
    if not rows:
        print("No customers found.")
    for first, last in rows:
        print(first, last)
 
 
def add_product(conn):
    try:
        name = input("Name: ")
        category = input("Category: ")
        price = float(input("Price: "))
        stock = int(input("Stock: "))
    except ValueError:
        print("Price is float, stock is integer")
        return
    conn.execute(
        "INSERT INTO products (name, category, price, stock) VALUES (?, ?, ?, ?)",
        (name, category, price, stock))
    conn.commit()
    print("Saved!")

def change_stock(conn):
    pid = input("Enter product ID: ")
    new_stock = int(input("Enter new stock: "))
    conn.execute(
        "UPDATE products SET stock = ? WHERE product_id = ?",
        (new_stock, pid))
    conn.commit()
    print("Updated!")


def show_receipt(conn):
    order_id = input("Enter order ID: ")
    cursor = conn.execute("""
        SELECT p.name, oi.quantity, oi.unit_price
        FROM order_items AS oi
        JOIN products AS p ON oi.product_id = p.product_id
        WHERE oi.order_id = ?
    """, (order_id,))

    rows = cursor.fetchall()
    if not rows:
        print("No items found for this order.")
        return

    print(f"\n--- Receipt for Order #{order_id} ---")
    total = 0

    for name, quantity, price in rows:
        subtotal = quantity * price
        print(f"{name} x {quantity} ({price:.2f}) = {subtotal:.2f}")
        total += subtotal

    print("-" * 35)
    print(f"Total: {total:.2f}")

def show_bestsellers(conn, limit):
    cursor = conn.execute("""
            SELECT p.name, SUM(oi.quantity) AS total_sold FROM order_items AS oi
            JOIN products AS p ON oi.product_id = p.product_id
            GROUP BY p.name
            ORDER BY total_sold DESC
            LIMIT ?
        """, (limit,))
    rows = cursor.fetchall()
    for idx, (product_name, quantity) in enumerate(rows, start=1):
            print(f"{idx}. {product_name} x {quantity} sold")
    
 
def main():
    conn = connect()
    while True:
        print("\n" \
        "1) List products  " \
        "2) Search customers  " \
        "3) Add product  " \
        "4) Update stock  " \
        "5) Show order receipt  " \
        "6) Show 3 bestsellers  " \
        "0) Quit")

        choice = input("> ")
        if choice == "1":
            list_products(conn)
        elif choice == "2":
            search_customers(conn)
        elif choice == "3":
            add_product(conn)
        elif choice == "4":
            change_stock(conn)
        elif choice == "5":
            show_receipt(conn)
        elif choice == "6":
            show_bestsellers(conn, 3)
        elif choice == "0":
            break
    conn.close()
 
 
main()
 