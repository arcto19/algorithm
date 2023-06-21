def bfs(n):
    q = []
    visit = [0]*101

    q.append(n)
    visit[n] = 1

    while q:
        fr = q.pop(0)

        for to in aa[fr]:
            if not visit[to]:
                q.append(to)
                visit[to] = visit[fr] + 1

    mx, ix = -21e8, 0
    for i in range(1, 100+1):
        if visit[i] >= mx:
            mx, ix = visit[i], i

    return ix

T = 10

for test_case in range(1, T+1):
    n, s = map(int, input().split())
    ls = list(map(int, input().split()))

    aa = [[] for _ in range(101)]
    for i in range(0, n, 2):
        fr, to = ls[i], ls[i+1]
        aa[fr].append(to)

    rs = bfs(s)

    print(f'#{test_case} {rs}')