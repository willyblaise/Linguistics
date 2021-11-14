from functools import lru_cache
from functools import reduce
from timeit import timeit

fibonacci_cache = {}


@lru_cache(maxsize=1000)
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_long(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci_long(n-1) + fibonacci_long(n-2)

    fibonacci_cache[n] = value 
    return value 

for n in range(1, 500):
    print(n, ":", fibonacci(n))

print("Fibonacci Long now\n")

for n in range(1,1000):
    print(n, ":", fibonacci_long(n))
#lis = [1,2,3,4,5,6]
#print(" \n")
#sum = reduce(lambda x,y : x+y, lis)
#print(f"The sum reduced is: {sum}")

print("it took this long to run the method ", timeit(
    stmt = "fibonacci_long(1000)",
    globals=locals(),
    number = 10 ** 2
))