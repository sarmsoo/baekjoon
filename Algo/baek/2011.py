from sys import stdin
input = stdin.readline

nums = [0] + list(map(int, list(input().strip())))
n = len(nums) - 1

dp = [[0] * 2 for _ in range(n + 1)]
dp[0][0] = 1
dp[1][0] = 1

if nums[1] == 0:
    print(0)
    exit(0)

for i in range(2, n + 1):
    if nums[i] != 0:
        if nums[i - 1] == 1:
            dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) % 1000000
            dp[i][1] = (dp[i - 2][0] + dp[i - 2][1]) % 1000000
        elif nums[i - 1] == 2:
            if 0 <= nums[i] <= 6:
                dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) % 1000000
                dp[i][1] = (dp[i - 2][0] + dp[i - 2][1]) % 1000000
            else:
                dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) % 1000000

        else:
            dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) % 1000000

    else:
        if nums[i - 1] == 1 or nums[i - 1] == 2:
            dp[i][1] = (dp[i - 2][0] + dp[i - 2][1]) % 1000000
        else:
            print(0)
            exit(0)

print(sum(dp[n]) % 1000000)