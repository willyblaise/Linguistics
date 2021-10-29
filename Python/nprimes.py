import itertools

def prime_numbers():
    yield 2
    prime_cache = [2]

    for n in itertools.count(3,2):
        print(f"current num by 3 {n}")
        is_prime = True

        for p in prime_cache:
            if n % p == 0:
                is_prime = False
                break

        if is_prime:
            prime_cache.append(n)
            yield n

max = int(input("Please enter the max number: "))
for k in prime_numbers():
    print(f"{k} is prime.")
    if k > max:
        break
