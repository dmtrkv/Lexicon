--1. Show the name and price of all products. (12 rows)
SELECT name, price FROM products;

--2. Which customers live in Stockholm? (2 rows)
SELECT * FROM customers WHERE city = 'Stockholm';

--3. Which products cost more than 1000 kr? (3 rows)
SELECT * FROM products WHERE price > 1000.00;

--4. Show all Accessories, cheapest first. (4 rows)
SELECT * FROM products WHERE category = 'Accessories' ORDER BY price;

--5. Which products have fewer than 10 in stock? (4 rows)
SELECT * FROM products WHERE stock < 10;

--6. Which customers have a first name that starts with E? (2 rows)
SELECT * FROM customers WHERE first_name LIKE 'E%';

--7. Which customers joined during 2024? (3 rows)
SELECT * FROM customers WHERE joined_date BETWEEN '2024-01-01' AND '2024-12-31';

--8. Show the 5 cheapest products. (5 rows)
SELECT * FROM products ORDER BY price LIMIT 5;

--9. Which categories exist? Each should appear only once. (3 rows)
SELECT DISTINCT category FROM products;

--10. Challenge: Clothing that is in stock (stock > 0) and costs
--under 600 kr, most expensive first. (4 rows)
SELECT * FROM products 
WHERE category = 'Clothing' AND stock > 0 AND price < 600.00 
ORDER BY price DESC;
