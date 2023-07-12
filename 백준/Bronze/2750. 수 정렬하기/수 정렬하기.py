import sys
input = sys.stdin.readline

n = int(input())

list_number = [int(input()) for _ in range(n)]

list_number.sort()

print(*list_number, sep='\n')