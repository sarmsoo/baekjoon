from sys import stdin
input = stdin.readline

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
L = list(map(int, input().split()))

max_ = max(max(A), max(L))
dp = [0] * (max_ + 1)
for a in A:
    dp[a] += 1

for i in range(1, max_ + 1):
    if not dp[i]:
        continue

    for j in range(2, max_ + 1):
        if i * j > max_:
            break
        dp[i * j] += dp[i]

answer = []
for i in L:
    answer.append(dp[i])

print(*answer)