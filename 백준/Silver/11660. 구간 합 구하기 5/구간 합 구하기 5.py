import sys
input = sys.stdin.readline

n, m = map(int, input().split())

ar = [[0]*(n+1)]

for _ in range(n):
    temp = [0] + list(map(int, input().split()))
    ar.append(temp)

for y in range(1, n+1):
    for x in range(2, n+1):
        ar[y][x] += ar[y][x-1]

for x in range(1, n+1):
    for y in range(2, n+1):
        ar[y][x] += ar[y-1][x]

for _ in range(m):
    y1, x1, y2, x2 = map(int, input().split())
    result = ar[y2][x2] - ar[y1-1][x2] - ar[y2][x1-1] + ar[y1-1][x1-1]
    print(result)