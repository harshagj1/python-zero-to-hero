# Module 24 — Performance & debugging demo
# Run: python perf_debug_demo.py

from __future__ import annotations

import logging
import time

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def membership_speed(n: int = 40_000) -> None:
    data_list = list(range(n))
    data_set = set(data_list)
    target = n - 1

    start = time.perf_counter()
    _ = target in data_list
    list_time = time.perf_counter() - start

    start = time.perf_counter()
    _ = target in data_set
    set_time = time.perf_counter() - start

    logging.info("list membership: %.6fs", list_time)
    logging.info("set membership:  %.6fs", set_time)


def slow_sum(n: int = 5_000) -> int:
    """Intentionally awkward stringy loop for demo profiling."""
    total = 0
    for i in range(n):
        total += int(str(i))
    return total


def main() -> None:
    membership_speed()
    start = time.perf_counter()
    result = slow_sum()
    logging.info("slow_sum=%s in %.4fs", result, time.perf_counter() - start)
    logging.info("Tip: python -m cProfile -s cumtime perf_debug_demo.py")


if __name__ == "__main__":
    main()
