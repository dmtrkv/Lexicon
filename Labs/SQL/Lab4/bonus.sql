--Exercise 1
--Show products in Clothing or Accessories that cost between 150 and 500 kr. Most expensive first.
--Expected: 4 rows
SELECT * FROM products
WHERE category IN ('Clothing', 'Accessories') 
	AND price BETWEEN 150 AND 500
ORDER BY price DESC;

--Exercise 2
--Which orders were placed in February 2026 and are not cancelled?
--Expected: 4 rows
SELECT * FROM orders
WHERE order_date >= '2026-02-01' 
	AND order_date < '2026-03-01' 
	AND status != 'cancelled';

--Exercise 3
--Show every order line with the order_id, product name, quantity and line total (quantity times unit
--price). Only show lines where the line total is more than 500 kr. Biggest first.
--Expected: 11 rows
SELECT
  oi.order_id,
  p.name AS product_name,
  oi.quantity,
  oi.quantity * oi.unit_price AS line_total
FROM order_items oi
	JOIN products p ON oi.product_id = p.product_id
WHERE oi.quantity * oi.unit_price > 500
ORDER BY line_total DESC;

--Exercise 4
--Which customers from Uppsala or Stockholm have placed at least one order? Each customer only
--once.
--Expected: 5 rows
SELECT DISTINCT c.first_name, c.last_name FROM customers c
	JOIN orders o ON c.customer_id = o.customer_id
WHERE c.city IN ('Uppsala', 'Stockholm');

--Exercise 5
--A new customer, Leo Falk from Uppsala, places an order today: 1 Hoodie Black and 2 Socks
--3-pack. Add the customer, the order and the order lines. Then show the receipt with product
--names using a JOIN.
--Expected: the receipt has 2 rows
INSERT INTO customers (customer_id, first_name, last_name, email, city, joined_date)
	VALUES (11, 'Leo', 'Falk', 'leo.falk@example.com', 'Uppsala', '2026-10-09');
	
INSERT INTO orders (order_id, customer_id, order_date)
	VALUES (16, 11, '2026-10-09');
	
INSERT INTO order_items (order_id, product_id, quantity, unit_price)
	VALUES (16, 1, 1, 599.00), 
	       (16, 9, 2, 129.00);
		   
SELECT p.name, oi.quantity FROM products p
	JOIN order_items oi ON p.product_id = oi.product_id
WHERE oi.order_id = 16;

--Exercise 6
--Order 12 is cancelled. Change its status, and put its products back in stock. Look at its order lines
--first to see which products and how many.
--Expected: Sneakers Classic goes from 12 to 13 in stock, Socks 3-pack from 100 to 101
UPDATE orders 
SET status = 'cancelled'
WHERE order_id = 12;

UPDATE products
SET stock = stock + (
	SELECT quantity FROM order_items
	WHERE order_id = 12 
		AND product_id = products.product_id
)
WHERE products.product_id IN (
	SELECT product_id FROM order_items
	WHERE order_id = 12
);

--Exercise 7
--Try to delete Hoodie Black (product 1). What happens, and why? How could the shop stop selling it
--without deleting it?
--Expected: an error
DELETE FROM products
WHERE product_id = 1;
-- set its stock to 0

--Exercise 8
--Add a column discount_percent to products. It should be 0 if nothing is given and can only be
--between 0 and 90. Give all Shoes 20 percent off. Then show every product with its price and its
--price after discount.
--Look up: ALTER TABLE ... ADD COLUMN · Expected: 12 rows
ALTER TABLE products
ADD COLUMN discount_percent REAL 
	DEFAULT 0.0 CHECK (discount_percent BETWEEN 0 AND 90);
		
UPDATE products
SET discount_percent = 20
WHERE category = 'Shoes';

SELECT name, price, discount_percent, 
	price * (1 - discount_percent / 100.0) AS discounted_price
FROM products;

--Exercise 9
--Show every product with the dates it was ordered. Products that were never ordered must also be
--shown, with an empty date. Sort by product name.
--Expected: 25 rows
SELECT p.name, o.order_date
FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id
LEFT JOIN orders o ON oi.order_id = o.order_id
ORDER BY p.name;

--Exercise 10
--Which customers have bought something from the Shoes category? Each customer only once.
--Expected: 3 rows
SELECT DISTINCT * FROM customers c
JOIN orders o ON c.customer_id = o.order_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
WHERE p.category = 'Shoes';

--Exercise 11
--Show all pairs of customers who live in the same city, for example Anna and Johan. Each pair
--should only appear once.
--Look up: self join (a table joined with itself) · Expected: 5 pairs
SELECT c.first_name || ' ' || cc.first_name AS neighbours, c.city FROM customers c
JOIN customers cc ON c.city = cc.city 
	AND c.customer_id < cc.customer_id;

--Exercise 12
--The price of Hoodie Black goes up to 649 kr. Change it, then find all order lines where the
--customer paid a different price than today's price. Show order_id, product name, what they paid
--and today's price.
--Expected: 3 rows
UPDATE products
SET price = 649.0
WHERE product_id = 1;

SELECT
    oi.order_id,
    p.name AS product_name,
    oi.unit_price AS paid_price,
    p.price AS new_price,
	p.price - oi.unit_price AS diff
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
WHERE oi.unit_price <> p.price;
