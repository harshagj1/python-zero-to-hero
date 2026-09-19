# Checkpoint B — Expense Tracker (tiny enterprise-style app)
# Run: python projects/checkpoint_b_expense_tracker.py
#
# SCHOOL: Save spending records to a JSON file using a class.
# WORK: Same architecture as many internal tools:
#       Model (Expense) + Service (ExpenseTracker) + persistence (JSON/DB) + menu/API.
#       Swap "expenses" for "incidents", "silences", or "datasets" and you're in
#       SRE / observability / AI-ops tooling territory.
# FASTAPI LINK: tracker.add/list ≈ POST/GET endpoints; JSON file ≈ DB table for now.

from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from pathlib import Path


# SCHOOL: path next to this script so data is easy to find.
# WORK: real apps use env vars / config for data directories.
DATA_FILE = Path(__file__).parent / "expenses.json"


@dataclass
class Expense:
    """SCHOOL: one spending record with three fields.
    WORK: like a Pydantic model or DB row in a FastAPI service.
    """

    description: str
    amount: float
    category: str

    def __post_init__(self):
        # SCHOOL: reject bad data as soon as the object is born.
        # WORK: same as request validation — fail fast at the boundary (enterprise rule).
        if self.amount <= 0:
            raise ValueError("amount must be positive")
        if not self.description.strip():
            raise ValueError("description required")


class ExpenseTracker:
    """SCHOOL: the manager that loads, saves, and totals expenses.
    WORK: service/repository layer — FastAPI depends on this, not on raw files.
    """

    def __init__(self, path: Path = DATA_FILE):
        self.path = path
        self.expenses: list[Expense] = []
        self.load()  # WHY: restore state on startup (like a service rehydrate)

    def load(self) -> None:
        # SCHOOL: if no file yet, start empty; else read JSON into Expense objects.
        # WORK: bootstrapping config/state — observability agents do similar on start.
        if not self.path.exists():
            self.expenses = []
            return
        raw = json.loads(self.path.read_text(encoding="utf-8"))
        self.expenses = [Expense(**item) for item in raw]

    def save(self) -> None:
        # SCHOOL: turn objects into plain dicts, write pretty JSON.
        # WORK: persistence; later replace with SQLite/Postgres (Module 22).
        payload = [asdict(e) for e in self.expenses]
        self.path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def add(self, description: str, amount: float, category: str) -> None:
        self.expenses.append(Expense(description, amount, category))
        self.save()  # WHY save immediately: don't lose data if the process dies

    def total(self) -> float:
        # SCHOOL: add all amounts.
        # WORK: aggregate queries — sum(errors), sum(tokens), sum(cost).
        return sum(e.amount for e in self.expenses)

    def by_category(self) -> dict[str, float]:
        # SCHOOL: group totals by category label.
        # WORK: group-by for dashboards (errors by endpoint, cost by model).
        summary: dict[str, float] = {}
        for e in self.expenses:
            summary[e.category] = summary.get(e.category, 0.0) + e.amount
        return summary


def menu() -> None:
    # SCHOOL: interactive loop for humans.
    # WORK: replace this menu with FastAPI routes for a real service.
    tracker = ExpenseTracker()
    while True:
        print("\n=== EXPENSES ===")
        print("1) Add")
        print("2) List")
        print("3) Totals by category")
        print("4) Quit")
        choice = input("Choose: ").strip()

        if choice == "1":
            try:
                desc = input("Description: ")
                amount = float(input("Amount: "))
                category = input("Category: ").strip() or "general"
                tracker.add(desc, amount, category)
                print("Saved.")
            except ValueError as err:
                # SCHOOL: show the error instead of crashing.
                # WORK: map to HTTP 400 with a clear message in REST APIs.
                print("Error:", err)
        elif choice == "2":
            if not tracker.expenses:
                print("(empty)")
            for e in tracker.expenses:
                print(f"- {e.description}: {e.amount:.2f} [{e.category}]")
            print(f"Grand total: {tracker.total():.2f}")
        elif choice == "3":
            for cat, total in tracker.by_category().items():
                print(f"{cat}: {total:.2f}")
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Unknown option.")


if __name__ == "__main__":
    menu()
