# Module 16 — Typing
# Run: python typing_demo.py

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, TypedDict


@dataclass
class User:
    name: str
    age: int


class UserPayload(TypedDict):
    name: str
    age: int
    active: bool


def average(nums: list[float]) -> float:
    return sum(nums) / len(nums) if nums else 0.0


def find_user(users: list[User], name: str) -> User | None:
    for user in users:
        if user.name == name:
            return user
    return None


def apply(x: int, fn: Callable[[int], int]) -> int:
    return fn(x)


def main() -> None:
    print(average([1.5, 2.5, 3.0]))
    users = [User("Ada", 36), User("Alan", 41)]
    print(find_user(users, "Ada"))
    print(find_user(users, "Noone"))
    print(apply(5, lambda n: n * n))

    payload: UserPayload = {"name": "Grace", "age": 85, "active": True}
    print(payload)


if __name__ == "__main__":
    main()
