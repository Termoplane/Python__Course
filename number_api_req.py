import requests
import json

with open ('dataset_24476_3.txt', 'r') as f:
    numbers = f.read().split()

for number in numbers:
    api_url = f'http://numbersapi.com/{number}/math'

    params = {
        'json': 'true'
    }

    res = requests.get(api_url, params=params)

    if res.json()['found']:
        print('Interesting')
    else:
        print('Boring')