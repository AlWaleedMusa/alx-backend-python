#!/usr/bin/env python3

"""
A module to measure the runtime of asynchronous comprehensions.
"""

from asyncio import gather
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing for
    asynchronous comprehensions concurrently.

    This function creates four tasks of the
    `async_comprehension` function and runs
    them concurrently using `asyncio.gather`.
    It measures the time taken to complete all
    four tasks and returns the duration.

    Returns:
        float: The total time taken to execute
        the four asynchronous comprehensions.
    """
    starting_time = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    await gather(*tasks)
    ending_time = time.time()

    return ending_time - starting_time
