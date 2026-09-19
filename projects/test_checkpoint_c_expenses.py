# Checkpoint C — tests for ExpenseTracker pieces
# Run from python-zero-to-hero:
#   pip install pytest
#   pytest -q projects/test_checkpoint_c_expenses.py

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "projects"))

from checkpoint_b_expense_tracker import Expense, ExpenseTracker  # noqa: E402


def test_expense_rejects_negative():
    with pytest.raises(ValueError):
        Expense("food", -1, "food")


def test_total(tmp_path):
    tracker = ExpenseTracker(path=tmp_path / "e.json")
    tracker.add("tea", 10, "food")
    tracker.add("bus", 20, "travel")
    assert tracker.total() == 30
    assert tracker.by_category()["food"] == 10
