# Module 22 — Databases with SQLite

## Layman idea

Files are fine until you need: searching, relations, consistency, concurrent updates.

A **database** stores structured data. **SQL** is the language you use to talk to many databases.

**SQLite** = a full database in a single file. Perfect for learning and many real apps.

## Mental model

| SQL idea | Plain English |
|----------|---------------|
| Table | Spreadsheet sheet |
| Row | One record |
| Column | One field |
| Primary key | Unique ID |
| Query | A question you ask the DB |

## Python + sqlite3

```python
import sqlite3

conn = sqlite3.connect("app.db")
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
""")
cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Ada", 36))
conn.commit()

for row in cur.execute("SELECT id, name, age FROM users"):
    print(row)

conn.close()
```

**Always use `?` placeholders** — never build SQL with f-strings for user input (SQL injection).

## CRUD

- **C**reate: `INSERT`
- **R**ead: `SELECT`
- **U**pdate: `UPDATE`
- **D**elete: `DELETE`

## Context manager style

```python
with sqlite3.connect("app.db") as conn:
    conn.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alan", 41))
```

## Next step after SQLite

- PostgreSQL / MySQL for multi-user production
- ORMs like SQLAlchemy / SQLModel for larger apps
- Migrations (Alembic) for evolving schemas

Learn SQL itself — ORMs don't remove the need to understand queries.

## Exercises

1. Create `books` table: title, author, year.
2. Insert 3 books; select all; select by author.
3. Update a year; delete one row.
4. Write a function `list_users(conn) -> list[tuple]`.

## Next

Run `sqlite_demo.py`, then **Module 23**.
