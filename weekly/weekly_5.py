with open('dataset_3380_5 (1).txt') as f:
    s = list(f)
    
for i in range(len(s)):
    s[i] = s[i].strip().split('\t')

d = {a:[] for a in range(1, 12)}

for i in range(len(s)):
    if int(s[i][0]) in d: 
        d[float(s[i][0])].append(float(s[i][2]))

print(d)

for j in range(1,12):
    if d[j]:
        print(j, sum(d[j])/len(d[j]))   
    else:
        print(j, '-')