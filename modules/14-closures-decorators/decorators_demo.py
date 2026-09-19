# Module 14 — Closures & Decorators
# Run: python decorators_demo.py

import functools
import time


def make_multiplier(factor):
    def multiply(x):
        return x * factor

    return multiply


def timed(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter() - start:.4f}s")
        return result

    return wrapper


def shout(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return str(func(*args, **kwargs)).upper()

    return wrapper


@timed
@shout
def greet(name):
    time.sleep(0.05)
    return f"hello {name}"


@functools.lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def main():
    double = make_multiplier(2)
    print("double 7:", double(7))
    print(greet("ada"))
    print("fib(30):", fib(30))


if __name__ == "__main__":
    main()
