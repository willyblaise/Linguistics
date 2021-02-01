

def dub(n):
    return lambda a: a*n

dubN = dub(2)

if __name__ == "__main__":
    n = int(input("Could you give me a number to double: "))
    print("{} doubled is {}".format(n, dubN(n)))
