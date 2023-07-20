n = int(input())

m = int(input())

list_number = list(map(int, input().split()))
list_number.sort()

bgn_point, end_point = 0, n-1

result = 0
while bgn_point < end_point:
    bgn_number, end_number = list_number[bgn_point], list_number[end_point]
    if bgn_number + end_number > m:
        end_point -= 1
    elif bgn_number + end_number < m:
        bgn_point += 1
    else:
        result += 1
        bgn_point += 1
        end_point -= 1

print(result)