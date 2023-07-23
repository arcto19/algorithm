import sys
input = sys.stdin.readline

n = int(input())

list_number = list(map(int, input().split()))
list_number.sort()

bgn_point, end_point = 0, n-1

result = 0
for i in range(n):
    target = list_number[i]

    bgn_point, end_point = 0, n-1

    while bgn_point < end_point:
        bgn_number, end_number = list_number[bgn_point], list_number[end_point]
        if bgn_number + end_number > target:
            end_point -= 1
        elif bgn_number + end_number < target:
            bgn_point += 1
        else:
            if bgn_point != i and end_point != i:
                result += 1
                break
            elif bgn_point == i:
                bgn_point += 1
            elif end_point == i:
                end_point -= 1

print(result)