#retry and sleep

import time
import random

def do_something():
    if random.randint(0, 1) == 0:
        print("Failure")
        raise RuntimeError
    print("Success")

while True:
    try:
        do_something()
    except Exception:
        time.sleep(1)
    else:
        break
        