from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
items = [(0, 0)]
for _ in range(n):
    w, v = map(int, input().split())
    items.append((w, v))

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w, v = items[i]

        if j < w:
            dp[i][j] = dp[i - 1][j]

        else:
            dp[i][j] = max(dp[i - 1][j], v + dp[i - 1][j - w])

print(dp[n][k])