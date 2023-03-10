from sys import stdin
input = stdin.readline

t = int(input())

for _ in range(t):
    dp = [[0] * 15 for _ in range(15)]
    for i in range(1, 15):
        dp[0][i] = i

    k = int(input())
    n = int(input())

    for i in range(1, k + 1):
        for j in range(1, n + 1):
            temp = 0
            for l in range(1, j + 1):
                temp += dp[i - 1][l]

            dp[i][j] = temp

    print(dp[k][n])
