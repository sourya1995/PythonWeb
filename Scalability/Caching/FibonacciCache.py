cache = {}

def fib(n):
    if(n <= 0):
        return 0
    if(n == 1 or n == 2):
        return 1
    try:
        return cache[n]
    except:
        result = fib(n-1) + fib(n-2)
        cache[n] = result
        return result
    

print(fib(100))