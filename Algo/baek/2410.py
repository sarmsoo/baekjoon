from sys import stdin
input = stdin.readline

n = int(input())
dp = [0] * (n + 1)
dp[0] = 1

arr = [2 ** k for k in range(21)]

for i in arr:
    if i <= n:
        for j in range(i, n + 1):
            dp[j] += (dp[j - i]) % 1000000000

print(dp[n] % 1000000000)