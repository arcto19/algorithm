dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def dfs(level, y, x, value):
    if level == 6:
        st.add(value)
        return
    else:
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < 4 and 0 <= nx < 4:
                dfs(level+1, ny, nx, value*10+aa[ny][nx])

T = int(input())

for test_case in range(1, T+1):
    aa = [list(map(int, input().split())) for _ in range(4)]
    st = set()

    for y in range(4):
        for x in range(4):
            dfs(0, y, x, aa[y][x])

    rs = len(st)

    print(f'#{test_case} {rs}')