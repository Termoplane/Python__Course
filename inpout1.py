with open('dataset_3363_2 (2).txt', 'r') as strg:
    s = strg.readline().strip()

ans = ''

for i in range(len(s) - 1):
    if s[i].isdigit() == 0:
        alph = s[i]
    else:
        dig = (s[i])
        if s[i + 1].isdigit() == 1:
            dig = dig + s[i]
            dig = int(dig) - 1 
        dig = int(dig)
        ans += alph * dig

with open ('answer.txt', 'w') as inf:
    inf.write(str(ans))



