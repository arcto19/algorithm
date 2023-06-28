T = int(input())

for test_case in range(1, T+1):
    n, m, k = map(int, input().split())
    ls = list(map(int, input().split())) # 도착 시간
    ls.sort()

    flag = 0
    for i in range(len(ls)):
        b = (ls[i]//m)*k # 도착 시간의 제품 개수(b), 도착 시간(ls[i])
        if b < i+1: # 도착 시간의 제품 개수(b) < 도착 인원(i+1)
            flag = 1 # 지연 발생
            break

    if flag:
        rs = 'Impossible'
    else:
        rs = 'Possible'

    print(f'#{test_case} {rs}')