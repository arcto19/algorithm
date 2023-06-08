T = int(input())

for test_case in range(1, T+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    cnt_h = 0
    for y in range(n):
        for x in range(n-k+1):
            flag = 0
            for dx in range(k):
                if not arr[y][x+dx]:
                    flag += 1
                    break

            if not flag:
                if x-1 < 0:
                    if not arr[y][x+k]:
                        cnt_h += 1
                elif x+k >= n:
                    if not arr[y][x-1]:
                        cnt_h += 1
                elif not arr[y][x-1]:
                    if not arr[y][x+k]:
                        cnt_h += 1

    cnt_v = 0
    for y in range(n-k+1):
        for x in range(n):
            flag = 0
            for dy in range(k):
                if not arr[y+dy][x]:
                    flag += 1
                    break

            if not flag:
                if y-1 < 0:
                    if not arr[y+k][x]:
                        cnt_v += 1
                elif y+k >= n:
                    if not arr[y-1][x]:
                        cnt_v += 1
                elif not arr[y-1][x]:
                    if not arr[y+k][x]:
                        cnt_v += 1

    print(f'#{test_case} {cnt_h + cnt_v}')