T = int(input())

for test_case in range(1, T+1):
    aa = [list(input()) for _ in range(5)]

    s = ''
    for x in range(15):
        for y in range(5):
            if x < len(aa[y]):
                s += aa[y][x]

    print(f'#{test_case} {s}')