from sys import stdin
input = stdin.readline

# bottom-up

dp = [0] * 101
dp[1] = dp[2] = dp[3] = 1
dp[4] = dp[5] = 2
for i in range(6, 101):
    dp[i] = dp[i - 1] + dp[i - 5]

for _ in range(int(input())):
    n = int(input())
    print(dp[n])