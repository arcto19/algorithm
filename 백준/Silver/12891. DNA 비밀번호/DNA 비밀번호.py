import sys
input = sys.stdin.readline

list_dna = ['A', 'C', 'G', 'T']

s, p = map(int, input().split())
string_dna = input()
list_count = list(map(int, input().split()))

cnt = 0

lst = [0]*4
for i in range(p):
    if string_dna[i] == list_dna[0]:
        lst[0] += 1
    elif string_dna[i] == list_dna[1]:
        lst[1] += 1
    elif string_dna[i] == list_dna[2]:
        lst[2] += 1
    elif string_dna[i] == list_dna[3]:
        lst[3] += 1

flag = 0
if lst[0] < list_count[0]:
    flag += 1
if lst[1] < list_count[1]:
    flag += 1
if lst[2] < list_count[2]:
    flag += 1
if lst[3] < list_count[3]:
    flag += 1

if not flag:
    cnt += 1

for i in range(s-p):
    lst[list_dna.index(string_dna[i])] -= 1
    lst[list_dna.index(string_dna[i+p])] += 1

    flag = 0
    if lst[0] < list_count[0]:
        flag += 1
    if lst[1] < list_count[1]:
        flag += 1
    if lst[2] < list_count[2]:
        flag += 1
    if lst[3] < list_count[3]:
        flag += 1

    if not flag:
        cnt += 1

print(cnt)