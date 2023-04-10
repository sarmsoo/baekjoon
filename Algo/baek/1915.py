from sys import stdin
from copy import deepcopy
input = stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
dp = deepcopy(graph)

for i in range(1, n):
    for j in range(1, m):
        if graph[i][j] == 1:
            if dp[i - 1][j - 1] > 0 and dp[i - 1][j] > 0 and dp[i][j - 1] > 0:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

answer = 0
for i in range(n):
    for j in range(m):
        answer = max(answer, dp[i][j])

print(answer ** 2)