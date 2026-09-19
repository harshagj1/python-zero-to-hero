# Module 07 — Dictionaries and Sets

## Layman idea

A **dictionary** is a real dictionary: you look up a **word (key)** to get a **definition (value)**. Super fast lookup.

A **set** is a bag of unique items — duplicates disappear. Great for membership tests and “unique list” problems.

```python
person = {"name": "Ada", "age": 36}
tags = {"python", "ai", "python"}  # becomes {"python", "ai"}
```

## Dictionaries

### Create / read / write

```python
user = {
    "id": 1,
    "name": "Ada",
    "skills": ["python", "math"],
}

print(user["name"])
print(user.get("email"))          # None if missing (safe)
print(user.get("email", "n/a")) # default

user["email"] = "ada@example.com"
user["age"] = 37
del user["id"]
```

Prefer `.get` when the key might be missing — avoids crash.

### Looping

```python
for key, value in user.items():
    print(key, "=>", value)

for key in user:
    print(key)

for value in user.values():
    print(value)
```

### Nested dicts (very common in APIs/JSON)

```python
data = {
    "user": {
        "name": "Ada",
        "address": {"city": "London"}
    }
}
print(data["user"]["address"]["city"])
```

## Sets

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # union
print(a & b)   # intersection
print(a - b)   # difference
print(2 in a)  # True — fast membership
```

Convert list → unique values:

```python
nums = [1, 2, 2, 3, 3, 3]
unique = list(set(nums))
```

Note: sets are unordered (don't rely on order).

## When pros choose what

| Structure | Best for |
|-----------|----------|
| list | Ordered sequence, duplicates OK |
| tuple | Fixed record |
| dict | Labeled fields / fast key lookup |
| set | Uniqueness / set math / fast “is it there?” |

## Exercises

1. Build a dict for a book: title, author, year, tags (list).
2. Safely print a missing key with `.get`.
3. From `[1,1,2,3,3,3,4]` produce sorted unique numbers.
4. Find common skills between two people using set intersection.

## Next

Run `dicts_sets_demo.py`, then **Module 08**.
