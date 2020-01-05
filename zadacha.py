#Задача по поиску директорий в директории main, в которых содержится файлы с расширением .py
import os


answer_test = []
answer = []

os.chdir('main')
for current_dir, dirs, files in os.walk('.'):
    for current_file in files:
        if current_file[-3:] == '.py' and current_dir[2:] not in answer_test:
            answer_test.append(current_dir[2:])
            

answer = sorted(answer_test)

with open ('answer.txt', 'w') as ans:
    ans.write('\n'.join(answer))