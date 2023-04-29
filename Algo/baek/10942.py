from sys import stdin
input = stdin.readline

n = int(input())
nums = [0] + list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if nums[i] == nums[j]:
            if i == j:
                dp[i][j] = 1

            elif i - j == 1:
                if nums[i] == nums[j]:
                    dp[i][j] = 1

            else:
                if dp[i - 1][j + 1] == 1:
                    dp[i][j] = 1

for _ in range(int(input())):
    j, i = map(int, input().split())
    print(dp[i][j])