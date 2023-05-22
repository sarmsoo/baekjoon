from sys import stdin
input = stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

dp = [1] * n

# 증가하는 수열은 안 바꿔도됨. 따라서 lis를 구해서 총 길이에서 빼주면 됨.
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))