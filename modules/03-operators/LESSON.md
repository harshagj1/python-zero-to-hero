# Module 03 — Operators

## Layman idea

**Operators** are symbols that do work: math, compare, combine true/false.

## Arithmetic operators

| Symbol | Meaning | Example |
|--------|---------|---------|
| `+` | Add | `3 + 2` → `5` |
| `-` | Subtract | `3 - 2` → `1` |
| `*` | Multiply | `3 * 2` → `6` |
| `/` | Divide (always float) | `5 / 2` → `2.5` |
| `//` | Floor divide | `5 // 2` → `2` |
| `%` | Remainder (modulo) | `5 % 2` → `1` |
| `**` | Power | `2 ** 3` → `8` |

### Why `%` matters in real life

- Even/odd: `n % 2 == 0` means even
- Wrap-around (clocks, circular lists)
- Chunking data into groups

## Comparison operators (result is always bool)

| Symbol | Meaning |
|--------|---------|
| `==` | Equal to |
| `!=` | Not equal |
| `<` `>` | Less / greater |
| `<=` `>=` | Less-or-equal / greater-or-equal |

```python
age = 18
print(age >= 18)  # True
```

**Trap:** `=` assigns. `==` compares. Mixing them is a classic beginner bug.

## Logical operators

| Operator | Meaning (plain English) |
|----------|-------------------------|
| `and` | Both must be True |
| `or` | At least one True |
| `not` | Flip True↔False |

```python
has_ticket = True
has_id = False
can_enter = has_ticket and has_id  # False
```

### Short-circuit (pro detail)

Python stops early when the answer is already known:

```python
False and something_expensive()  # something_expensive never runs
True or something_expensive()    # same idea
```

## Operator precedence (order of operations)

Roughly like school math: `**` before `* /` before `+ -`. Comparisons after. Logic last-ish.

When unsure: **use parentheses**. Pros do this for clarity, not only correctness.

```python
(2 + 3) * 4   # 20
2 + 3 * 4     # 14
```

## Identity vs equality (early pro tip)

```python
a = [1, 2]
b = [1, 2]
print(a == b)   # True  — same contents
print(a is b)   # False — different boxes in memory
```

Use `==` for values. Use `is` mainly for `None`:

```python
if nickname is None:
    print("No nickname")
```

## Exercises

1. Check if a number is even.
2. Check if a person can vote: age >= 18 **and** is citizen.
3. Compute compound interest formula: `A = P * (1 + r) ** t` with sample numbers.
4. Predict `True and False or True` then verify.

## Next

Run `operators_demo.py`, then **Module 04**.
