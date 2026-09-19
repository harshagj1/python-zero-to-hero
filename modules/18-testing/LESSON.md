# Module 18 — Testing with pytest

## Layman idea

If you change code and nothing breaks the alarm, you're flying blind.

**Tests** are tiny programs that check your real programs still behave.

Professionals don't test because they love bureaucracy — they test so they can change code fearlessly.

## Assert basics

```python
def add(a, b):
    return a + b

assert add(2, 3) == 5
```

`assert` crashes the test if the condition is false.

## pytest workflow

1. Install: `pip install pytest`
2. Name files `test_*.py` or `*_test.py`
3. Name functions `test_*`
4. Run: `pytest -q`

```python
# test_mathy.py
from mathy import add

def test_add_positive():
    assert add(2, 3) == 5

def test_add_zero():
    assert add(0, 5) == 5
```

## Arrange / Act / Assert pattern

```python
def test_withdraw():
    # Arrange
    account = BankAccount("Ada", 100)
    # Act
    account.withdraw(40)
    # Assert
    assert account.balance == 60
```

## Testing exceptions

```python
import pytest

def test_withdraw_too_much():
    account = BankAccount("Ada", 10)
    with pytest.raises(ValueError):
        account.withdraw(50)
```

## Fixtures (shared setup)

```python
import pytest

@pytest.fixture
def account():
    return BankAccount("Ada", 100)

def test_deposit(account):
    account.deposit(5)
    assert account.balance == 105
```

## What to test (pro judgment)

- Core business rules
- Edge cases (empty, zero, None, big numbers)
- Bug regressions (once fixed, add a test so it never returns)

Don't obsess over testing every trivial getter.

## Checkpoint C

Add tests for Checkpoint B's `Expense` validation and `total()`.

## Exercises

1. Write tests for `average`.
2. Write a test that expects `ValueError`.
3. Run pytest and fix a failing test on purpose, then correct it.
4. Add a fixture.

## Next

Look at `test_examples.py`, then **Module 19**.
