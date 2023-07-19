import sys
input = sys.stdin.readline

n = int(input())

sum_value = 1

bgn_point, end_point = 1, 1

result = 0
while end_point <= n:
    if sum_value > n:
        sum_value -= bgn_point
        bgn_point += 1
    elif sum_value < n:
        end_point += 1
        sum_value += end_point
    else:
        result += 1
        end_point += 1
        sum_value += end_point

print(result)