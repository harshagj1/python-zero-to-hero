# Module 12 — OOP Advanced
# Run: python oop_advanced_demo.py

from abc import ABC, abstractmethod
from dataclasses import dataclass
import math


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."


class Cat(Animal):
    def speak(self):
        return f"{self.name}: meow"


class Dog(Animal):
    def speak(self):
        return f"{self.name}: woof"


@dataclass
class Point:
    x: float
    y: float

    def distance_from_origin(self) -> float:
        return math.hypot(self.x, self.y)


class Money:
    def __init__(self, amount, currency="USD"):
        self.amount = float(amount)
        self.currency = currency

    def __str__(self):
        return f"{self.currency} {self.amount:.2f}"

    def __eq__(self, other):
        return (
            isinstance(other, Money)
            and self.amount == other.amount
            and self.currency == other.currency
        )


class Notifier(ABC):
    @abstractmethod
    def send(self, message: str) -> None: ...


class PrintNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"[notify] {message}")


def main():
    animals = [Cat("Misha"), Dog("Rex")]
    for a in animals:
        print(a.speak())

    p = Point(3, 4)
    print(p, "distance:", p.distance_from_origin())

    print(Money(10, "INR"))
    print("equal?", Money(5) == Money(5))

    PrintNotifier().send("Payment received")


if __name__ == "__main__":
    main()
