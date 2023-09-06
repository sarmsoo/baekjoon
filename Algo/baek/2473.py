from sys import stdin
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer = [1e10, 0, 0]
for i in range(n - 2):
    left, right = i + 1, n - 1
    while left < right:
        sum_ = arr[i] + arr[left] + arr[right]
        if abs(sum(answer)) > abs(sum_):
            answer = [arr[i], arr[left], arr[right]]
            if sum_ == 0:
                break

        if sum_ > 0:
            right -= 1
        else:
            left += 1

print(*answer)