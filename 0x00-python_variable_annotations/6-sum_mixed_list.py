#!/usr/bin/env python3
'''
    Basic annotation 
'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    returns the sum of elm in a list as a float.

    Args:
        input_list (list): a list of elem [ints, floats].

    Returns:
        float: sum of elem in the list.
    """

    return float(sum(mxd_lst))
