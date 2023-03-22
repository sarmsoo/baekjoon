# bottom-up
'''
n = int(input())
a = list(map(int, input().split()))
dp = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))
'''

# top-down

n = int(input())
a = list(map(int, input().split()))
dp = [0] * n
dp[0] = 1

def sol(i):
    if dp[i] != 0:
        return dp[i]

    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], sol(j))
    dp[i] += 1
    return dp[i]

print(sol(n - 1))