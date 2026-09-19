"""Small helper functions for the module demo."""


def shout(text: str) -> str:
    return text.upper() + "!"


def average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0
