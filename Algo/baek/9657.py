n = int(input())

# 1: 상근 승
# 2: 창영 승
dp = [0] * 1001
dp[1] = 1
dp[2] = 2
dp[3] = 1
dp[4] = 1

for i in range(5, n + 1):
    if dp[i - 4] == 2 or dp[i - 3] == 2 or dp[i - 1] == 2:
        dp[i] = 1
    else:
        dp[i] = 2

if dp[n] == 1:
    print("SK")
else:
    print("CY")