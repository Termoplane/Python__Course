import json

initial = json.loads(input())

with_children = {element['name']: [] for element in initial}

for eli in initial:
    for elc in with_children:
        if elc in eli['parents']:
            with_children[elc].append(eli['name'])

for element in with_children:
    with_children[element] = set(with_children[element])

print(with_children)