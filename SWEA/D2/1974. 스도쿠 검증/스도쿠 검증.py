T = int(input())

for test_case in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    flag = 0

    for y in range(9): # rows
        rows = []
        for x in range(9):
            if arr[y][x] in rows:
                flag += 1
                break
            else:
                rows.append(arr[y][x])

    for x in range(9): # cols
        cols = []
        for y in range(9):
            if arr[y][x] in cols:
                flag += 1
                break
            else:
                cols.append(arr[y][x])

    for y in range(0, 9, 3): # 3*3 grid
        for x in range(0, 9, 3):
            grid = []
            for dy in range(3):
                for dx in range(3):
                    ny, nx = y + dy, x + dx
                    if arr[ny][nx] in grid:
                        flag += 1
                        break
                    else:
                        grid.append(arr[ny][nx])

    if flag:
        res = 0
    else:
        res = 1

    print(f'#{test_case} {res}')