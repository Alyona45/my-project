
n = int(input())
MY_CACHE = {}

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n in MY_CACHE.keys():
        return MY_CACHE[n]
    else:
        fib_number = fibonacci(n-1) + fibonacci(n-2)
        MY_CACHE[n] = fib_number
        return fib_number
print(fibonacci(n))