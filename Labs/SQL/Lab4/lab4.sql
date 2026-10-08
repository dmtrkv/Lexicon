--Exercise 1
--Show every order with the customer's first name, last name and the order status.
--Expected: 15 rows
SELECT c.first_name, c.last_name, o.status FROM orders o 
JOIN customers c ON o.customer_id = c.customer_id;

--Exercise 2
--Show all orders made by Erik.
--Expected: 3 rows
SELECT * FROM orders o 
JOIN customers c ON o.customer_id = c.customer_id
WHERE c.first_name = 'Erik';

--Exercise 3
--Show all orders from customers in Göteborg, newest first.
--Expected: 3 rows
SELECT * FROM orders o 
JOIN customers c ON o.customer_id = c.customer_id
WHERE c.city = 'Göteborg'
ORDER BY o.order_date DESC;

--Exercise 4
--Show every order item with the product name and category.
--Expected: 23 rows
SELECT p.name, p.category FROM order_items oi 
JOIN products p ON oi.product_id = p.product_id; 

--Exercise 5
--Which orders contained Shoes? Show order_id and product name.
--Expected: 4 rows
SELECT o.order_id, p.name FROM orders o 
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
WHERE p.category = 'Shoes'; 

--Exercise 6
--Show the full receipt for order 10: product name, quantity, unit price and line total.
--Expected: 2 rows
SELECT p.name, oi.quantity, oi.unit_price, oi.quantity * oi.unit_price AS total_price FROM orders o 
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
WHERE o.order_id = 10;

--Exercise 7
--Show which customers have bought a Hoodie Black (first name and order date).
--Expected: 3 rows
SELECT c.first_name, o.order_date FROM orders o 
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
JOIN customers c ON o.customer_id = c.customer_id
WHERE p.name = 'Hoodie Black';

--Exercise 8
--Show all customers and their orders, including customers with no orders.
--Expected: 17 rows
SELECT * FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id;

--Exercise 9
--Which products have never been sold?
--Expected: 2 rows
SELECT * FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id
WHERE oi.order_id IS NULL; 

--Exercise 10
--Challenge: show customers from Uppsala and every product they bought (first name, product
--name, quantity).
--Expected: 8 rows
SELECT c.first_name, p.name AS product_name, oi.quantity, o.order_id FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
WHERE c.city = 'Uppsala'
