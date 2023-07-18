import sys
input = sys.stdin.readline

n, m = map(int, input().split())

list_number = list(map(int, input().split()))

list_remainder = [0]*m

sum_value = 0
for number in list_number:
    sum_value = (sum_value + number)%m
    list_remainder[sum_value] += 1

result = list_remainder[0]
for remainder in list_remainder:
    if remainder > 1:
        result +=(remainder*(remainder-1))//2

print(result)