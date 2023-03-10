# bottom-up
'''
n = int(input())

dp = [[-1] * 10 for _ in range(n + 1)]
# 기본값
for i in range(10):
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][0] = dp[i - 1][0]
        else:
            tmp = 0
            for k in range(j + 1):
                tmp += dp[i - 1][k]

            dp[i][j] = tmp

print(sum(dp[n]) % 10007)
'''

# top-down

from sys import setrecursionlimit
setrecursionlimit(10 ** 5)

n = int(input())

dp = [[0] * 10 for _ in range(n + 1)]
# 기본값
for i in range(10):
    dp[1][i] = 1


def sol(i, j):
    if dp[i][j] != 0:
        return dp[i][j]

    for k in range(j + 1):
        dp[i][j] += sol(i - 1, k)

    return dp[i][j]


answer = 0
for i in range(10):
    answer += sol(n, i)

print(answer % 10007)