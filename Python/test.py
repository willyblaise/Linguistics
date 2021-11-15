import itertools
import time
import numpy as np
import requests
import json
from collections import namedtuple

# customDecoder unction
def customDecoder(geekDict):
    return namedtuple('X', geekDict.keys())(*geekDict.values())

start = time.time()

lottery = np.random.randint(1,51,(4,6))
alottery = np.array(lottery)


with open('combinations.txt', 'w') as f:
    f.write("hello")

print(lottery)

#object mapping using json
r = requests.get('https://api.github.com/users/willyblaise')
response = r.text

personData = '{"id": 1, "last_name": "Wayne", "age": 71}'
personData2 = '{"id": 1, "last_name": "Carter", "age": 52}'
person = json.loads(personData, object_hook = lambda x : namedtuple("Person", x.keys()) (*x.values()))

person2 = json.loads(personData2, object_hook = customDecoder)

ghub = json.loads(response, object_hook = lambda x : namedtuple("Ghub", x.keys()) (*x.values()))

print(f"My last name is {person.last_name} and my age is {person.age}")
print(f"My last name is {person2.last_name} and my age is {person2.age}")
print(f"My login name is {ghub.login} and my URL is {ghub.url}")
print(r)

stop = time.time()
total_time = stop - start

print(f"Total time to run on this computer is {total_time}")