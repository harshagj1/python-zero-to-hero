# Module 15 — Iterators & Protocols
# Run: python iterators_protocols_demo.py

import time
from contextlib import contextmanager


class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1


class Team:
    def __init__(self, members):
        self._members = list(members)

    def __len__(self):
        return len(self._members)

    def __getitem__(self, index):
        return self._members[index]


@contextmanager
def timed_block(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        print(f"{label}: {time.perf_counter() - start:.4f}s")


def main():
    print(list(CountDown(3)))

    team = Team(["Ada", "Alan", "Grace"])
    print("len:", len(team))
    print("first:", team[0])
    for person in team:  # works via __getitem__ fallback protocol
        print("-", person)

    with timed_block("sleep"):
        time.sleep(0.05)


if __name__ == "__main__":
    main()
