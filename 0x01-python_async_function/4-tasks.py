#!/usr/bin/env python3

"""back to basics"""

import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes `n` tasks concurrently, each task waiting for a random delay up to `max_delay` seconds.

    Args:
        n (int): The number of tasks to execute.
        max_delay (int): The maximum delay for each task in seconds.

    Returns:
        List[float]: A list of delays in seconds for each completed task.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
