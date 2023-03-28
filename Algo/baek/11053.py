# bottom-up
'''
n = int(input())
a = list(map(int, input().split()))
dp = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))
'''

# top-down

n = int(input())
a = list(map(int, input().split()))
dp = [0] * n
dp[0] = 1

def sol(i):
    if i == 0:
        return 1
    if dp[i] != 0:
        return dp[i]
    dp[i] = 1
    for j in range(i - 1, -1, -1):
        if dp[i] < sol(j) + 1 and a[i] > a[j]:
            dp[i] = sol(j) + 1
    return dp[i]

sol(n - 1)
print(max(dp))
'''
top-down 에서
if a[i] > a[j] and dp[i] < sol(j):
으로 순서 바꾸면 틀림. 굉장히 주의 해야함.
이유는 a[i] > a[j]에서 먼저 조건 판단이 나서 
if 아래의 dp 테이블에 값을 넣지를 못하는 경우가 발생함.
의도적으로 dp[i] < sol(j)를 조건문에서 먼저 적어주면
모든 경우의 dp table이 값이 들어감.
'''