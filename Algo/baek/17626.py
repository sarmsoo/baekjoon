# bottom-up

from math import sqrt

n = int(input())

dp = [0] * (n + 1)
dp[0] = 0
dp[1] = 1

for i in range(2, n + 1):
    min_ = 4
    for j in range(int(sqrt(i)), 0, -1):
        if j ** 2 > i:
            break
        min_ = min(min_, dp[i - j ** 2])
    dp[i] = min_ + 1

print(dp[n])