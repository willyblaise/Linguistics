import json
import requests


g = requests.get('http://127.0.0.1:8080/api/v1/resources/injects/all')

j = json.loads(g.content)

for i in j:
    print(i)
