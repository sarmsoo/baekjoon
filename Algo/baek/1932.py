from sys import stdin
input = stdin.readline

# bottom-up

n = int(input())
triangles = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * i for i in range(1, n + 1)]
dp[0][0] = triangles[0][0]
tmp1, tmp2 = 0, 0
for i in range(n):
    tmp1 += triangles[i][0]
    tmp2 += triangles[i][-1]
    dp[i][0] = tmp1
    dp[i][-1] = tmp2

for i in range(n):
    for j in range(1, i):
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + triangles[i][j]

print(max(dp[n - 1]))


# top-down

n = int(input())
triangles = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * i for i in range(1, n + 1)]
dp[0][0] = triangles[0][0]

tmp1, tmp2 = 0, 0
for i in range(n):
    tmp1 += triangles[i][0]
    tmp2 += triangles[i][-1]
    dp[i][0] = tmp1
    dp[i][-1] = tmp2

def sol(i, j):
    if i == 0:
        return dp[0][0]
    if dp[i][j] != 0:
        return dp[i][j]

    dp[i][j] = max(sol(i - 1, j), sol(i - 1, j - 1)) + triangles[i][j]
    return dp[i][j]

answer = 0
for i in range(n):
    answer = max(answer, sol(n - 1, i))

print(answer)

