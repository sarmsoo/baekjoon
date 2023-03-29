from sys import stdin
input = stdin.readline

n = int(input())
dp = [0] * (n + 2)
table = [[] for _ in range(n + 2)]

for i in range(1, n + 1):
    t, p = map(int, input().split())
    if i + t <= n + 1:
        table[i + t].append((i, p))

for i in range(1, n + 2):
    dp[i] = dp[i - 1]

    if table[i]:
        for start, p in table[i]:
            dp[i] = max(dp[start] + p, dp[i])

print(dp[n + 1])