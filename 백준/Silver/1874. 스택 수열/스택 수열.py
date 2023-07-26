import sys
input = sys.stdin.readline

n = int(input())

list_number = [int(input()) for _ in range(n)]

i = 1
stack = []
result = []

flag = 0
for number in list_number:
    while i <= number:
        stack.append(i)
        result.append('+')
        i += 1
    
    if stack.pop() != number:
        flag = 1
        break

    result.append('-')

if flag:
    print('NO')
else:
    print('\n'.join(result))