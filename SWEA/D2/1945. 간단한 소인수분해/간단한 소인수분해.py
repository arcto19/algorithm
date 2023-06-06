T = int(input())

for test_case in range(1, T+1):
    n = int(input())

    base = [2, 3, 5, 7, 11]
    exponent = [0]*5

    i = 0
    while i < 5:
        if n%base[i]:
            i += 1
        else:
            n = n//base[i]
            exponent[i] += 1

    print(f'#{test_case}', *exponent)