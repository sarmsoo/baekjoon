# top-down

from sys import setrecursionlimit
setrecursionlimit(10 ** 5)

n = int(input())

dp = [n + 1] * (n + 1)

for i in range(n + 1):
    if i ** 2 > n:
        break
    dp[i ** 2] = 1


def sol(i):
    if dp[i] != n + 1:
        return dp[i]

    for j in range(1, n + 1):
        if i - (j ** 2) < 0:
            break
        dp[i] = min(dp[i], sol(i - j ** 2) + 1)

    return dp[i]


print(sol(n))

# bottom-up
'''
n = int(input())
dp = [n + 1] * (n + 1)

for i in range(1, n + 1):
    if i ** 2 > n:
        break
    dp[i ** 2] = 1

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j ** 2 > i:
            break
        dp[i] = min(dp[i], dp[i - j ** 2] + 1)

print(dp[n])
'''