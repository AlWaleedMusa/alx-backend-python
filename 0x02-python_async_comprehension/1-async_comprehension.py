#!/usr/bin/env python3

"""A basic asyncio code"""

from typing import List


async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an asynchronous generator.

    This function uses an asynchronous list comprehension
    to collect 10 random float numbers generated by the
    `async_generator` function.

    Returns:
        List[float]: A list of 10 random float numbers.
    """
    result = [i async for i in async_generator()]
    return result
