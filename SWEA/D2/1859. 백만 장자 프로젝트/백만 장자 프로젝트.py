T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    lst = list(map(int, input().split()))

    mx = lst[-1]

    ni = 0
    for i in range(len(lst)-1, -1, -1):
        if mx > lst[i]:
            ni += (mx - lst[i])
        else:
            mx = lst[i]

    print(f'#{test_case} {ni}')