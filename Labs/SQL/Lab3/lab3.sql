--Exercise 1
--Add yourself as customer number 11 (use a made-up email).
INSERT INTO customers (customer_id, first_name, last_name, email, city, joined_date)
VALUES (11, 'D', 'M', 'd.m@example.com', 'Stockholm', '2026-09-07');

--Exercise 2
--Add two new products in one INSERT: Scarf (Accessories, 229 kr, 15 in stock) and Gloves
--(Accessories, 199 kr, 20 in stock).
INSERT INTO products (product_id, name, category, price, stock)
VALUES
  (13, 'Scarf', 'Accessories', 229, 15),
  (14, 'Gloves', 'Accessories', 199, 20);

--Exercise 3
--Customer 7 (Emma) orders 2 Beanies (product 10, 179 kr). Make the order (order 16) and the
--order item.
INSERT INTO orders (order_id, customer_id, order_date)
VALUES (16, 7, '2026-10-07');
INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES (16, 10, 2, 179.00);

--Exercise 4
--Try to add an order item with quantity 0. Which rule stops you?
INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES (16, 14, 0, 199.00); -- CHECK constraint failed: quantity > 0

--Exercise 5
--Order 12 has been shipped. Change its status.
UPDATE orders SET status = 'shipped'
WHERE order_id = 12;

--Exercise 6
--The Water Bottle (product 5) is back in stock: 50 pieces.
UPDATE products SET stock = 50
WHERE product_id = 5;

--Exercise 7
--Raise the price of all Accessories by 10%.
UPDATE products SET price = price * 1.1
WHERE category = 'Accessories';

--Exercise 8
--Delete the cancelled order. Watch out: its items must go first! Why?
DELETE FROM order_items 
WHERE order_id = (
	SELECT order_id FROM orders
	WHERE status = 'cancelled'
	); -- There is no 'ON DELETE CASCADE'
DELETE FROM orders
WHERE status = 'cancelled';
