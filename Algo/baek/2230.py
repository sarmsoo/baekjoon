from sys import stdin
from sys import maxsize
input = stdin.readline
'''
n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]
nums.sort()

answer = maxsize
for i in range(n - 1):
    for j in range(i + 1, n):
        tmp = nums[j] - nums[i]
        if tmp >= m:
            answer = min(answer, tmp)
            break

print(answer)
'''
'''
n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]
nums.sort()

answer = maxsize
j = 0
for i in range(n):
    while j < i and nums[i] - nums[j] >= m:
        answer = min(answer, nums[i] - nums[j])
        j += 1
        
print(answer)
'''

n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]
nums.sort()

answer = maxsize
j = 0
