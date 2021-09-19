import sys
import os
import requests
import time
import logging
import datetime


#creating a logger
logging.basicConfig(filename = "/home/champ/problems.log", level = logging.DEBUG)
logger = logging.getLogger()


start = time.time()
try:
    req = requests.get(f'https://wttr.in/{sys.argv[1].replace(" ", "+")}')
except:
    logger.error(f"{datetime.datetime.now()} - Maybe no city was passed into the program.")
    raise
finally:
    stop = time.time()
    dt = stop - start
    logger.info(f"it took {dt} to run the process.")



print(req.text)
print(f"{req.status_code}")


#stax = lambda x : x * 1.0825

#subtotal = int(input("Please provide the Subtotal: "))
#print(f"Subtotal + Sales Tax is: {stax(subtotal)}")