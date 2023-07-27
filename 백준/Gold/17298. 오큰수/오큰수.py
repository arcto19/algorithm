import sys
input = sys.stdin.readline

n = int(input())

list_number = list(map(int, input().split()))

result = [-1]*n

stack = []
for i in range(n):
    while stack and list_number[stack[-1]] < list_number[i]:
        result[stack.pop()] = list_number[i]
    stack.append(i)

print(*result)