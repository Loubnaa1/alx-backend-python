#!/usr/bin/env python3
""" contains sum_mixed_list function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns sum of mixed list as a float."""
    return sum(mxd_lst)
