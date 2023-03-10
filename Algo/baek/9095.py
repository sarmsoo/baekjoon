from sys import stdin
input = stdin.readline

# bottom-up
'''
t = int(input())

dp = [-1] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 12):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
for _ in range(t):
    print(dp[int(input())])
'''

# top-down

t = int(input())

dp = [-1] * 12
def sol(x: int) -> int:
    if dp[x] != -1:
        return dp[x]
    if x == 1:
        return 1
    if x == 2:
        return 2
    if x == 3:
        return 4

    dp[x] = sol(x - 1) + sol(x - 2) + sol(x - 3)

    return dp[x]

for t in range(t):
    n = int(input())
    print(sol(n))