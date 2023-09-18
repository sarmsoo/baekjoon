n = int(input())

dp = [0] * 1000001
dp[0] = 1
dp[1] = 2
dp[2] = 7

tmp = 0
for i in range(3, n + 1):
    tmp += dp[i - 3]
    dp[i] = (dp[i - 1] * 2 + dp[i - 2] * 3 + tmp * 2) % 1000000007

print(dp[n])