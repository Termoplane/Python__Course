s, t = (input() for _ in range(2))

i = 0

print(s.find(t))

while s.find(t) > -1:
    i += 1
    s = s[s.find(t) + 1:]
    print(s)

print(i)