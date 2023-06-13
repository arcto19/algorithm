T = 10

for test_case in range(1, T+1):
    _ = int(input())
    arr = [list(map(int, input().split())) for y in range(100)]

    mn = 21e8
    for x in range(100):
        if arr[0][x] == 1:
            dx = x

            y, cnt = 0, 0
            while y < 99:
                if dx > 0 and arr[y][dx-1]:
                    while dx > 0 and arr[y][dx-1]:
                        dx -= 1
                        cnt += 1
                elif dx < 99 and arr[y][dx+1]:
                    while dx < 99 and arr[y][dx+1]:
                        dx += 1
                        cnt += 1
                y += 1
                cnt += 1

            if cnt <= mn:
                res, mn = x, cnt

    print(f'#{test_case} {res}')