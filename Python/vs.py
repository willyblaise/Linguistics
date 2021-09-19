import sys
import os
import requests

req = requests.get(f'https://wttr.in/{sys.argv[1].replace(" ", "+")}')

print(req.text)
print(f"{req.status_code}")


stax = lambda x : x * 1.0825

subtotal = int(input("Please provide the Subtotal: "))
print(f"Subtotal + Sales Tax is: {stax(subtotal)}")