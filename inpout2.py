text = open("dataset_3363_3 (2).txt", 'r')
s = text.read().replace('\n', ' ').lower().split()
text.close()

s.sort()

maxim = 0

d = {x: 0 for x in s}
for i in s:
    d[i] += 1
for j in d.values():
    if j > maxim:
        maxim = j
for key, value in d.items():
    if value == maxim:
        value = str(value)
        ans = (key, value)
        ans = str(ans)

with open ('answer.txt', 'w') as inf:
    inf.write(ans)