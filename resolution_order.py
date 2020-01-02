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
    if a in graph and b in graph:
        for i in range(len(graph[b])):
            while a not in graph[b]:
                return graph_measurer(a, graph[b][i])
            return False

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
    else:
        print('No')