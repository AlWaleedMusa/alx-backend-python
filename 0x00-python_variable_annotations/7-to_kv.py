#!/usr/bin/env python3
'''
    Basic annotation
'''

from typing import List, Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """
    return a tuple.

    Args:
        k (string): a string.
        v (int | float): int or a float
    Returns:
        a tuple (string, square(v)).
    """

    return (k, v**2)
