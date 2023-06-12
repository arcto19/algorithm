T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    arr = [input().split() for _ in range(n)]
    arr_t = list(map(list, zip(*arr)))

    print(f'#{test_case}')
    for i in range(n):
        print(f'{"".join(arr_t[i][::-1])} {"".join(arr[n-1-i][::-1])} {"".join(arr_t[n-1-i])}')