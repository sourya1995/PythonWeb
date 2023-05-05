import math

_SIN_MEMOIZED_VALUES = {}

def memoized_sin(x):
    if x not in _SIN_MEMOIZED_VALUES:
        _SIN_MEMOIZED_VALUES[x] = math.sin(x)
    return _SIN_MEMOIZED_VALUES[x]