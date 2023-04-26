from sys import stdin
from sys import maxsize
input = stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))
front, back = 0, 0
sum = nums[0]
answer = maxsize
while True:
    if sum >= s and front == n - 1:
        print(answer)
        break

    if sum >= s:
        if back == front:
            print(1)
            break

        answer = min(answer, front - back + 1)
        if sum - nums[back] >= s:
            sum -= nums[back]
            back += 1
        else:
            front += 1
            if front <= n - 1:
                sum += nums[front]
            else:
                print(answer)
                break

    else:
        front += 1
        sum += nums[front]