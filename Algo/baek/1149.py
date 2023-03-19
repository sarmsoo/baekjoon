from sys import stdin
input = stdin.readline

# bottom - up

n = int(input())
dp = [[0] * 3 for _ in range(n + 1)]
for i in range(1, n + 1):
    r, g, b = map(int, input().split())

    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + r
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + g
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + b

print(min(dp[n]))


# top-down
from sys import setrecursionlimit
setrecursionlimit(10 ** 5)

n = int(input())
rgbs = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    r, g, b = map(int, input().split())
    rgbs[i].append(r)
    rgbs[i].append(g)
    rgbs[i].append(b)

dp = [[0] * 3 for _ in range(n + 1)]
dp[1][0] = rgbs[1][0]
dp[1][1] = rgbs[1][1]
dp[1][2] = rgbs[1][2]

def sol(i, j):
    if i == 1:
        return dp[1][j]
    if dp[i][j]:
        return dp[i][j]

    dp[i][0] = min(sol(i - 1, 1), sol(i - 1, 2)) + rgbs[i][0]
    dp[i][1] = min(sol(i - 1, 0), sol(i - 1, 2)) + rgbs[i][1]
    dp[i][2] = min(sol(i - 1, 0), sol(i - 1, 1)) + rgbs[i][2]

    return dp[i][j]

print(min(sol(n, 0), sol(n, 1), sol(n, 2)))