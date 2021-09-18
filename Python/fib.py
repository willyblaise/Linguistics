from functools import lru_cache
from functools import reduce

@lru_cache(maxsize=1000)
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)


for n in range(1, 500):
    print(n, ":", fibonacci(n))


lis = [1,2,3,4,5,6]
print("\n")
sum = reduce(lambda x,y : x+y, lis)
print(f"The sum reduced is: {sum}")