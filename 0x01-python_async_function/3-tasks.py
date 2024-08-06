#!/usr/bin/env python3
"""Tasks"""

from asyncio import Task, create_task

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Create an asyncio Task for the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay for the wait_random coroutine.

    Returns:
        Task: An asyncio Task object for the wait_random coroutine.
    """
    return create_task(wait_random(max_delay))
