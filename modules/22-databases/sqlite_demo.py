# Module 22 — SQLite demo
# Run: python sqlite_demo.py

from __future__ import annotations

import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "demo.db"


def main() -> None:
    if DB.exists():
        DB.unlink()

    with sqlite3.connect(DB) as conn:
        conn.execute(
            """
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL
            )
            """
        )
        people = [("Ada", 36), ("Alan", 41), ("Grace", 85)]
        conn.executemany("INSERT INTO users (name, age) VALUES (?, ?)", people)

        print("All users:")
        for row in conn.execute("SELECT id, name, age FROM users ORDER BY age"):
            print(" ", row)

        conn.execute("UPDATE users SET age = ? WHERE name = ?", (37, "Ada"))
        row = conn.execute(
            "SELECT name, age FROM users WHERE name = ?", ("Ada",)
        ).fetchone()
        print("Updated Ada:", row)

        conn.execute("DELETE FROM users WHERE name = ?", ("Alan",))
        count = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
        print("Remaining users:", count)


if __name__ == "__main__":
    main()
