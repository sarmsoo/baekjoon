# top-down
'''
from sys import setrecursionlimit
setrecursionlimit(10 ** 5)

n, k = map(int, input().split())

dp = [[0] * (k + 1) for _ in range(n + 1)]
dp[1][0] = 1
if k > 0:
    dp[1][1] = 1


def sol(i, j):
    if dp[i][j] != 0:
        return dp[i][j]

    if j == 0 or i == j:
        dp[i][j] = 1
        return dp[i][j]

    dp[i][j] = sol(i - 1, j - 1) + sol(i - 1, j)
    return dp[i][j]


print(sol(n, k) % 10007)
'''

# bottom-up

n, k = map(int, input().split())

dp = [[0] * (k + 1) for _ in range(n + 1)]
dp[1][0] = 1
if k > 0:
    dp[1][1] = 1

for i in range(2, n + 1):
    for j in range(0, k + 1):
        if j == 0 or i == j:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

print(dp[n][k] % 10007)