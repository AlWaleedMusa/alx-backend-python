#!/usr/bin/env python3
'''
    Basic annotations in a list.
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    returns the sum of elm in a list as a float.

    Args:
        input_list (list): a list of elem.

    Returns:
        float: sum of elem in the list.
    """

    return sum(input_list)
