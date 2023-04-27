from sys import stdin
from sys import maxsize
input = stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))
right, left = 0, 0
sum = nums[0]
answer = maxsize
while True:
    if sum >= s:
        if left == right:
            print(1)
            break
        answer = min(answer, right - left + 1)
        if sum - nums[left] >= s:
            sum -= nums[left]
            left += 1
        else:
            right += 1
            if right <= n - 1:
                sum += nums[right]
            else:
                print(answer)
                break
    else:
        right += 1
        if right <= n - 1:
            sum += nums[right]
        else:
            print(0)
            break