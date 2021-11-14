import requests
import json


g = requests.get('https://api.github.com/users/willyblaise')

j = json.loads(g.content)

print(f"My login id is: {j['login']}")
