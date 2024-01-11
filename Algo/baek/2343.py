from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = sum(arr)
answer = 0
while left <= right:
    num = m
    mid = (left + right) // 2

    flag = True
    temp = mid
    for i in range(n):
        # 강의 한개가 블루레이 크기보다 클 때
        if arr[i] > mid:
            flag = False
            break
        # 블루레이에 담을 수 있을 때
        if arr[i] <= temp:
            temp -= arr[i]
        # 없을 때
        else:
            # 더 이상 남은 블루레이가 없을 때
            if num == 1:
                flag = False
                break

            num -= 1
            temp = mid - arr[i]

    if flag:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)