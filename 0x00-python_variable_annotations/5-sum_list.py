#!/usr/bin/env python3
'''
    Basic annotations in a list.
'''


def sum_list(input_list: list) -> float:
    """
    returns the sum of elm in a list as a float.

    Args:
        input_list (list): a list of elem.

    Returns:
        float: sum of elem in the list.
    """

    sum = 0
    for num in input_list:
        sum += num

    return sum
