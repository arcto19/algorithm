dr = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1]
]

st = [
    [],
    [0, 1, 2, 3],
    [0, 2],
    [1, 3],
    [0, 1],
    [1, 2],
    [2, 3],
    [0, 3],
]

def bfs(y, x):
    q = []
    visit = [[0]*m for _ in range(n)]

    q.append((y, x))
    visit[y][x] = 1

    while q:
        y, x = q.pop(0)

        if visit[y][x] < l:
            for i in st[aa[y][x]]:
                ny, nx = y + dr[i][0], x + dr[i][1]
                if 0 <= ny < n and 0 <= nx < m:
                    if aa[ny][nx]:
                        if not visit[ny][nx]:
                            if (i+2)%4 in st[aa[ny][nx]]:
                                q.append((ny, nx))
                                visit[ny][nx] = visit[y][x] + 1

    ct = 0
    for y in range(n):
        for x in range(m):
            if visit[y][x]:
                ct += 1

    return ct

T = int(input())

for test_case in range(1, T+1):
    n, m, r, c, l = map(int, input().split())

    aa = [list(map(int, input().split())) for _ in range(n)]

    rs = bfs(r, c)

    print(f'#{test_case} {rs}')