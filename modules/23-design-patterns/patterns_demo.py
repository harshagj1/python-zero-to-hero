# Module 23 — Design Patterns demo
# Run: python patterns_demo.py

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass


# Strategy via plain functions
def tax_us(amount: float) -> float:
    return amount * 0.08


def tax_in(amount: float) -> float:
    return amount * 0.18


@dataclass
class Cart:
    amount: float
    tax_fn: Callable[[float], float]

    def total(self) -> float:
        return self.amount + self.tax_fn(self.amount)


# Simple repository / storage strategy
class MemoryStorage:
    def __init__(self) -> None:
        self._items: list[str] = []

    def add(self, item: str) -> None:
        self._items.append(item)

    def all(self) -> list[str]:
        return list(self._items)


@dataclass
class TodoService:
    storage: MemoryStorage

    def add(self, item: str) -> None:
        self.storage.add(item)

    def list(self) -> list[str]:
        return self.storage.all()


# Factory
def make_tax(country: str):
    table = {"US": tax_us, "IN": tax_in}
    try:
        return table[country]
    except KeyError as exc:
        raise ValueError(f"unknown country {country}") from exc


def main() -> None:
    print("US total:", Cart(100, make_tax("US")).total())
    print("IN total:", Cart(100, make_tax("IN")).total())

    service = TodoService(MemoryStorage())
    service.add("learn patterns")
    service.add("write tests")
    print("todos:", service.list())


if __name__ == "__main__":
    main()
