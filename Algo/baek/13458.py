from sys import stdin
from math import ceil
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())

answer = 0
for num in arr:
    answer += 1
    num -= b
    answer += max(0, ceil((num / c)))

print(answer)