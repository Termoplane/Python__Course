cipher = dict.fromkeys(list(input()))

signs = list(input())

i = 0

for keys in cipher:
    cipher[keys] = signs[i]
    i += 1

inp_1 = list(input())
inp_2 = list(input())

for i in range(len(inp_1)):
        inp_1[i] = cipher[inp_1[i]]

cipher = {k:v for v, k in cipher.items()}

for i in range(len(inp_2)):
        inp_2[i] = cipher[inp_2[i]]

str_1 = ''.join(inp_1)
str_2 = ''.join(inp_2)

print(str_1, '\n', str_2)

#message = list(input())
#cipher = list(input())
#
#input_1 = input()
#input_2 = input()
#
#f