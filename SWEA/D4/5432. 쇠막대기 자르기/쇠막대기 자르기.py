T = int(input())

for test_case in range(1, T+1):
    str = input()

    res, cnt = 0, 0
    for i in range(len(str)):
        if str[i] == '(':
            cnt += 1
        else:
            if str[i-1] == '(':
                cnt -= 1
                res += cnt
            else:
                cnt -= 1
                res += 1

    print(f'#{test_case} {res}')