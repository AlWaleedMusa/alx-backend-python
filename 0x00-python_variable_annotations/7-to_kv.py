#!/usr/bin/env python3
'''
    Basic annotation
'''

# Write a type-annotated function to_kv that takes a string k and an int OR float v as arguments and returns a tuple. The first element of the tuple is the string k. The second element is the square of the int/float v and should be annotated as a float.

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
