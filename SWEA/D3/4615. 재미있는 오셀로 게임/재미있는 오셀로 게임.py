dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

T = int(input())

for test_case in range(1, T+1):
    n, m = map(int, input().split())

    arr = [[0]*n for _ in range(n)]

    for y in range(n//2-1, n//2+1):
        for x in range(n//2-1, n//2+1):
            if (y+x)%2:
                arr[y][x] = 1
            else:
                arr[y][x] = 2

    for i in range(m):
        x, y, z = map(int, input().split())
        arr[y-1][x-1] = z
        for j in range(8):
            for k in range(1, n):
                ny = y-1 + dy[j]*k
                nx = x-1 + dx[j]*k
                if 0 <= ny < n and 0 <= nx < n:
                    if not arr[ny][nx]:
                        break
                    elif arr[ny][nx] == z:
                        for l in range(1, k):
                            my = y-1 + dy[j]*l
                            mx = x-1 + dx[j]*l
                            arr[my][mx] = z
                        break

    bk, wt = 0, 0
    for y in range(n):
        for x in range(n):
            if arr[y][x] == 1:
                bk += 1
            elif arr[y][x] == 2:
                wt += 1

    print(f'#{test_case} {bk} {wt}')