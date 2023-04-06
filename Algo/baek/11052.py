from sys import stdin
input = stdin.readline

# bottom-up

n = int(input())
card = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)
dp[1] = card[1]
for i in range(2, n + 1):
    dp[i] = card[i]
    for j in range(1, i):
        dp[i] = max(dp[i], dp[i - j] + card[j])

print(dp[n])

# top-down

def sol(i):
    if dp[i] != 0:
        return dp[i]
    dp[i] = card[i]
    for j in range(i - 1, 0, -1):
        dp[i] = max(dp[i], sol(i - j) + card[j])
    return dp[i]

print(sol(n))