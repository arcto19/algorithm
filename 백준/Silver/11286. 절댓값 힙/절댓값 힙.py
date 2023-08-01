import sys
input = sys.stdin.readline

import heapq

n = int(input())

heap = []
for _ in range(n):
    number = int(input())
    if not number:
        if len(heap) > 0:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(number), number))