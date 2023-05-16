from sys import stdin
input = stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))
dp = [[0, []] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, i):
        if arr[i] > arr[j] and dp[i][0] < dp[j][0]:
            dp[i][0] = dp[j][0]
            dp[i][1] = dp[j][1][:] # deepcopy()보다는 slicing
    dp[i][0] += 1
    dp[i][1].append(arr[i])

tmp = 0
result = 0
for i in range(1, n + 1):
    if dp[i][0] > tmp:
        tmp = dp[i][0]
        result = i

print(dp[result][0])
print(*dp[result][1])

'''
n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
        dp[i] += 1
        
print(max(dp))

k = max(dp)
result = []
for i in range(n - 1, -1, -1):
    if dp[i] == k:
        result.append(k)
        k -= 1

result.reverse()
print(*result)
'''