dy_1 = [-1, 0, 1, 0]
dx_1 = [0, 1, 0, -1]

dy_2 = [-1, 1, 1, -1]
dx_2 = [1, 1, -1, -1]

T = int(input())

for test_case in range(1, T+1):
    n, m = map(int, input().split())
    aa = [list(map(int, input().split())) for _ in range(n)]

    mx = -21e8
    for y in range(n):
        for x in range(n):

            ct = aa[y][x]
            for i in range(4):
                for j in range(1, m):
                    ny = y + dy_1[i]*j
                    nx = x + dx_1[i]*j
                    if 0 <= ny < n and 0 <= nx < n:
                        ct += aa[ny][nx]
            mx = max(mx, ct)

            ct = aa[y][x]
            for i in range(4):
                for j in range(1, m):
                    ny = y + dy_2[i]*j
                    nx = x + dx_2[i]*j
                    if 0 <= ny < n and 0 <= nx < n:
                        ct += aa[ny][nx]
            mx = max(mx, ct)

    print(f'#{test_case} {mx}')