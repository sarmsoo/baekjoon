from sys import stdin
input = stdin.readline

n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))

dp = [[0, 0] for _ in range(n + 1)]
dp[1][0] = arr[1]

for i in range(2, n + 1):
    dp[i][0] = max(dp[i - 2][0], dp[i - 2][1], dp[i - 3][1]) + arr[i]
    dp[i][1] = dp[i - 1][0] + arr[i]

print(max(max(dp[n]), max(dp[n - 1])))

n = int(input())
w = [0]
for i in range(n):
    w.append(int(input()))
dp = [0]
dp.append(w[1])
if n > 1:
    dp.append(w[1] + w[2])
for i in range(3, n + 1):
    dp.append(max(dp[i - 1], dp[i - 3] + w[i - 1] + w[i], dp[i - 2] + w[i]))
print(dp[n])