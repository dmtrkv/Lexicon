--Level 1
--Exercise 1
--Create a table suppliers with supplier_id (primary key), name (must have a value and must be
--unique), country (Sweden if nothing is given) and email.
--Expected: Runs without errors
CREATE TABLE suppliers (
	supplier_id INTEGER PRIMARY KEY,-- AUTOINCREMENT,
	name TEXT NOT NULL UNIQUE,
	country TEXT DEFAULT 'Sweden',
	email TEXT
);

--Exercise 2
--Add a supplier without giving a country. Then show all suppliers. What does the country column
--say?
--Expected: 1 row, country is Sweden
INSERT INTO suppliers(name, email)
	VALUES ('Ann', 'ann@sup.com');
SELECT * FROM suppliers; -- country: Sweden

--Exercise 3
--Try to add a second supplier with the same name, Nordic Textiles. What happens, and which rule
--stopped you?
--Expected: An error
INSERT INTO suppliers(name, email)
	VALUES ('Ann', 'ann@sup.com'); -- UNIQUE constraint failed: suppliers.name

--Exercise 4
--Create a table coupons where the code itself (for example 'SUMMER20') is the primary key.
--discount_percent must be between 1 and 90, and valid_until must have a value. Then try to add a
--coupon with 95 percent off.
--Expected: The table is created, the INSERT gives an error
CREATE TABLE coupons (
    code TEXT PRIMARY KEY,
    discount_percent INTEGER CHECK (discount_percent BETWEEN 1 AND 90),
    valid_until TEXT NOT NULL
);
INSERT INTO coupons (code, discount_percent, valid_until)
	VALUES ('SUMMER20', 95, '2026-12-31'); -- CHECK constraint failed: discount_percent BETWEEN 1 AND 90

--Level 2
--Use the SQLite documentation: sqlite.org/lang_createtable.html and sqlite.org/lang_altertable.html
--Exercise 5
--Add a supplier without giving a supplier_id. Which id does it get? Why?
--Look up: INTEGER PRIMARY KEY · Expected: 1 new row
INSERT INTO suppliers(name, email)
	VALUES ('Bob', 'bob@sup.com'); -- supplier_id = 1

--Exercise 6
--Rename the column email in suppliers to contact_email.
--Look up: ALTER TABLE ... RENAME COLUMN · Expected: Runs without errors
ALTER TABLE suppliers
RENAME COLUMN email TO contact_email;

--Exercise 7
--Show the columns of the products table using SQL, not the Database Structure tab.
--Look up: PRAGMA table_info · Expected: 5 rows, one per column
PRAGMA table_info(products);

--Exercise 8
--A product can come from many suppliers, and a supplier can deliver many products. Create the
--middle table product_suppliers with a purchase price that must be more than 0. The same pair
--can only appear once. Then try to connect product 1 to supplier 99.
--Look up: PRIMARY KEY with two columns · Expected: The table is created, the INSERT gives
--an error
CREATE TABLE product_suppliers(
	product_id INTEGER NOT NULL,
	supplier_id INTEGER NOT NULL,
	purchase_price REAL CHECK (purchase_price > 0.00),
	PRIMARY KEY (product_id, supplier_id),
	FOREIGN KEY (product_id) REFERENCES products (product_id),
	FOREIGN KEY (supplier_id) REFERENCES suppliers (supplier_id)
);
INSERT INTO product_suppliers (product_id, supplier_id, purchase_price)
	VALUES (1, 99, 999.99); -- FOREIGN KEY constraint failed

--Exercise 9
--Create a table campaigns with name, start_date and end_date. Add a rule that end_date can
--never be before start_date. Test it with a campaign that ends before it starts.
--Look up: CHECK that compares two columns · Expected: The table is created, the INSERT
--gives an error
CREATE TABLE campaigns (
    name TEXT,
    start_date TEXT,
    end_date TEXT,
    CHECK (end_date >= start_date)
);
INSERT INTO campaigns (name, start_date, end_date)
	VALUES ('Winter Sale', '2026-12-31', '2026-01-12'); -- CHECK constraint failed: end_date >= start_date


--Exercise 10
--Create a table product_sizes with an own id, product_id (points to products), size (only S, M, L or
--XL) and stock (0 if nothing is given). The same product can't have the same size twice. Test it by
--adding size M for product 1 twice.
--Look up: UNIQUE on two columns · Expected: The first INSERT works, the second gives an
--error
CREATE TABLE product_sizes (
    id INTEGER PRIMARY KEY,
    product_id INTEGER,
    size TEXT CHECK (size IN ('S', 'M', 'L', 'XL')),
    stock INTEGER DEFAULT 0,
    UNIQUE (product_id, size),
    FOREIGN KEY (product_id) REFERENCES products (product_id)
);
INSERT INTO product_sizes (product_id, size)
	VALUES (1, 'M');
INSERT INTO product_sizes (product_id, size)
	VALUES (1, 'M'); -- UNIQUE constraint failed: product_sizes.product_id, product_sizes.size

--Exercise 11
--Create a table employees where each employee can have a manager, who is also an employee in
--the same table. The boss has no manager. Add the boss and two employees who report to the
--boss.
--Look up: a foreign key that points to its own table · Expected: 3 rows
CREATE TABLE employees (
	id INTEGER PRIMARY KEY,
	name TEXT NOT NULL,
	manager_id INTEGER,
	FOREIGN KEY (manager_id) REFERENCES employees (id)
);
INSERT INTO employees (id, name)
	VALUES (1, 'boss');
INSERT INTO employees (id, name, manager_id)
	VALUES (2, 'emp1', 1);
INSERT INTO employees (id, name, manager_id)
	VALUES (3, 'emp2', 1);
	
--Exercise 12
--Create two tables: teams and players, where a player belongs to a team. Make it so that when a
--team is deleted, its players are deleted automatically. Add one team with two players, delete the
--team, and check the players table.
--Look up: ON DELETE CASCADE · Expected: 0 rows left in players
CREATE TABLE teams (
	id INTEGER PRIMARY KEY
);
CREATE TABLE players (
	id INTEGER PRIMARY KEY,
	team_id INTEGER NOT NULL,
	FOREIGN KEY (team_id) REFERENCES teams (id) ON DELETE CASCADE
);
INSERT INTO teams (id)
	VALUES(1);
INSERT INTO players (id, team_id)
	VALUES (1, 1),
	       (2, 1);
SELECT * FROM players;
DELETE FROM teams
	WHERE id = 1;
SELECT * FROM players;
