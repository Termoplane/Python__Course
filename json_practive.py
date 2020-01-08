#Работает наоборот, считает кол-во предков, с самим собой, исправлять лень, посмотреть потом

import json

classes_read = json.loads(input())

classes = {}

for dic in classes_read:
    classes[dic['name']] = [parent for parent in dic['parents']]

ans = {}

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    try:
        for next in graph[start].remove(visited):
            dfs(graph, next, visited)
        return visited
    except ValueError:
        for next in graph[start]:
            dfs(graph, next, visited)
        return visited

for parent in classes:
    print(parent, ":", len(dfs(classes, parent)))