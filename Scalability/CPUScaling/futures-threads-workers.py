from concurrent import futures
import random

def compute():
    return sum(
        [random.randint(1, 100) for i in range(1000000)])

with futures.ProcessPoolExecutor() as executor: #max_workers=multiprocessing.cpu_count
    futs = [executor.submit(compute) for _ in range(8)]

results = [f.result() for f in futs]
print("Results: %s" % results)