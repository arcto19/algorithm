dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x):
    q = []
    track = []

    visit[y][x] = 1
    q.append((y, x))
    track.append(aa[y][x])

    while q:
        y, x = q.pop(0)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if aa[ny][nx] - aa[y][x] == 1:
                    visit[ny][nx] = 1
                    q.append((ny, nx))
                    track.append(aa[ny][nx])

    return min(track), len(track)

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    aa = [list(map(int, input().split())) for _ in range(n)]

    visit = [[0]*n for _ in range(n)]

    no, ct = 0, 0
    for y in range(n):
        for x in range(n):
            if not visit[y][x]:
                no_te, ct_te = bfs(y, x)
                if ct_te > ct or (ct == ct_te and no > no_te):
                    no, ct = no_te, ct_te

    print(f'#{test_case} {no} {ct}')