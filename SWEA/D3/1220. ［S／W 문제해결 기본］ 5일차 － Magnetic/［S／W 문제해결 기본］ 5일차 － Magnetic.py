T = 10

for test_case in range(1, T+1):
    n = int(input())
    aa = [list(map(int, input().split())) for _ in range(n)]

    ct = 0
    for x in range(n):
        ns = 0
        for y in range(n):
            if aa[y][x]:
                ss = aa[y][x]
                if ns == 1 and ss == 2:
                    ct += 1
                ns = aa[y][x]

    print(f'#{test_case} {ct}')