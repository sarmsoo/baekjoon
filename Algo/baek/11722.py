from sys import stdin
input = stdin.readline

# 이중 for문
n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n
for i in range(n):
    for j in range(i):
        if arr[j] > arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

# bisect
n = int(input())
arr = list(map(int, input().split()))
dp = []

def bisect(nums, target):
    left, right = 0, len(nums)
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if mid > len(nums) - 1:
            return right
        if nums[mid] <= target:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

for num in arr:
    k = bisect(dp, num)

    if len(dp) == k:
        dp.append(num)
    else:
        dp[k] = num
print(len(dp))