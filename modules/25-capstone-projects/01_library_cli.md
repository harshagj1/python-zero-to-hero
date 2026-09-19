# Capstone 1 — Library Management CLI

## Goal

A terminal app for a small library: add books, borrow, return, search, persist to disk.

## Skills proven

OOP, dataclasses, file/JSON or SQLite, argparse or menu CLI, exceptions, tests

## Requirements

- Book: title, author, isbn, available (bool)
- Member: name, member_id
- Commands:
  - add book
  - list books
  - search by title/author
  - borrow book (fails if unavailable)
  - return book
  - save/load automatically
- Reject invalid input cleanly
- Tests for borrow/return rules

## Stretch

- Due dates with `datetime`
- Export catalog to CSV
- Use SQLite instead of JSON

## Acceptance checklist

- [ ] Can restart app and still see books
- [ ] Cannot borrow an already borrowed book
- [ ] README with run instructions
- [ ] At least 5 pytest tests
