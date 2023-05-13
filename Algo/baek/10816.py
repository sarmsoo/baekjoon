from sys import stdin
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
num = list(map(int, input().split()))
dm = dict()

for i in range(n):
    dm[arr[i]] = dm.get(arr[i], 0) + 1

result = []
for i in range(m):
    result.append(dm.get(num[i], 0))

print(*result)