#!/usr/bin/env python3
"""
    Basic annotation 
"""
from typing import List
# Write a type-annotated function sum_mixed_list which takes a list mxd_lst of integers and floats and returns their sum as a float.

def sum_mixed_list(mxd_lst: List[int, float]) -> float:
    """
    returns the sum of elm in a list as a float.

    Args:
        input_list (list): a list of elem [ints, floats].

    Returns:
        float: sum of elem in the list.
    """
    return sum(mxd_lst)
