#!/usr/bin/env python3
''' task number 1 wait_n coroutine'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Launches multiple instances using the specified max_delay, and collects their outputs. """
    delay = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
        )
    return sorted(delay)
