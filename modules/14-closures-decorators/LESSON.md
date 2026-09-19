# Module 14 — Closures and Decorators

## Layman idea

Functions are values in Python — you can pass them around like numbers.

A **closure** is a function that remembers variables from the place it was born.

A **decorator** is a wrapper that adds behavior around a function (logging, timing, auth checks) without rewriting the function.

## Closures

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor  # remembers factor
    return multiply

double = make_multiplier(2)
print(double(10))  # 20
```

## Decorators — the pattern

```python
import functools
import time

def timed(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

@timed
def slow_add(a, b):
    time.sleep(0.1)
    return a + b
```

`@timed` means: `slow_add = timed(slow_add)`.

Always use `functools.wraps` so the wrapped function keeps its real name/docs.

## Decorators with arguments

```python
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def hi():
    print("hi")
```

## Where you'll see this at work

- Flask/FastAPI route decorators
- Retry logic
- Caching (`functools.lru_cache`)
- Permission checks
- Metrics / logging

## Exercises

1. Write `@shout` that uppercases a returned string.
2. Write `@once` that only allows the first call to run.
3. Use `functools.lru_cache` on a recursive Fibonacci and feel the speed.
4. Explain closures in one plain sentence.

## Next

Run `decorators_demo.py`, then **Module 15**.
