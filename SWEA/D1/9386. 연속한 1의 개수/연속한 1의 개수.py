T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    lst = input().split('0')

    mx = 0
    for l in lst:
        mx = max(mx, len(l))

    print(f'#{test_case} {mx}')