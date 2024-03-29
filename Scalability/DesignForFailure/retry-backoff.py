#exponential backoff

import time
import random

def do_something():
    if random.randint(0, 1) == 0:
        print("Failure")
        raise RuntimeError
    print("Success")

attempt = 0
while True:
    try:
        do_something()
    except Exception:
        time.sleep(2 ** attempt)
        attempt += 1
    else:
        break