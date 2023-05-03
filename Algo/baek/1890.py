from sys import stdin
input = stdin.readline
# top-down

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

dy = [1, 0]
dx = [0, 1]

for y in range(n):
    for x in range(n):
        w = graph[y][x]

        if y == n - 1 and x == n - 1:
            continue

        for i in range(2):
            ny = y + dy[i] * w
            nx = x + dx[i] * w
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            dp[ny][nx] += dp[y][x]

print(dp[n - 1][n - 1])
