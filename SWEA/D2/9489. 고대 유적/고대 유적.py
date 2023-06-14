T = int(input())

for test_case in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    mx_h = -21e8
    for y in range(n): # y축 탐색
        cnt = 0
        for x in range(m):
            if arr[y][x] == 1:
                cnt += 1
                if cnt >= 2:
                    if cnt > mx_h:
                        mx_h = cnt
            else:
                cnt = 0

    mx_v = -21e8
    for x in range(m): # x축 탐색
        cnt = 0
        for y in range(n):
            if arr[y][x] == 1:
                cnt += 1
                if cnt >= 2:
                    if cnt > mx_v:
                        mx_v = cnt
            else:
                cnt = 0

    print(f'#{test_case} {max(mx_h, mx_v)}')