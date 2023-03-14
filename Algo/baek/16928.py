from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())

ladder_snake = [0] * 101
for _ in range(n):
    x, y = map(int, input().split())
    ladder_snake[x] = y
for _ in range(m):
    u, v = map(int, input().split())
    ladder_snake[u] = v

visited = [False] * 101
q = deque([1])
visited[1] = True
times = 0
while q:
    for _ in range(len(q)):
        curr = q.popleft()
        if curr == 100:
            print(times)
            exit(0)

        for i in range(1, 7):
            next = curr + i
            if next > 100 or visited[next]:
                continue

            visited[next] = True
            while ladder_snake[next] != 0:
                next = ladder_snake[next]
                visited[ladder_snake[next]] = True
            q.append(next)

    times += 1