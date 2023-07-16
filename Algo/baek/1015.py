from sys import stdin
input = stdin.readline

n = int(input())
arr_a = list(map(int, input().split()))

tmp = []
for i in range(n):
    tmp.append([arr_a[i], i])

tmp.sort()
for i in range(n):
    tmp[i] = tmp[i] + [i]

tmp.sort(key=lambda x: x[1])
for i in range(n):
    print(tmp[i][2], end=' ')