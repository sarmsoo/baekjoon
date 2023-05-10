from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

n = int(input())

nums = []
for i in range(n):
    heappush(nums, int(input()))

answer = 0
while len(nums) > 1:
    first = heappop(nums)
    second = heappop(nums)

    tmp = first + second
    answer += tmp

    heappush(nums, tmp)

print(answer)