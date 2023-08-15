from sys import stdin
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))

result = [0] * n
for i in range(n):
    cnt = 0
    for j in range(n):
        if result[j] == 0 and cnt == arr[i]:
            result[j] = i + 1
            break
        if result[j] == 0:
            cnt += 1

print(*result)