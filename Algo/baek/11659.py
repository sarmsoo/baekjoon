from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

table = [0]
sum_ = 0
for i in range(n):
    sum_ += nums[i]
    table.append(sum_)

for _ in range(m):
    i, j = map(int, input().split())
    print(table[j] - table[i - 1])