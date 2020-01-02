import sys
sys.stdin = open("input.txt", "r")

n = int(input())
graph = {}

for j in range(n):
    inp = input().split(' ')
    graph[inp[0]] = [inp[0]]
    if ':' in inp:
        inp.remove(':')
    for j in inp[1:]:
        graph[inp[0]].append(j)

def graph_measurer(a, b):
    global graph
    buf = []
    if a in graph and b in graph:
        for i in range(len(graph[b])):
            buf.append(graph[b][i])
            if a in graph[b]:
                return True
            elif i == len(graph[b]):
                for k in range(len(buf)):
                    return graph_measurer(a, buf[k])
                buf.clear()
            else:
                continue
        

req_number = int(input())

for i in range(req_number):
    inp = input().split()
    if len(inp) == 2:
        if inp[0] == inp[1]:
            print('Yes')
            continue
        if graph_measurer(inp[0], inp[1]) == True:
            print('Yes')
        else:
            print('No')