from sys import stdin
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

answer = 0
for i in range(n):
    left, right = 0, n - 1
    if left == i:
        left += 1
    if right == i:
        right -= 1

    while left < right:
        sum = arr[left] + arr[right]
        if arr[i] == sum:
            answer += 1
            break
        elif arr[i] > sum:
            left += 1
            if left == i:
                left += 1
        else:
            right -= 1
            if right == i:
                right -= 1

print(answer)