from sys import stdin
input = stdin.readline

n, l = map(int, input().split())
water = list(map(int, input().split()))
water.sort()
start = water[0]
end = start + l
count = 1
for i in range(n):
    if start <= water[i] < end:
        continue
    else:
        start = water[i]
        end = start + l
        count += 1
print(count)

