from sys import stdin
input = stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [1001] * n
dp[0] = 0

for i in range(n):
    for j in range(1, nums[i] + 1):
        if i + j < n:
            dp[i + j] = min(dp[i + j], dp[i] + 1)

if dp[n - 1] != 1001:
    print(dp[n - 1])
else:
    print(-1)