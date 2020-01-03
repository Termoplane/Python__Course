from itertools import groupby
import sys
sys.stdin = open("input.txt", "r")

err_qty = int(input())
error_parents = {}

for err_class in range(err_qty):
    inp = input().split(' ')
    error_parents[inp[0]] = []
    if ':' in inp:
        inp.remove(':')
    if len(inp) > 1:
        for i in range(1, len(inp)):
            if inp[i] not in error_parents.keys():
                error_parents[inp[i]] = []
    for parent in inp[1:]:
        error_parents[inp[0]].append(parent)

ans_buffer = []
err_buffer = []

print(error_parents)

def parent_test(child):
    global err_buffer
    global error_parents
    if len(error_parents[child]) > 0:
        for parents in error_parents[child]:
            if parent_test(parents):
                return True
    else: 
        return False
check_qty = int(input())

for check_counter in range(check_qty):
    err_name = input()
    err_buffer.append(err_name)
    if parent_test(err_name) == True:
        ans_buffer.append(err_name)

new_ans = [el for el, _ in groupby(ans_buffer)]

print('\n'.join(new_ans))