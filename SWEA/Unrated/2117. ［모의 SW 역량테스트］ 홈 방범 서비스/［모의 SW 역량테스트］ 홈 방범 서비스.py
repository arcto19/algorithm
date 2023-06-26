dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

def bfs(y, x):
    q = []
    visit = [[0]*n for _ in range(n)]

    q.append((y, x))
    visit[y][x] = 1

    k, ct, mx = 0, aa[y][x], -21e8
    while q:
        y, x = q.pop(0)

        if k != visit[y][x]:
            k = visit[y][x]
            if k*k + (k-1)*(k-1) <= m*ct:
                mx = max(mx, ct)

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if not visit[ny][nx]:
                    q.append((ny, nx))
                    visit[ny][nx] = visit[y][x] + 1
                    ct += aa[ny][nx]

    return mx

T = int(input())

for test_case in range(1, T+1):
    n, m = map(int, input().split())
    aa = [list(map(int, input().split())) for _ in range(n)]

    mx = -21e8
    for y in range(n):
        for x in range(n):
            rs = bfs(y, x)
            mx = max(mx, rs)

    print(f'#{test_case} {mx}')