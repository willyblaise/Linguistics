import time
import logging
import datetime

logging.basicConfig(filename = "/home/champ/problems2.log", level = logging.DEBUG)
logger = logging.getLogger()


def pchg():
    cv = int(input("Please provide the current value: "))
    iv = int(input("Please provide the initial value: "))

    c_minus_i = cv - iv
    try:
        c_minus_i = c_minus_i / iv
    except ZeroDivisionError:
        logger.error(f"{datetime.datetime.now()} - You cannot divide by zero")
        raise
    finally:
        logger.info(f"This app finished at {datetime.datetime.now()}")

    return c_minus_i * 100


if __name__ == "__main__":
    pc = pchg()
    print("The percentage change is {}".format(pc))
