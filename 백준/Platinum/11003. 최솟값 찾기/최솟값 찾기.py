import sys
input = sys.stdin.readline

from collections import deque

n, l = map(int, input().split())
list_number = list(map(int, input().split()))

q = deque()
for i in range(n):
    while q and q[0][0] < i-l+1:
        q.popleft()

    while q and q[-1][1] > list_number[i]:
        q.pop()

    q.append((i, list_number[i]))

    print(q[0][1], end=" ")