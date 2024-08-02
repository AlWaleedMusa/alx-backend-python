#!/usr/bin/env python3
'''
    Let's duck type an iterable object
'''
from typing import List, Sequence, Iterable, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return the length"""
    return [(i, len(i)) for i in lst]
