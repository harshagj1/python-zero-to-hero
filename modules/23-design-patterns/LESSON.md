# Module 23 — Design Patterns (practical Python)

## Layman idea

**Design patterns** are named solutions to common design problems — like standard chess openings. Learn them to communicate with other engineers and avoid reinventing shaky structures.

Don't force patterns. Use them when the pain appears.

## Patterns you'll actually use

### 1) Strategy — swap algorithms
```python
class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy
    def sort(self, data):
        return self.strategy(data)

Sorter(sorted).sort([3,1,2])
Sorter(lambda xs: sorted(xs, reverse=True)).sort([3,1,2])
```

In Python, functions often replace heavy strategy class hierarchies.

### 2) Factory — central place to create objects
```python
def make_notifier(kind: str):
    if kind == "email":
        return EmailNotifier()
    if kind == "sms":
        return SmsNotifier()
    raise ValueError(kind)
```

### 3) Adapter — make mismatched APIs work together
Wrap an old interface so new code can use it cleanly.

### 4) Observer / pub-sub — react to events
Logging handlers, UI events, message buses.

### 5) Singleton (use sparingly)
One shared instance (config, db pool). In Python, module-level objects are often enough.

### 6) Dependency Injection — pass collaborators in
```python
class OrderService:
    def __init__(self, payments, emailer):
        self.payments = payments
        self.emailer = emailer
```

This makes testing easy (pass fakes).

## Pythonic principle over pattern worship

- Duck typing + protocols beat deep inheritance trees
- Composition over inheritance
- Small functions and clear modules beat ceremony

## Exercises

1. Implement strategy for tax calculation (US vs IN rates as functions).
2. Factory that returns different storage backends (`MemoryStorage`, `JsonStorage`).
3. Refactor a class to inject its dependency instead of hardcoding.
4. Find a pattern already used in your Checkpoint B code (hint: repository-ish tracker).

## Next

Run `patterns_demo.py`, then **Module 24**.
