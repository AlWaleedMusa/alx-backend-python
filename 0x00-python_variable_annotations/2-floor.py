#!/usr/bin/env python3
'''
    Basic annotations between float and int.
'''


def floor(n: float) -> int:
    """
    returns the floor of the float.

    Args:
        n (float): The number to floor.

    Returns:
        int: The result of flooring n.
    """

    return float.__floor__(n)
