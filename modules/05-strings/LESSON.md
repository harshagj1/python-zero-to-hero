# Module 05 — Strings (text)

## Layman idea

A **string** is text. Almost everything users type is a string: names, emails, messages, file contents.

In Python, strings are **immutable**: you don't change a string in place — you create a new one.

```python
name = "ada"
name = name.upper()  # new string "ADA"; old "ada" is discarded
```

## Creating strings

```python
a = "double quotes"
b = 'single quotes'
c = """multi-line
string"""
```

## Indexing and slicing (like cutting bread)

```python
word = "Python"
# index:  012345
print(word[0])     # P
print(word[-1])    # n (last character)
print(word[0:3])   # Pyt  (start inclusive, end exclusive)
print(word[:2])    # Py
print(word[2:])    # thon
print(word[::-1])  # nohtyP (reverse)
```

## Useful methods (memorize these)

| Method | What it does |
|--------|----------------|
| `.lower()` / `.upper()` / `.title()` | Change case |
| `.strip()` | Remove edge spaces |
| `.replace(old, new)` | Swap text |
| `.split(sep)` | Break into a list |
| `.join(list)` | Glue a list into one string |
| `.startswith(...)` / `.endswith(...)` | Check edges |
| `.find(...)` | Position or -1 |
| `.isdigit()` / `.isalpha()` | Character checks |

```python
csv = "a,b,c"
parts = csv.split(",")       # ["a", "b", "c"]
again = "-".join(parts)      # "a-b-c"
```

## f-strings (the pro way to format)

```python
name = "Ada"
age = 36
print(f"{name} is {age}")
print(f"{name=} {age=}")          # debug style
print(f"Price: ${9.5:.2f}")       # 9.50
```

Older styles exist (`%`, `.format()`). Prefer **f-strings** in modern code.

## Escape characters

```python
print("She said \"hello\"")
print("Line1\nLine2")   # newline
print("Col1\tCol2")     # tab
print(r"C:\new\folder") # raw string — backslashes literal
```

## Exercises

1. Take `"  python ZERO to hero  "`, strip, title-case it.
2. Count how many times `"a"` appears in a sentence (hint: `.count`).
3. Split an email `"user@example.com"` into username and domain.
4. Build a receipt line with f-string: item name + price with 2 decimals.

## Next

Run `strings_demo.py`, then **Module 06**.
