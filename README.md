# Lexicon

Lexicon is a collection of Python learning labs and small projects. The exercises cover Python fundamentals, databases, and web APIs. Most files are independent examples or exercises; run them individually from the repository root.

## Repository structure

- `Labs/Python/` — nine labs covering basics, collections, control flow, functions, scope, comprehensions, classes, and object-oriented programming.
- `Labs/SQL/` — SQL practice, including webshop and cinema examples.
- `Labs/NoSQL/` — MongoDB connection, query, and webshop seed exercises.
- `Labs/API/` — HTTP client exercises, API integrations, and a FastAPI movie API.
- `Checkpoints/` — checkpoint-style Python practice.
- `Projects/Bookable/` — an interactive in-memory booking system demo.

## Requirements

Use Python 3.10 or later for the API examples (they use modern type hints). The booking demo supports Python 3.8 or later. Some labs need third-party packages or local services:

- HTTP labs: `requests`
- GitHub token and FastAPI labs: `python-dotenv`
- FastAPI server: `fastapi` and `uvicorn`
- MongoDB labs: `pymongo` and a MongoDB server at `mongodb://localhost:27017/`
- SQL labs use SQLite and SQL scripts; a database browser or the `sqlite3` command-line tool may be useful.

Install only the dependencies needed for the lab you plan to run. For example:

```bash
python -m pip install requests python-dotenv
```

## Running examples

Run a standalone Python lab from the repository root:

```bash
python Labs/Python/Lab1/lab1.py
```

## Notes

- Database and network exercises may need a local database service or an internet connection.
- The MongoDB seed script drops and recreates the `customers`, `products`, and `orders` collections in its `webshop` database. Use it only when you intend to reset that sample data.
- Some exercise files contain unfinished prompts or commented-out solutions; they are intended for practice rather than as a complete application.
