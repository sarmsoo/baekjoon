from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

q = deque(range(1, n + 1))


answer = 0
for i in range(len(arr)):
    if arr[i] == q[0]:
        q.popleft()
        continue
    index = q.index(arr[i])
    if index <= len(q) // 2:
        for _ in range(index):
            tmp = q.popleft()
            q.append(tmp)
        q.popleft()
        answer += index
    else:
        answer += len(q) - index
        for _ in range(len(q) - index - 1):
            tmp = q.pop()
            q.appendleft(tmp)
        q.pop()

print(answer)