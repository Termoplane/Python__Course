a = int(input())

ans = dict.fromkeys(['север','юг','запад','восток'], 0)

for x in range(a):
    x = input().split()
    if x[0] in ans.keys():
        ans[x[0]] += int(x[1])

print(ans['восток'] - ans['запад'], ans['север'] - ans['юг'], end = '')