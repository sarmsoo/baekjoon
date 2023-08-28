from sys import stdin
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [[0] * 2 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i][0] = max(dp[i][0], dp[j][0] + 1)

for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if arr[i] > arr[j]:
            dp[i][1] = max(dp[i][1], dp[j][1] + 1)

print(max([dp[i][0] + dp[i][1] for i in range(n)]) + 1)