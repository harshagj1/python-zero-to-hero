# Module 06 — Lists and Tuples

## Layman idea

A **list** is a shopping list: ordered, changeable, can hold many items.

A **tuple** is like a sealed packing list: ordered, but you usually **don't change** it after creation.

```python
fruits = ["apple", "banana", "cherry"]  # list
point = (10, 20)                        # tuple
```

## Lists — everyday workhorse

### Create / read / update

```python
nums = [10, 20, 30]
print(nums[0])      # 10
nums[0] = 99        # change
nums.append(40)     # add at end
nums.insert(1, 15)  # insert at index
last = nums.pop()   # remove and return last
nums.remove(20)     # remove first matching value
```

### Common operations

```python
len(nums)
nums.sort()              # in-place
sorted(nums)             # new sorted list
nums.reverse()
20 in nums               # membership → True/False
```

### Nested lists

```python
matrix = [
    [1, 2],
    [3, 4],
]
print(matrix[1][0])  # 3
```

### Copy carefully (classic bug)

```python
a = [1, 2, 3]
b = a          # NOT a copy — same list!
b.append(4)    # a also changes

c = a.copy()   # real shallow copy
# or c = a[:]
```

## Tuples — fixed records

```python
rgb = (255, 128, 0)
name, age = ("Ada", 36)  # unpacking
```

Why tuples?

- Safer when data shouldn't change
- Can be dictionary keys (lists cannot)
- Slightly more memory-efficient
- Multiple return values from functions often come as tuples

```python
def min_max(values):
    return min(values), max(values)

lo, hi = min_max([3, 1, 7])
```

## List vs tuple — choose like a pro

| Need | Choose |
|------|--------|
| Growing / shrinking / editing | `list` |
| Fixed record (x, y) or row | `tuple` |
| “Don't touch this” signal | `tuple` |

## Exercises

1. Start with `[5, 2, 9, 1]`, append `7`, sort ascending, print.
2. Remove the middle item from a 5-item list using `pop(index)`.
3. Unpack `("India", "New Delhi")` into `country, capital`.
4. Explain in comments why `b = a` is dangerous for lists.

## Next

Run `lists_tuples_demo.py`, then **Module 07**.
