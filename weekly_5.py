with open('dataset_3380_5 (1).txt') as f:
    p = []
    d = {}
    for l in f:
        p.append(l.strip('\n').split('\t'))
    print(p)
    for y in p:
        y[0] = int(y[0])
        y[2] = int(y[2])
    print(p)
    for c in p:
        if int(c[0]) in d:
            d[c[0]].append(c[2])
        else:
            d[c[0]] = [c[2]]

    for k in sorted(d.keys()):
        print(k, '', sum(d[k]) / float(len(d[k])))