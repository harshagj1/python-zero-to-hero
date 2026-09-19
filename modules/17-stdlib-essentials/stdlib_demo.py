# Module 17 — Stdlib Essentials
# Run: python stdlib_demo.py
#
# SCHOOL: Python ships with useful built-in toolboxes (stdlib). Learn them before pip-installing everything.
# WORK: SRE/Obs/AI automation leans heavily on pathlib, datetime, json, logging, re, collections.

import json
import logging
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

# SCHOOL: logging > random prints for real programs.
# WORK: observability starts with structured logs; SRE debugs from logs during incidents.
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def main() -> None:
    now = datetime.now(timezone.utc)
    # SCHOOL: timestamps in UTC avoid timezone confusion.
    # WORK: always store event time in UTC for metrics/logs/traces.
    logging.info("UTC now: %s", now.isoformat())

    out = Path(__file__).parent / "out"
    out.mkdir(exist_ok=True)
    target = out / "note.txt"
    # SCHOOL: pathlib builds file paths safely on Windows/Mac/Linux.
    # WORK: portable automation scripts across operator laptops and servers.
    target.write_text(f"written at {now.isoformat()}\n", encoding="utf-8")
    logging.info("Wrote %s", target)

    words = "to be or not to be".split()
    # SCHOOL: Counter counts how often each thing appears.
    # WORK: top error codes; top slow endpoints; token frequency in AI evals.
    print("Counter:", Counter(words))

    groups: defaultdict[str, list[str]] = defaultdict(list)
    for name in ["Ada", "Alan", "Grace", "Guido"]:
        groups[name[0]].append(name)
    # SCHOOL: defaultdict creates missing drawers automatically.
    # WORK: group logs by service; group spans by route; group docs by label.
    print("grouped:", dict(groups))

    text = "Order 12 costs 99 dollars"
    # SCHOOL: regex finds patterns (here: digits).
    # WORK: extract status codes / IPs / request ids from messy logs (Obs/SRE).
    print("numbers:", re.findall(r"\d+", text))

    payload = {"course": "zero-to-hero", "module": 17}
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
