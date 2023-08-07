import sys
input = sys.stdin.readline

list_number = list(input())

for i in range(len(list_number)-1):
    for j in range(i+1, len(list_number)):
        if list_number[i] > list_number[j]:
            list_number[i], list_number[j] = list_number[j], list_number[i]

for i in range(len(list_number)-1, -1, -1):
    print(list_number[i], end='')
print()