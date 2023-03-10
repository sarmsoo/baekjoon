# top-down

from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10 ** 5)
input = stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
coins = set(coins)
min_coin = min(coins)

dp = [0] * (k + 1)
for coin in coins:
    if coin > k:
        continue
    dp[coin] = 1

if k < min_coin:
    print(-1)
    exit(0)


def sol(i):
    if dp[i] != 0:
        return dp[i]
    min_ = k + 1
    for coin in coins:
        if i - coin < min_coin:
            continue
        min_ = min(min_, sol(i - coin))
    dp[i] = min_ + 1
    return dp[i]

ans = sol(k)
if ans > k:
    print(-1)
else:
    print(ans)
# print(sol(k))




