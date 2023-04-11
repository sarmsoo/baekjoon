from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 5)
input = stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1] * m for _ in range(n)]
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(sy, sx):
    if sy == n - 1 and sx == m - 1:
        return 1

    if dp[sy][sx] != -1:
        return dp[sy][sx]

    ways = 0
    for i in range(4):
        ny = sy + dy[i]
        nx = sx + dx[i]
        if 0 <= ny < n and 0 <= nx < m and graph[sy][sx] > graph[ny][nx]:
            ways += dfs(ny, nx)

    dp[sy][sx] = ways
    return dp[sy][sx]

print(dfs(0, 0))