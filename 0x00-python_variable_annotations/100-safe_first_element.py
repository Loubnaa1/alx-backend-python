#!/usr/bin/env python3
"""contains safe_first_element function"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''extracts the first element of a sequence '''
    if lst:
        return lst[0]
    else:
        return None
