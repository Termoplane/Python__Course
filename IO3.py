with open("dataset_3363_4 (2).txt", "r", encoding='utf-8') as text:
    s = text.read().split('\n')

i = 0
first = 0
second = 0
third = 0

for j in s:
    j = j.split(';')
    s[i] = j
    i+=1

avball = []

for k in range(len(s) - 1):
    avball.append(str(round(((int(s[k][1])+int(s[k][2])+int(s[k][3])) / 3), 9)))
    first = first + int(s[k][1])
    second = second + int(s[k][2])
    third = third + int(s[k][3])

first = first / (len(s) - 1) 
second = second / (len(s) - 1) 
third = third / (len(s) - 1) 

with open("answer.txt", 'w') as answer:
    for i in range(len(avball)):
        print(avball[i], file = answer)
    print(round(first, 9),round(second, 9),round(third, 9), file=answer)