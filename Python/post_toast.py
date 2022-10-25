import requests
import json
from datetime import datetime


def get_part_of_day(h):
    return (
        "morning"
        if 5 <= h <= 11
        else "afternoon"
        if 12 <= h <= 17
        else "evening"
        if 18 <= h <= 22
        else "night"
    )


hour = int(input("What is the hour of the day?"))

tod = get_part_of_day(hour)

meal = input(f"What did Cool have eat this {tod}?")

med = {
        "units" : 2,
        "meal" : meal,
        "subjectId" : 1
    }

url = 'http://127.0.0.1:8080/api/v1/resources/injects/create'

x = requests.post(url, data = med)

print(f"return code: {x}")
