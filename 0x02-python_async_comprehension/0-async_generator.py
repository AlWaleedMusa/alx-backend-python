#!/usr/bin/env python3

"""A basic asyncio code"""

import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """
    An asynchronous generator that yields a random float between 0 and 10.

    This function waits for 1 second, then generates a random float between 0 and 10.
    It repeats this process 10 times, yielding a new random float each time.

    Yields:
        float: A random float between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
