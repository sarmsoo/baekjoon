from sys import stdin
input = stdin.readline
'''
# bottom-up
n = int(input())
seq = [0] + list(map(int, input().split()))

dp = [0] * (n + 1)
dp[1] = seq[1]
for i in range(2, n + 1):
    dp[i] = seq[i]
    for j in range(1, i):
        if seq[i] > seq[j]:
            dp[i] = max(dp[i], seq[i] + dp[j])

print(max(dp))
'''
# top-down
n = int(input())
seq = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)
dp[1] = seq[1]

def sol(i):
    if dp[i] != 0:
        return dp[i]
    dp[i] = seq[i]
    for j in range(i - 1, 0, -1):
        if dp[i] < sol(j) + seq[i] and seq[i] > seq[j]:
            dp[i] = sol(j) + seq[i]
    return dp[i]

sol(n)
print(max(dp))