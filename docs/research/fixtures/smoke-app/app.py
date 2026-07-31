"""Tiny fixture module — intentional bug for validation smokes."""


def add(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b + 1  # BUG: off-by-one; correct is a + b
