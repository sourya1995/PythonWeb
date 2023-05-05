import functools
import math

@functools.lru_cache(maxsize=2)
def memoized_sin(x):
    return math.sin(x)