--Exercise 13
--Practice lab. A cinema shows movies in two salons. Each movie has a title, a length in minutes and
--an age limit (0, 7, 11 or 15). A screening is one movie shown in one salon on a date and at a time.
--Customers buy tickets for screenings. Each ticket has a seat number and a price, and a seat can
--only be sold once per screening. Create cinema.db, draw the ER diagram and write CREATE TABLE
--with suitable constraints. Add test data: at least 3 movies, 4 screenings, 3 customers, 6 tickets,
--and one screening with no tickets. Then write three queries: all screenings with the movie title,
--sorted by date and time; every ticket with customer name, movie title and date; and the
--screenings that have no tickets sold.
--Expected: depends on your own test data
CREATE TABLE movies (
    movie_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    length_minutes INTEGER NOT NULL CHECK (length_minutes > 0),
    age_limit INTEGER NOT NULL CHECK (age_limit IN (0, 7, 11, 15))
);

CREATE TABLE salons (
    salon_id INTEGER PRIMARY KEY,
    salon_name TEXT NOT NULL UNIQUE
);

CREATE TABLE screenings (
    screening_id INTEGER PRIMARY KEY,
    movie_id INTEGER NOT NULL,
    salon_id INTEGER NOT NULL,
    screening_date TEXT NOT NULL,
    screening_time TEXT NOT NULL,
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
    FOREIGN KEY (salon_id) REFERENCES salons(salon_id),
    UNIQUE (salon_id, screening_date, screening_time)
);

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

CREATE TABLE tickets (
    ticket_id INTEGER PRIMARY KEY,
    screening_id INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    seat_number INTEGER NOT NULL CHECK (seat_number > 0),
    price REAL NOT NULL CHECK (price >= 0.0),
    FOREIGN KEY (screening_id) REFERENCES screenings(screening_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    UNIQUE (screening_id, seat_number)
);

INSERT INTO movies (movie_id, title, length_minutes, age_limit)
VALUES
    (1, 'Movie 1', 120, 7),
    (2, 'Movie 2', 105, 11),
    (3, 'Movie 3', 90, 0);

INSERT INTO salons (salon_id, salon_name)
VALUES
    (1, 'Salon 1'),
    (2, 'Salon 2');

INSERT INTO screenings
    (screening_id, movie_id, salon_id, screening_date, screening_time)
VALUES
    (1, 1, 1, '2026-11-01', '14:00'),
    (2, 2, 2, '2026-11-01', '16:00'),
    (3, 3, 1, '2026-11-02', '18:00'),
    (4, 1, 2, '2026-11-03', '20:00');

INSERT INTO customers (customer_id, first_name, last_name)
VALUES
    (1, 'Ann', 'A.'),
    (2, 'Bob', 'B.'),
    (3, 'Cid', 'C.');

INSERT INTO tickets
    (ticket_id, screening_id, customer_id, seat_number, price)
VALUES
    (1, 1, 1, 1, 120.00),
    (2, 1, 2, 2, 120.00),
    (3, 2, 3, 1, 110.00),
    (4, 2, 1, 2, 110.00),
    (5, 3, 2, 5, 95.00),
    (6, 3, 3, 6, 95.00);
	-- no tickets for scr 4

-- All screenings with movie title, sorted by date and time
SELECT
    s.screening_id,
    m.title AS movie_title,
    s.screening_date,
    s.screening_time,
    sa.salon_name
FROM screenings s
JOIN movies m ON s.movie_id = m.movie_id
JOIN salons sa ON s.salon_id = sa.salon_id
ORDER BY s.screening_date, s.screening_time;

-- Every ticket with customer name, movie title and date
SELECT
    t.ticket_id,
    c.first_name || ' ' || c.last_name AS customer_name,
    m.title AS movie_title,
    s.screening_date,
    s.screening_time,
    t.seat_number,
    t.price
FROM tickets t
JOIN customers c ON t.customer_id = c.customer_id
JOIN screenings s ON t.screening_id = s.screening_id
JOIN movies m ON s.movie_id = m.movie_id
ORDER BY s.screening_date, s.screening_time, t.seat_number;

-- Screenings with no tickets sold
SELECT
    s.screening_id,
    m.title AS movie_title,
    s.screening_date,
    s.screening_time,
    sa.salon_name
FROM screenings s
JOIN movies m ON s.movie_id = m.movie_id
JOIN salons sa ON s.salon_id = sa.salon_id
LEFT JOIN tickets t ON s.screening_id = t.screening_id
WHERE t.ticket_id IS NULL
ORDER BY s.screening_date, s.screening_time;
