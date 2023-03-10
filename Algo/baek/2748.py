# top-down
'''
n = int(input())
dp = [-1] * 91
dp[0] = 0
dp[1] = 1
def sol(x: int) -> int:
    # memoization
    if dp[x] != -1:
        return dp[x]

    if x == 0 or x == 1:
        return dp[x]

    dp[x] = sol(x - 2) + sol(x - 1)

    return dp[x]

print(sol(n))
'''

# bottom-up

n = int(input())
dp = [-1] * 91
dp[0] = 0
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])
