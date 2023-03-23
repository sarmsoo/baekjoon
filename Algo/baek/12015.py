from bisect import bisect_left

n = int(input())
seq = list(map(int, input().split()))
dp = []

for num in seq:
    k = bisect_left(dp, num) # bisect_right로 하면 답 안나옴.

    if len(dp) == k:
        dp.append(num)
    else:
        dp[k] = num

print(len(dp))