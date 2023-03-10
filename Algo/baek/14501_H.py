from sys import stdin
input = stdin.readline

# top - down
'''
n = int(input())
table = [tuple(map(int, input().split())) for _ in range(n)]

dp = [0] * n
dp.append(0)
for i in range(n - 1, -1, -1):
    t, p = table[i]
    if i + t > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], dp[i + t] + p)

print(dp[0])
'''

# bottom - up

n = int(input())

table = [tuple(map(int, input().split())) for _ in range(n)]
dp = [0] * (n + 1)

for i in range(n):
    for j in range(i + table[i][0], n + 1):
        if dp[j] < dp[i] + table[i][1]:
            dp[j] = dp[i] + table[i][1]

print(dp[-1])