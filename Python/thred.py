import time
from threading import Thread


def start():
    print("We are starting here: ")
    time.sleep(3)
    print("We are done starting")

def stop():
    print("Stopping soon: ")
    time.sleep(2)
    print("Done Stopping....")


if __name__ == "__main__":
    t1 = Thread(target=start)
    t2 = Thread(target=stop)

    t1.start()
    t2.start()