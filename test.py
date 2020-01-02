n = int(input())
graph = {}

for j in range(n):
    inp = input().split(' ')
    graph[inp[0]] = []
    inp.remove(':')
    for j in inp[1:]:
        graph[inp[0]].append(j)

print(graph)