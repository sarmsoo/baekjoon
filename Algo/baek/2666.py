from sys import stdin
from sys import maxsize
input = stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
dp = [[[maxsize] * (n + 1) for _ in range(n + 1)] for _ in range(m + 1)]
dp[0][a][b] = 0

for i in range(1, m + 1):
    k = int(input())
    for y in range(1, n + 1):
        for x in range(1, n + 1):
            if dp[i - 1][y][x] == maxsize:
                continue
            dp[i][k][x] = min(dp[i][k][x], dp[i - 1][y][x] + abs(y - k))
            dp[i][y][k] = min(dp[i][y][k], dp[i - 1][y][x] + abs(x - k))

answer = maxsize
for y in range(n + 1):
    for x in range(n + 1):
        answer = min(answer, dp[m][y][x])

print(answer)