import re
import requests

ans = []

template = r"<a(.*?)href(.*?)=(.*?)(\"|')(((.*?):\/\/)|(\.\.)|)(.*?)(\/|:|\"|')(.*)"

inp = input().strip()

link_text = requests.get(inp).text

#print(link_text)

res = re.findall(template, link_text)

for link in res:
    dom = link[8]
    if dom not in ans:
        ans.append(dom)

ans.sort()

for dom in ans:
    print(dom)