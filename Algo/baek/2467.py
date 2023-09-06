from sys import stdin
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))

left, right = 0, n - 1
answer = (0, 1e10)
while left < right:
    sum_ = arr[left] + arr[right]
    if abs(sum(answer)) > abs(sum_):
        answer = (arr[left], arr[right])
        if sum_ == 0:
            break

    if sum_ > 0:
        right -= 1
    else:
        left += 1

print(*answer)