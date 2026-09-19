# Code under test + pytest examples
# Install: pip install pytest
# Run from this folder: pytest -q

def average(nums: list[float]) -> float:
    if not nums:
        raise ValueError("nums must not be empty")
    return sum(nums) / len(nums)


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def test_average_normal():
    assert average([2, 4, 6]) == 4


def test_average_empty_raises():
    import pytest

    with pytest.raises(ValueError):
        average([])


def test_clamp():
    assert clamp(150, 0, 100) == 100
    assert clamp(-5, 0, 100) == 0
    assert clamp(40, 0, 100) == 40
