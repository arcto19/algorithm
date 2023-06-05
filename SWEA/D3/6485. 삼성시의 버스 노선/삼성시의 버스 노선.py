T = int(input())

for test_case in range(1, T+1):
    n = int(input())

    lst1 = [0]*5001
    for i in range(n):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            lst1[i] += 1

    p = int(input())

    lst2 = [0]*p
    for j in range(p):
        c = int(input())
        lst2[j] = lst1[c]

    print(f'#{test_case}', *lst2)