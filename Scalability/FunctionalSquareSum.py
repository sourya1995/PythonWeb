def compute(numbers):
    return sum(list(map(lambda x : x*x, filter(lambda x: x < 50, numbers))))