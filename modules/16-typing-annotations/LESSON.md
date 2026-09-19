# Module 16 — Typing and Annotations

## Layman idea

Python still runs dynamically, but **type hints** tell humans and tools what you *intend*.

They're like labels on jars: optional for the interpreter, invaluable for teams, IDEs, and catching bugs early with checkers (`mypy`, `pyright`).

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

## Common annotations

```python
from typing import Optional, Any
# Python 3.10+: use | instead of Optional/Union

age: int = 30
tags: list[str] = ["ai", "python"]
mapping: dict[str, int] = {"a": 1}
maybe_email: str | None = None
```

## Functions and classes

```python
def add(a: int, b: int) -> int:
    return a + b

class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
```

## Useful typing tools

| Tool | Use |
|------|-----|
| `list[str]` | list of strings |
| `dict[str, float]` | mapping |
| `tuple[int, str]` | fixed-shape tuple |
| `Callable[[int], str]` | function types |
| `TypeVar` | generics |
| `Protocol` | structural typing (“has these methods”) |
| `TypedDict` | dict with known keys |

```python
from typing import Callable

def apply(x: int, fn: Callable[[int], int]) -> int:
    return fn(x)
```

## Dataclasses + hints = industry default

```python
from dataclasses import dataclass

@dataclass
class Order:
    id: int
    total: float
    paid: bool = False
```

## What type hints are NOT

- They do **not** enforce types at runtime by themselves
- Bad hints can lie — keep them honest
- Don't annotate every tiny local variable; annotate public APIs

## Exercises

1. Annotate `average(nums: list[float]) -> float`.
2. Write `find_user(users: list[User], name: str) -> User | None`.
3. Create a `TypedDict` for a JSON user payload.
4. Run a type checker later when you set up tooling (Module 20).

## Next

Run `typing_demo.py`, then **Module 17**.
