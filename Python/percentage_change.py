

def pchg():
    cv = int(input("Please provide the current value: "))
    iv = int(input("Please provide the initial value: "))
    pc = (cv - iv)/iv * 100
    return print("The percentage change is {}".format(pc))


if __name__ == "__main__":
    pchg()
