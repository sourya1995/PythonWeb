import cachetools.func
import math
import time

memoized_sin = cachetools.func.ttl_cache(ttl=5)(math.sin)