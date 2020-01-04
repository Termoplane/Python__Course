lst = [1, 2, 3]

for i in lst:
    print(i)

it = iter(lst)
while True:
    try:
        i = next(it)
        print(i)
    except StopIteration:
        break