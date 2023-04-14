from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1] + graph[i - 1][j - 1]

for _ in range(m):
    y1, x1, y2, x2 = map(int, input().split())
    answer = dp[max(y2, y1)][max(x2, x1)] \
             - dp[min(y2, y1) - 1][max(x2, x1)] - dp[max(y2, y1)][min(x2, x1) - 1] \
             + dp[min(y2, y1) - 1][min(x2, x1) - 1]

    print(answer)