#!/usr/bin/env python3
"""Measure the runtime"""

import time
import asyncio

wait_n = __import__("1-concurrent_coroutines").wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average runtime of the wait_n function.

    Args:
        n (int): The number of coroutines to run.
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        float: The average runtime per coroutine.
    """
    starting_time = time.time()

    asyncio.run(wait_n(n, max_delay))

    return (time.time() - starting_time) / n
