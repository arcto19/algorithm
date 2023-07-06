def dfs(level, value):
    global mn
 
    if value >= b:
        mn = min(mn, value)
        return
 
    if level == n:
        if value >= b:
            mn = min(mn, value)
        return
    else:
        dfs(level+1, value)
        dfs(level+1, value+ls[level])
 
T = int(input())
 
for test_case in range(1, T+1):
    n, b = map(int, input().split())
    ls = list(map(int, input().split()))
 
    mn = 21e8
    dfs(0, 0)
 
    print(f'#{test_case} {mn-b}')