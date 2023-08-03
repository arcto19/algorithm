import sys
input = sys.stdin.readline

n = int(input())

list_number = [(int(input()), i) for i in range(n)]
list_number.sort()

max_value = 0
for i in range(n):
    if max_value < list_number[i][1] - i:
        max_value = list_number[i][1] - i

print(max_value+1)