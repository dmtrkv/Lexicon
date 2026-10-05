--LAB1:

--Show the first name and email of all customers. (10 rows)
SELECT first_name, email FROM customers;

--Show all products in the Shoes category. (3 rows)
SELECT * FROM products WHERE category = 'Shoes';

--Which customers live in Uppsala? (3 rows)
SELECT * FROM customers WHERE city = 'Uppsala';

--Which product costs exactly 199 kr? (1 row)
SELECT * FROM products WHERE price = 199.00;

--Show all products sorted by name, A to Z. (12 rows)
SELECT * FROM products ORDER BY name;

--Show all customers, the one who joined first at the top. (10 rows)
SELECT * FROM customers ORDER BY joined_date;

--Which products are sold out (stock is 0)? (2 rows)
SELECT * FROM products WHERE stock < 1;

--Show the 3 newest customers. (3 rows)
SELECT * FROM customers ORDER BY joined_date DESC LIMIT 3;

--Show customers from Stockholm or Göteborg. Use IN. (4 rows)
SELECT * FROM customers WHERE city IN ('Stockholm', 'Göteborg');

--Show product name and price, but call the columns product and price_sek. (12 rows)
SELECT name AS product, price as price_sek FROM products;


--Bonus questions:

--Show products that are Clothing or Shoes and cost more than 1000 kr. 
--Hint: you need brackets. Try without them too: why is the answer different? (3 rows)
SELECT * FROM products WHERE category IN ('Clothing', 'Shoes') AND price > 1000.00;

--For every product in stock, show name, price, stock 
--and the total value of the stock (price × stock) as stock_value. Highest value first. (10 rows)
SELECT name, price, stock, price * stock AS stock_value FROM products 
WHERE stock > 0 ORDER BY stock_value;

--Which customers have a first name with exactly 4 letters? 
--Hint: _ in LIKE means "exactly one character". (4 rows)
SELECT * FROM customers WHERE first_name LIKE '____';

--Sort the products by price, cheapest first, and show only products number 6 to 10. 
--Hint: look up OFFSET. (5 rows)
SELECT * FROM products ORDER BY price LIMIT 5 OFFSET 5;

--Show customers who joined before 2025 and don't live in Uppsala. 
--Sort by city, and by last name within the same city. (4 rows)
SELECT * FROM customers 
WHERE joined_date < '2025-01-01' AND city != 'Uppsala'
ORDER BY city, last_name;
