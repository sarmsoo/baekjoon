from sys import stdin
input = stdin.readline

n = int(input())
m = int(input())
vip = [0]
for _ in range(m):
    vip.append(int(input()))
vip.append(n + 1)

dp = [0] * 41
dp[0] = 1
dp[1] = 1
for i in range(2, 41):
    dp[i] = dp[i - 2] + dp[i - 1]

answer = 1
for i in range(1, m + 2):
    length = vip[i] - vip[i - 1] - 1
    answer = answer * dp[length]

print(answer)