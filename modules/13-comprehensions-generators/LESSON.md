# Module 13 — Comprehensions and Generators

## Layman idea

Pros hate noisy loops for simple transforms. Python gives shortcuts.

**Comprehension** = build a new list/dict/set in one clear expression.  
**Generator** = produce values lazily (one at a time) to save memory.

## List comprehensions

```python
# Long way
squares = []
for n in range(5):
    squares.append(n * n)

# Pro way
squares = [n * n for n in range(5)]
```

With filter:

```python
evens = [n for n in range(10) if n % 2 == 0]
```

## Dict / set comprehensions

```python
names = ["ada", "alan"]
lengths = {name: len(name) for name in names}
unique_lens = {len(name) for name in names}
```

## When NOT to use them

If the logic is complex (many branches), a normal loop is clearer. Readability > cleverness.

## Generators and `yield`

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for x in countdown(3):
    print(x)
```

`yield` pauses the function and sends a value. Next iteration resumes.

Generator expression:

```python
sum_of_squares = sum(n * n for n in range(1_000_000))
```

Notice: no giant list stored — values stream through.

## Why engineers care

- Process huge files line by line
- Pipelines of transformations
- Lower memory usage
- Cleaner APIs (`for item in reader():`)

## Exercises

1. Squares of 1..20 via list comprehension.
2. Dict mapping numbers 1..5 to cubics.
3. Write generator `infinite_count(start=0)` and print first 5 values (use `break`).
4. Sum of even numbers 1..1000 with a generator expression.

## Next

Run `comprehensions_generators_demo.py`, then **Module 14**.
