T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    aa = [list(map(int, input())) for _ in range(n)]

    r = 0
    for y in range(n):
        for x in range(abs(n//2-y), n-abs(n//2-y)):
            r += aa[y][x]

    print(f'#{test_case} {r}')