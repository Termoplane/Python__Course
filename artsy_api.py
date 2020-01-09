import requests
import json

client_id = '263d87baf5e1390e0745'
client_secret = '25927d363b1aa86b8a4a9d0d6cc6484c'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# достаем токен
token = r.json()["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}

with open('dataset_24476_4.txt', 'r') as f:
    id_s = f.read().split()
    for id in id_s:
        # инициируем запрос с заголовком
        res = requests.get(f"https://api.artsy.net/api/artists/{id}", headers=headers)
        res.encoding = 'utf-8'

        print(res.json()['name'], res.json()['nationality'])