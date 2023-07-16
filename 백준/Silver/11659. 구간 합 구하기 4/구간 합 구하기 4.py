import sys
input = sys.stdin.readline

n, m = map(int, input().split())

list_number = list(map(int, input().split()))

prefix_sum = [0]

temp = 0
for number in list_number:
    temp += number
    prefix_sum.append(temp)

for _ in range(m):
    i, j = map(int, input().split())
    result = prefix_sum[j] - prefix_sum[i-1]
    print(result)