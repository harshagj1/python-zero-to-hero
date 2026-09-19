"""Math helpers living inside a package."""


def clamp(value, low, high):
    """Keep value between low and high."""
    return max(low, min(high, value))
