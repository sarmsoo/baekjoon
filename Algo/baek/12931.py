from sys import stdin
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))

answer = 0
while sum(arr) > 0:
    flag = True
    for i in range(n):
        if arr[i] == 0:
            continue

        if arr[i] % 2 != 0:
            arr[i] -= 1
            answer += 1
            flag = False
            break

    if flag:
        for i in range(n):
            arr[i] = arr[i] // 2
        answer += 1

print(answer)