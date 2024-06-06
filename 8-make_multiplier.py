#!/usr/bin/env python3
""" contains make_multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns a function that multiplies a float by multiplier"""
    return lambda var: var * multiplier
