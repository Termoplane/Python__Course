def counter(s, a, b):
    i = 0
    if a not in s:
        return 0
    if a in b:
        return "Impossible"
    while a in s:
        s = s.replace(a, b)
        i += 1
        if i > 1000:
            return "Impossible"
    return i

s = input()
a = input()
b = input()

print(counter(s, a, b))