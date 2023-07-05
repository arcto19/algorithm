def dfs(level, value):
    global ct

    if value > k:
        return

    if value == k:
        ct += 1
        return
    else:
        for i in range(level, n):
            dfs(i+1, value+ls[i])

T = int(input())

for test_case in range(1, T+1):
    n, k = map(int, input().split())
    ls = list(map(int, input().split()))

    ct = 0
    dfs(0, 0)

    print(f'#{test_case} {ct}')