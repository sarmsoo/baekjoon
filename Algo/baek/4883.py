from sys import stdin
input = stdin.readline

cnt = 0
while True:
    cnt += 1
    n = int(input())
    if n == 0:
        break

    graph = [[]] + [list(map(int, input().split())) for _ in range(n)]

    dp = [[0] * 3 for _ in range(n + 1)]
    dp[1][0] = 1000
    dp[1][1] = graph[1][1]
    dp[1][2] = dp[1][1] + graph[1][2]

    for i in range(2, n + 1):
        dp[i][0] = min(dp[i - 1][0], dp[i - 1][1]) + graph[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2], dp[i][0]) + graph[i][1]
        dp[i][2] = min(dp[i - 1][1], dp[i - 1][2], dp[i][1]) + graph[i][2]

    print(f'{cnt}. {dp[n][1]}')