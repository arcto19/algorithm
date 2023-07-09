def dfs(level, value):
    global mn
 
    if value > mn:
        return
 
    if level > 11:
        mn = min(mn, value)
        return
    else:
        dfs(level+1, value+cost[0]*plan[level])
        dfs(level+1, value+cost[1])
        dfs(level+3, value+cost[2])
        dfs(level+12, value+cost[3])
 
T = int(input())
 
for test_case in range(1, T+1):
    cost = list(map(int, input().split()))
    plan = list(map(int, input().split()))
 
    mn = 365*3000

    dfs(0, 0)
 
    print(f'#{test_case} {mn}')