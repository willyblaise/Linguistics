import random
from datetime import datetime



lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
special_characters = ['!','@','#','$','%','^','&','*','(',')']

combo = lower + upper + numbers + special_characters
length = 8

print("".join(random.sample(combo, length)))
