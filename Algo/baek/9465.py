from sys import stdin
from sys import setrecursionlimit
input = stdin.readline
setrecursionlimit(10 ** 6)

# bottom-up
'''
t = int(input())

for _ in range(t):
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(2)]

    if n == 1:
        print(max(table[0][0], table[1][0]))
        continue

    dp = [[0] * n for _ in range(2)]
    dp[0][0], dp[1][0] = table[0][0], table[1][0]
    dp[1][1], dp[0][1] = dp[0][0] + table[1][1], dp[1][0] + table[0][1]

    for i in range(2, n):
        dp[1][i] = max(dp[0][i - 1] + table[1][i], dp[0][i - 2] + table[1][i])
        dp[0][i] = max(dp[1][i - 1] + table[0][i], dp[1][i - 2] + table[0][i])

    print(max(dp[0][n - 1], dp[1][n - 1]))
'''

# top-down


def sol(i: int, j: int) -> int:
    if dp[i][j] != 0:
        return dp[i][j]
    if j == 0:
        return table[i][0]
    if j == 1:
        return table[0][0] + table[1][1] if i == 1 else table[1][0] + table[0][1]

    if i == 0:
        dp[0][j] = max(sol(1, j - 1) + table[0][j], sol(1, j - 2) + table[0][j])
    elif i == 1:
        dp[1][j] = max(sol(0, j - 1) + table[1][j], sol(0, j - 2) + table[1][j])

    return dp[i][j]


t = int(input())
for _ in range(t):
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]

    print(max(sol(0, n - 1), sol(1, n - 1)))
