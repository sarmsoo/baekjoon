from sys import stdin
input = stdin.readline
'''
n = int(input())
seq = [0] + list(map(int, input().split()))
dp = [[0, 0] for _ in range(n + 1)]

flag = False
for i in range(1, n + 1):
    if seq[i] < 0:
        if dp[i - 1][0] + seq[i] > 0:
            dp[i][0] = dp[i - 1][0] + seq[i]
            dp[i][1] = dp[i - 1][1]

        else:
            dp[i][0] = 0
            dp[i][1] = dp[i - 1][1]

    else:
        flag = True
        dp[i][0] = dp[i - 1][0] + seq[i]
        if dp[i][0] > dp[i - 1][1]:
            dp[i][1] = dp[i][0]
        else:
            dp[i][1] = dp[i - 1][1]

if flag:
    print(max(dp[n]))
else:
    print(max(seq[1:]))
'''
'''
n = int(input())
seq = list(map(int, input().split()))

tmp = 0
answer = -1001
for i in range(n):
    tmp += seq[i]
    if tmp < 0:
        tmp = 0
    else:
        answer = max(answer, tmp)

print(max(answer, max(seq)))
'''

n = int(input())
seq = list(map(int, input().split()))

for i in range(1, n):
    seq[i] = max(seq[i], seq[i - 1] + seq[i])

print(max(seq))