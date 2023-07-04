T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    aa = [list(input()) for _ in range(n)]
    aa_t = list(map(list, zip(*aa)))

    flag = 0

    for i in range(n):
        for j in range(n-4):
            if aa[i][j] == aa[i][j+1] == aa[i][j+2] == aa[i][j+3] == aa[i][j+4] == 'o':
                flag = 1
                break

    for i in range(n):
        for j in range(n-4):
            if aa_t[i][j] == aa_t[i][j+1] == aa_t[i][j+2] == aa_t[i][j+3] == aa_t[i][j+4] == 'o':
                flag = 1
                break

    for i in range(n-4):
        for j in range(n-4):
            if aa[i][j] == aa[i+1][j+1] == aa[i+2][j+2] == aa[i+3][j+3] == aa[i+4][j+4] == 'o':
                flag = 1
                break

    for i in range(n-4):
        for j in range(n-1, 3, -1):
            if aa_t[i][j] == aa_t[i+1][j-1] == aa_t[i+2][j-2] == aa_t[i+3][j-3] == aa_t[i+4][j-4] == 'o':
                flag = 1
                break

    if flag:
        rs = 'YES'
    else:
        rs = 'NO'

    print(f'#{test_case} {rs}')