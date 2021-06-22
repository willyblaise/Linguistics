import sys
import requests

resp = requests.get(f'https://wttr.in/{sys.argv[1].replace(" ", "+")}')

print(resp.text)
print(f"Response Code: {resp.status_code}")
