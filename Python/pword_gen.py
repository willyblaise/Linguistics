import string
import random


combo = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits

long = 8

temp = random.sample(combo, long)
password = "".join(temp)
print(password)
