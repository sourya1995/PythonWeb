import multiprocessing
import time

def print_footballer():
    time.sleep(0.1)
    print("Eric Cantona")
    print("David Beckham")
    print("Cristiano Ronaldo")
    print("Edinson Cavani")

with multiprocessing.Pool(processes=3) as Pool:
    jobs = []
    for _ in range [5]: #print 5 items in parallel
        jobs.append(Pool.apply_async(print_footballer))
    for job in jobs:
        job.wait()

    