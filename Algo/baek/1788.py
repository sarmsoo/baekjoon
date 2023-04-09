n = int(input())

if n == 0:
    print(0)
    print(0)
    exit(0)

flag = False
if n < 0:
    n = -n
    flag = True

dp = [0] * (n + 1)
dp[0] = 0
dp[1] = 1
for i in range(2, n + 1):
    dp[i] = dp[i - 2] % 1000000000 + dp[i - 1] % 1000000000

if flag:
    if n % 2 == 0:
        print(-1)
        print(dp[n] % 1000000000)
    else:
        print(1)
        print(dp[n] % 1000000000)

elif n > 0:
    print(1)
    print(dp[n] % 1000000000)