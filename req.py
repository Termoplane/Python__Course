import requests

with open('dataset_3378_3.txt', 'r') as inf:
    site = inf.readline().strip()

catalog = 'https://stepic.org/media/attachments/course67/3.6.3/'

r = requests.get(site)


if r.text.split()[0].strip() != 'We':
    for x in range(250):
        a = r.text
        site = catalog + a
        site = site.strip()
        r = requests.get(site)
        print (r.text)
else:
    print(r.text)