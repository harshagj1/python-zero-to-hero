# Module 13 — Comprehensions & Generators
# Run: python comprehensions_generators_demo.py

squares = [n * n for n in range(1, 11)]
print("squares:", squares)

evens = [n for n in range(20) if n % 2 == 0]
print("evens:", evens)

word_lengths = {w: len(w) for w in ["python", "ai", "data"]}
print("lengths:", word_lengths)


def countdown(n):
    while n > 0:
        yield n
        n -= 1


print("countdown:", list(countdown(5)))

# Memory-friendly sum
total = sum(n * n for n in range(1, 1001))
print("sum of squares 1..1000:", total)


def read_fake_lines():
    """Pretend we're streaming a big file."""
    for i in range(1, 4):
        yield f"log-line-{i}"


for line in read_fake_lines():
    print("got:", line)
