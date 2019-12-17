num_1 = int(input())
dic = [input().lower() for i in range(num_1)]  

num_2 = int(input())
values = ' '.join([input() for j in range(num_2)]).strip().split(' ')

ans = set()

for k in values:
    a = k.lower()
    if a not in dic:
        ans.add(k)

print('\n'.join([k for k in ans]))