# Module 15 — Iterators and Protocols

## Layman idea

A `for` loop doesn't magically know your object. It asks for an **iterator**.

Python is built on **protocols**: “If your object has these methods, it can play this role.”

## Iterable vs iterator

- **Iterable**: can provide an iterator (`list`, `str`, files, your classes with `__iter__`)
- **Iterator**: produces next values via `__next__`, raises `StopIteration` when done

```python
nums = [10, 20, 30]
it = iter(nums)
print(next(it))  # 10
print(next(it))  # 20
```

## Make your own iterable

```python
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1
```

Using `yield` inside `__iter__` is a clean way to build iterators.

## Other useful protocols

| Want this… | Implement… |
|------------|------------|
| `len(obj)` | `__len__` |
| `obj[i]` | `__getitem__` |
| `with obj:` | `__enter__` / `__exit__` |
| `obj + other` | `__add__` |
| compare | `__eq__`, `__lt__`, … |

## Context managers (the `with` protocol)

```python
class TempMessage:
    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, exc_type, exc, tb):
        print("exit")
        return False  # don't swallow exceptions

with TempMessage():
    print("inside")
```

Or use `contextlib.contextmanager` for a generator-style version.

## Why this matters for “10 YOE” level

Frameworks and libraries are full of protocols. Understanding them lets you:

- Write clean APIs
- Plug into `for`, `with`, unpacking, sorting
- Read Python source / library code without fear

## Exercises

1. Build `RangeLite(start, stop)` iterable without using `range`.
2. Build a context manager that prints how long a block took.
3. Use `iter(callable, sentinel)` pattern with `input` until empty string (careful in demos).
4. Explain iterable vs iterator in plain English.

## Next

Run `iterators_protocols_demo.py`, then **Module 16**.
