num_1 = int(input())
dic = [input().lower() for i in range(num_1)]  

num_2 = int(input())
values =[input().split() for j in range(num_2)]

ans = set()

for w in range(len(values)):
    if values[w].lower() not in dic:
        ans.add(values[w])

print(k + '\n' for k in ans)