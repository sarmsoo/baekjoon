# top-down
'''
n = int(input())

dp = [0] * 1001
dp[1] = 1
dp[2] = 3


def sol(i):
    if dp[i] != 0:
        return dp[i]

    dp[i] = 2 * sol(i - 2) + sol(i - 1)

    return dp[i]


print(sol(n) % 10007)
'''

# bottom-up

n = int(input())

dp = [0] * 1001
dp[1] = 1
dp[2] = 3

for i in range(3, n + 1):
    dp[i] = 2 * dp[i - 2] + dp[i - 1]

print(dp[n])