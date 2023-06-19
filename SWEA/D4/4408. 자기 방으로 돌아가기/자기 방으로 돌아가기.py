T = int(input())

for test_case in range(1, T+1):
    n = int(input())

    lst = [0]*200

    for i in range(n):
        bgn, end = map(int, input().split())

        if bgn > end:
            bgn, end = end, bgn

        for j in range((bgn-1)//2, (end-1)//2+1):
            lst[j] += 1

    res = max(lst)

    print(f'#{test_case} {res}')