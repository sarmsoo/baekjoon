from sys import stdin
from sys import setrecursionlimit
input = stdin.readline
setrecursionlimit(10 ** 5)

# bottom-up
'''
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
dp[0][0] = graph[0][0]

for i in range(1, n):
    dp[i][0] = graph[i][0] + dp[i - 1][0]
for j in range(1, m):
    dp[0][j] = graph[0][j] + dp[0][j - 1]

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = graph[i][j] + max(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1])

print(dp[n - 1][m - 1])
'''
# top-down
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
dp[0][0] = graph[0][0]

def sol(y, x):
    if y == 0 and x == 0:
        return graph[0][0]

    if y < 0 or y >= n or x < 0 or x >= m:
        return 0

    if dp[y][x] != 0:
        return dp[y][x]

    dp[y][x] = graph[y][x] + max(sol(y - 1, x), sol(y, x - 1), sol(y - 1, x - 1))
    return dp[y][x]

print(sol(n - 1, m - 1))