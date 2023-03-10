from sys import maxsize
from sys import setrecursionlimit
import time
setrecursionlimit(10 ** 6)
'''
n = int(input())

max_ = maxsize
dp = [max_] * ((10 ** 6) + 1)
dp[1] = 0

for i in range(1, n):
    if i * 3 <= n:
        dp[i * 3] = min(dp[i * 3], dp[i] + 1)
    if i * 2 <= n:
        dp[i * 2] = min(dp[i * 2], dp[i] + 1)

    dp[i + 1] = min(dp[i + 1], dp[i] + 1)

print(dp[n])
'''

# top-down

'''
top-down도 코드 돌아가는거 보면 결국 바텀업으로 간다.
하지만 생각하기가 더 쉽고 코드가 직관적이다.
대신 메모리를 더 사용하고 시간이 더 걸린다.
'''
dp = [-1] * (10 ** 6 + 1)
dp[1] = 0
def to_one(x: int) -> int:
    # 메모이제이션
    if dp[x] != -1:
        return dp[x]

    if x == 1:
        return 0

    dp[x] = 1 + to_one(x - 1)

    if x % 3 == 0:
        dp[x] = min(dp[x], 1 + to_one(x // 3))

    if x % 2 == 0:
        dp[x] = min(dp[x], 1 + to_one(x // 2))

    return dp[x]

def to_one2(x: int) -> int:
    if dp[x] != -1:
        return dp[x]

    if x == 1:
        return 0

    dp[x] = 1 + to_one(x - 1)

    if x % 3 == 0:
        dp[x] = min(dp[x], 1 + dp[x // 3])

    if x % 2 == 0:
        dp[x] = min(dp[x], 1 + dp[x // 2])

    return dp[x]

n = int(input())

print(to_one(n), to_one2(n))