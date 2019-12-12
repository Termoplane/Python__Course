import requests

with open('dataset_3378_2.txt', 'r') as adr:
    site = adr.read().strip()

url = requests.get(site)
text = url.text

with open('answer.txt', 'w') as ans:
    ans.write(str(text.count('\n')))