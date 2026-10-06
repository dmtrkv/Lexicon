--Extra challenges: SELECT

--Level 1

--Exercise 1
--Show products that are not Accessories, are in stock, and have a space in their name. Sort by
--category, then by price from highest to lowest.
--Expected: 6 rows
SELECT * FROM products 
WHERE category NOT IN ('Accessories') AND stock > 0 AND name LIKE '% %'
ORDER BY category, price DESC;

--Exercise 2
--Show customers who live in a city starting with S or M, plus customers with no city at all.
--Expected: 4 rows
SELECT * FROM customers 
WHERE city LIKE 'S%' OR city LIKE 'M%' OR city IS NULL;

--Exercise 3
--Which Shoes product is the second most expensive? Show only that one.
--Expected: 1 row
SELECT * FROM products 
WHERE category = 'Shoes' 
ORDER BY price DESC LIMIT 1 OFFSET 1;

--Exercise 4
--Of the customers who joined in 2024 or 2025, show the 3 who joined most recently. Solve it
--without BETWEEN and without >=.
--Expected: 3 rows
SELECT * FROM customers 
WHERE joined_date LIKE '2024-__-__' OR joined_date LIKE '2025-__-__'
ORDER BY joined_date DESC LIMIT 3;

--Level 2
--Use the SQLite documentation: sqlite.org/lang_corefunc.html

--Exercise 5
--Show each customer's full name in one column called full_name (like "Anna Lindqvist"), sorted by
--last name.
--Look up: || · Expected: 10 rows
SELECT first_name || ' ' || last_name AS full_name FROM customers
ORDER BY last_name;

--Exercise 6
--Give every product a price level: budget under 200 kr, mid from 200 to 799 kr, premium from 800
--kr.
--Look up: CASE WHEN · Expected: 12 rows: 4 budget, 5 mid, 3 premium
SELECT name, price,
CASE 
	WHEN price < 200.00 THEN 'budget' 
	WHEN price BETWEEN 200.00 AND 799.00 THEN 'mid' 
	WHEN price >= 800.00 THEN 'premium' 
END AS price_level 
FROM products;

--Exercise 7
--Show every customer's first name and city, but write Unknown instead of NULL.
--Look up: COALESCE · Expected: 10 rows
SELECT first_name, coalesce(city, 'Unknown') as city_name FROM customers;

--Exercise 8
--Which customers joined in the first half of a year (January to June), whatever the year?
--Look up: strftime · Expected: 6 rows
SELECT * FROM customers 
WHERE strftime('%m', joined_date) BETWEEN '01' AND '06';

--Exercise 9
--Which product has the longest name?
--Look up: LENGTH · Expected: 1 row
SELECT name, length(name) as name_length FROM products
ORDER BY name_length DESC LIMIT 1;

--Exercise 10
--Show each customer's email username: the part before the @.
--Look up: substr and instr · Expected: 10 rows
SELECT substr(email, 0, instr(email, '@')) AS login, email FROM customers;

--Level 3

--Exercise 11
--Which products cost more than the average price? Don't type the average yourself: let SQL
--calculate it inside the query.
--Expected: 5 rows
SELECT name, price FROM products 
WHERE price > (
	SELECT avg(price) FROM products
	);

--Exercise 12
--Make a price list with one column that says, for example, "Socks 3-pack costs 129 kr". Only
--products in stock, cheapest first. Watch out: does it say 129 or 129.0? Fix it.
--Expected: 10 rows
SELECT name || ' costs ' || CAST(price AS INTEGER) || ' kr' AS price_list FROM products;

--Exercise 13
--How many customers live in each city? Biggest city first.
--Look up: GROUP BY · Expected: 6 rows
SELECT coalesce(city, 'Unknown') AS city_name, count(*) AS number_of_customers FROM customers 
GROUP BY city_name 
-- HAVING number_of_customers > 1
ORDER BY number_of_customers DESC;
