--Exercise 9
--Anna (customer 1) asks: 'Which products have I bought?' Write the query that answers her. Show
--product names only, each once.
--Expected: 4 rows
SELECT DISTINCT p.name FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
WHERE c.customer_id = 1;

--Exercise 10
--Erik says his email is wrong. Correct it to erik.johansson@example.com.
--Expected: 1 row changed
UPDATE customers SET email = 'erik.johansson@example.com'
WHERE customer_id = (
	SELECT customer_id FROM customers
	WHERE first_name = 'Erik' AND last_name = 'Johansson'
);

--Exercise 11
--Create a view customer_overview that a support person can use: customer_id, first name, city and
--number of orders, but no email. Customers with no orders must also be shown.
--Expected: 10 rows when you SELECT from the view
CREATE VIEW customer_overview AS
SELECT
    c.customer_id,
    c.first_name,
    c.city,
    COUNT(o.order_id) AS number_of_orders
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id;
	
SELECT * FROM customer_overview;

--Exercise 12
--Discuss in pairs: the webshop wants to add a birth_date column 'just in case'. What would you
--say? Write two sentences.
--Expected: two sentences
--According to suggestions, if you don't really need some data - don't save it.
--Also 'birth_date' is a personal information.
 