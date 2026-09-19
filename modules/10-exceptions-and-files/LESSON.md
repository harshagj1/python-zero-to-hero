# Module 10 — Exceptions and Files

## Layman idea

Two truths of real software:

1. Things go wrong (bad input, missing files, network fail)
2. Programs must remember things (files, databases)

**Exceptions** = Python's way of saying “something went wrong.”
**Files** = saving/loading data on disk.

## Exceptions

```python
try:
    number = int(input("Age: "))
except ValueError:
    print("That was not a number.")
else:
    print("Thanks,", number)
finally:
    print("This always runs")
```

| Block | When it runs |
|-------|----------------|
| `try` | Code that might fail |
| `except` | Handler for a failure type |
| `else` | If try succeeded |
| `finally` | Always (cleanup) |

### Raise your own

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount
```

### Pro habits

- Catch **specific** exceptions (`ValueError`), not bare `except:`
- Don't silence errors unless you have a reason
- Put cleanup in `finally` or use context managers (`with`)

## Files with `with` (always prefer this)

```python
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Hello file\n")

with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

`with` auto-closes the file even if errors happen.

### Modes

| Mode | Meaning |
|------|---------|
| `"r"` | Read |
| `"w"` | Write (overwrite) |
| `"a"` | Append |
| `"x"` | Create new (fail if exists) |
| `"rb"`/`"wb"` | Binary |

### Line by line (big files)

```python
with open("log.txt", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

## pathlib (modern pro style)

```python
from pathlib import Path

path = Path("data") / "notes.txt"
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text("hello\n", encoding="utf-8")
print(path.read_text(encoding="utf-8"))
```

## JSON files (very common)

```python
import json
from pathlib import Path

data = {"name": "Ada", "skills": ["python"]}
Path("ada.json").write_text(json.dumps(data, indent=2), encoding="utf-8")
loaded = json.loads(Path("ada.json").read_text(encoding="utf-8"))
```

## Exercises

1. Ask for a number; handle non-numeric input without crashing.
2. Write three lines to `practice.txt`, then read them back.
3. Save a dict as JSON and load it.
4. Raise `ValueError` if a function receives a negative age.

## Checkpoint B preview

Expense tracker: classes + JSON file storage.

## Next

Run `exceptions_files_demo.py`, then **Module 11**.
