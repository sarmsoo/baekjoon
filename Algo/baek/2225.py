n, k = map(int, input().split())

dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][1] = 1

for j in range(1, k + 1):
    dp[1][j] = j

for i in range(2, n + 1):
    for j in range(2, k + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

print(dp[n][k] % 1000000000) # 맞는거 같은데 틀렸을 때, 다시 한 번 출력문을 봐라...