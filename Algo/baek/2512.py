from sys import stdin
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

left = 1
right = max(arr)

while left <= right:
    mid = (left + right) // 2
    tmp = 0
    for i in range(n):
        if arr[i] < mid:
            tmp += arr[i]
        else:
            tmp += mid
    if tmp <= m:
        left = mid + 1
    else:
        right = mid - 1

print(right)