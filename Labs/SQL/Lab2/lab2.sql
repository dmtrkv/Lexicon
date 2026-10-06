--Exercise 1
--Create a table books with: book_id (primary key), title (must have a value), author, year (whole
--number).
CREATE TABLE books (
	book_id INTEGER PRIMARY KEY,
	title TEXT NOT NULL,
	author TEXT,
	year INTEGER
);

--Exercise 2
--Add a rule to books so year must be greater than 1400. (Hint: DROP and CREATE again.)
DROP TABLE books;
CREATE TABLE books (
	book_id INTEGER PRIMARY KEY,
	title TEXT NOT NULL,
	author TEXT,
	year INTEGER CHECK (year > 1400)
);

--Exercise 3
--Add a column isbn to books. It should be TEXT.
ALTER TABLE books
ADD COLUMN isbn TEXT;

--Exercise 4
--Delete the books table.
DROP TABLE books;

--Exercise 5
--Create a table reviews: review_id, product_id (points to products), rating (1 to 5), comment.
CREATE TABLE reviews (
	review_id INTEGER PRIMARY KEY AUTOINCREMENT,
	product_id INTEGER NOT NULL,
	rating INTEGER CHECK (rating BETWEEN 1 AND 5),
	comment TEXT,
	FOREIGN KEY (product_id) REFERENCES products (product_id)
);

--Exercise 6
--Test reviews: try to add a review with rating 6. What happens?
INSERT INTO reviews (product_id, rating, comment)
VALUES (9, 6, 'A must!'); -- CHECK constraint failed: rating BETWEEN 1 AND 5

--Exercise 7
--Test reviews: try to add a review for product 50. What happens?
INSERT INTO reviews (product_id, rating)
VALUES (50, 5); -- FOREIGN KEY constraint failed

--Exercise 8
--On paper: draw the 4 webshop tables as boxes and draw arrows for each foreign key.
