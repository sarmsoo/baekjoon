from sys import maxsize
# bottom-up
n = int(input())

dp = [[maxsize, []] for _ in range(n + 1)]
dp[1][0], dp[1][1] = 0, [1]
if n > 1:
    dp[2][0], dp[2][1] = 1, [1, 2]

for i in range(2, n + 1):
    if i % 3 == 0 and dp[i // 3][0] + 1 < dp[i][0]:
        dp[i][0] = dp[i // 3][0] + 1
        dp[i][1] = dp[i // 3][1] + [i]
    if i % 2 == 0 and dp[i // 2][0] + 1 < dp[i][0]:
        dp[i][0] = dp[i // 2][0] + 1
        dp[i][1] = dp[i // 2][1] + [i]
    if dp[i - 1][0] + 1 < dp[i][0]:
        dp[i][0] = dp[i - 1][0] + 1
        dp[i][1] = dp[i - 1][1] + [i]

print(dp[n][0])
print(*reversed(dp[n][1]))