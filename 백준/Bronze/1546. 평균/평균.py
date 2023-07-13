import sys
input = sys.stdin.readline

n = int(input())

list_score = list(map(int, input().split()))

score_sum = sum(list_score)

score_max = max(list_score)

result = score_sum / score_max * 100 / n

print(result)