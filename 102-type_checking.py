#!/usr/bin/env python3
"""contains zoom_array function """

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ returns a list """
    zoomed_in: List = [
        item for item in lst
        for j in range(factor)
    ]
    return zoomed_in


array: Tuple = (12, 72, 91)

zoom_2x: List = zoom_array(array)

zoom_3x: List = zoom_array(array, 3)
