n = int(input())

list_number = list(map(int, input().split()))

list_sorted = []
for i in range(n):
   list_sorted.append(list_number[i])
   for j in range(i, 0, -1):
       if list_sorted[j] < list_sorted[j-1]: # 오름차순
           list_sorted[j], list_sorted[j-1] = list_sorted[j-1], list_sorted[j]

prefix_sum = [0]*n

prefix_sum[0] = list_sorted[0]

for i in range(1, n):
    prefix_sum[i] = prefix_sum[i-1] + list_sorted[i]

result = sum(prefix_sum)

print(result)