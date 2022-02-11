


toys = [ 20, 100, 10, 22, 18, 11 ]


def how_many_toys(input, k):
    summation = 0
    count = 0

    for i in input:
        if  summation + i <= k:
            summation += i
            count += 1
    return count



if __name__ == "__main__":

    k = int(input("How much money do you have to spend? "))
    toys.sort()
    print(toys)
    toy_count = how_many_toys(toys, k)

    print(f"You can buy {toy_count} items.")
