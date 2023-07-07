from sys import stdin, maxsize
input = stdin.readline

# top-down
def sol(i, j, start):
    if dp[i][j] != 0:
        return dp[i][j]
    if i == 1:
        return table[1][j]

    tmp = maxsize
    for l in range(3):
        if l == j:
            continue
        if i > 2:
            tmp = min(tmp, sol(i - 1, l, start))
            continue
        if l != start:
            tmp = min(tmp, sol(i - 1, l, start))
    dp[i][j] = tmp + table[i][j]
    return dp[i][j]


n = int(input())
table = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(n)]

answer = maxsize
for j in range(3):
    dp = [[0] * 3 for _ in range(n + 1)]
    sol(n, j, j)
    answer = min(answer, dp[n][j])

print(answer)

# bottom-up
answer = maxsize
for j in range(3):
    dp = [[maxsize] * 3 for _ in range(n + 1)]
    dp[1][j] = table[1][j]
    for i in range(2, n + 1):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + table[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + table[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + table[i][2]

    for l in range(3):
        if j == l:
            continue
        answer = min(answer, dp[n][l])
print(answer)