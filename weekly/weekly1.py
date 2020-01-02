num = int(input())

res = {}

def football_qualifier () :
    global res
    match = input().strip().split(';')
    if match[0] not in res:
        res[match[0]] = [0, 0, 0, 0, 0]
        res[match[0]][0] += 1
        if match[1] > match[3]:
            res[match[0]][1] += 1
            res[match[0]][4] += 3
        elif match[1] < match[3]:
            res[match[0]][3] += 1
        else:
            res[match[0]][2] += 1
            res[match[0]][4] += 1
    else:
        res[match[0]][0] += 1
        if match[1] > match[3]:
            res[match[0]][1] += 1
            res[match[0]][4] += 3
        elif match[1] < match[3]:
            res[match[0]][3] += 1
        else:
            res[match[0]][2] += 1
            res[match[0]][4] += 1
    if match[2] not in res:
        res[match[2]] = [0, 0, 0, 0, 0]
        res[match[2]][0] += 1
        if match[3] > match[1]:
            res[match[2]][1] += 1
            res[match[2]][4] += 3
        elif match[3] < match[1]:
            res[match[2]][3] += 1
        else:
            res[match[2]][2] += 1
            res[match[2]][4] += 1
    else:
        res[match[2]][0] += 1
        if match[3] > match[1]:
            res[match[2]][1] += 1
            res[match[2]][4] += 3
        elif match[3] < match[1]:
            res[match[2]][3] += 1
        else:
            res[match[2]][2] += 1
            res[match[2]][4] += 1

for i in range(num):
    football_qualifier()

for q, w in res.items():
    print((q+':'), *w, end='\n')