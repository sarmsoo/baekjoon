from sys import stdin
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))

count = [0] * 1000001
for num in arr:
    count[num] += 1

result = [-1] * n
stack = [0]
for i in range(n):
    while stack and count[arr[stack[-1]]] < count[arr[i]]:
        result[stack.pop()] = arr[i]
    stack.append(i)

print(*result)