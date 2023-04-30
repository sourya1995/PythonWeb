import random
import multiprocessing

def compute(results):
    results.append(sum(
        [random.randint(1, 100) for i in range(1000000)]))

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=8)
    print("Results: %s" % pool.map(compute, range(8)))