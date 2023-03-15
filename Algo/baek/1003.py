"""피보나치 함수"""

t = int(input())
nums = [int(input()) for _ in range(t)]
n = max(nums)
res_0 = [1, 0, 1]
res_1 = [0, 1, 1]
for i in range(3, n + 1):
        res_1.append(res_1[i - 1] + res_1[i - 2])
        res_0.append(res_0[i - 1] + res_0[i - 2])
for num in nums:
    print(res_0[num], res_1[num])

"""DP"""


