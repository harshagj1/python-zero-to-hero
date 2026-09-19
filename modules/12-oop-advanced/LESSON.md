# Module 12 — OOP Advanced

## Inheritance — “is a”

```python
class Animal:
    def speak(self):
        return "..."

class Cat(Animal):
    def speak(self):
        return "meow"
```

`Cat` inherits from `Animal` and can override methods.

### `super()`

Call the parent version while extending it:

```python
class Employee:
    def __init__(self, name):
        self.name = name

class Manager(Employee):
    def __init__(self, name, team_size):
        super().__init__(name)
        self.team_size = team_size
```

## Composition vs inheritance (pro judgment)

Prefer **composition** (“has a”) when you're combining behaviors:

```python
class Engine:
    def start(self): ...

class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS an Engine
```

Inheritance is best for true “is-a” relationships. Overusing inheritance creates fragile hierarchies.

## Magic methods (dunder methods)

Special names Python calls for you:

| Method | Enables |
|--------|---------|
| `__str__` | `print(obj)` friendly text |
| `__repr__` | unambiguous debug text |
| `__eq__` | `obj == other` |
| `__len__` | `len(obj)` |
| `__getitem__` | `obj[i]` |

```python
class Playlist:
    def __init__(self, songs):
        self._songs = list(songs)

    def __len__(self):
        return len(self._songs)

    def __getitem__(self, index):
        return self._songs[index]
```

## Dataclasses (modern Python)

Less boilerplate for data-holding classes:

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
```

Auto-generates `__init__`, `__repr__`, `__eq__`, etc.

## Abstract base classes (interface idea)

```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def charge(self, amount: float) -> None: ...
```

Subclasses must implement `charge`. Useful in large systems.

## Exercises

1. `Vehicle` → `Car` / `Bike` with different `move()` messages.
2. Make `Point` a dataclass; add method `distance_from_origin()`.
3. Implement `__str__` and `__eq__` for a `Money(amount, currency)` class.
4. Prefer composition: `Library` has a list of `Book` objects.

## Next

Run `oop_advanced_demo.py`, build Checkpoint B, then **Module 13**.
