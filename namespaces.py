children = {'global': 'None'}
var_names ={'global': []}

def create (namespace, parent):
    if namespace not in children:
        children[namespace] = ''
        children[namespace] += parent
    if namespace not in var_names:
        var_names[namespace] = []

def add(namespace, variable):
    if variable not in var_names[namespace]:
        var_names[namespace].append(variable)
    
def get(namespace, variable):
    if variable in var_names[namespace]:
        return namespace
    elif children.get(namespace) == 'None':
        return None
    elif variable in str(var_names.items()):
        return get(children.get(namespace), variable)
    else:
        return None
    

i = int(input())

for j in range(i):
    foo, namespace, variable = (str(k) for k in input().split())
    if foo == 'create':
        create(namespace, variable)
       # print(children, var_names)
    elif foo == 'add':
        add(namespace, variable)
       # print(children, var_names)
    elif foo == 'get':
       print(get(namespace, variable))
    else:
        print('Недопустимое имя функции')    
