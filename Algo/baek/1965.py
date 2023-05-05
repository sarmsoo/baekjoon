from sys import stdin
input = stdin.readline
# bottom-up
'''
n = int(input())
arr =[0] + list(map(int, input().split()))

dp = [0] * (n + 1)
dp[1] = 1

for i in range(2, n + 1):
    tmp = 0
    for j in range(1, i):
        if arr[i] > arr[j]:
            tmp = max(tmp, dp[j])

    dp[i] = tmp + 1

print(max(dp))
'''

# top-down
n = int(input())
arr =[0] + list(map(int, input().split()))

dp = [0] * (n + 1)
dp[1] = 1

def sol(i):
    if dp[i] != 0:
        return dp[i]

    dp[i] = 1
    for j in range(i - 1, 0, -1):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], sol(j) + 1)

    return dp[i]

answer = 0
for i in range(n, 0, -1):
    answer = max(answer, sol(i))

print(answer)