from sys import stdin
from copy import deepcopy
input = stdin.readline

n = int(input())
dp = [[[0] * 2 for _ in range(3)] for i in range(2)]

for i in range(1, n + 1):
    a, b, c = map(int, input().split())
    # max
    dp[1][0][0] = max(dp[0][0][0], dp[0][1][0]) + a
    dp[1][1][0] = max(dp[0][0][0], dp[0][1][0], dp[0][2][0]) + b
    dp[1][2][0] = max(dp[0][1][0], dp[0][2][0]) + c

    # min
    dp[1][0][1] = min(dp[0][0][1], dp[0][1][1]) + a
    dp[1][1][1] = min(dp[0][0][1], dp[0][1][1], dp[0][2][1]) + b
    dp[1][2][1] = min(dp[0][1][1], dp[0][2][1]) + c

    dp[0] = deepcopy(dp[1])

max_ = max(dp[1][0][0], dp[1][1][0], dp[1][2][0])
min_ = min(dp[1][0][1], dp[1][1][1], dp[1][2][1])

print(max_, min_)