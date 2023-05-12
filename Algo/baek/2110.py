from sys import stdin
input = stdin.readline

n, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()
length = arr[-1] - arr[0] + 1
max_d = (length - c) // (c - 1) + 1

left, right = 1, max_d
answer = 0
while left <= right:
    mid = (left + right) // 2
    prev = arr[0]
    count = 1

    for i in range(1, n):
        if arr[i] - prev >= mid:
            prev = arr[i]
            count += 1

    if count >= c:
        left = mid + 1
        answer = mid
    else:
        right = mid - 1

print(answer)