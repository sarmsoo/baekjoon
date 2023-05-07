from sys import stdin
from collections import deque
input = stdin.readline

n, m, p = map(int, input().split())
s = [0] + list(map(int, input().split()))
graph = [list(input().strip()) for _ in range(n)]
queues = [deque() for _ in range(p + 1)]
result = [0] * (p + 1)

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for i in range(n):
    for j in range(m):
        if graph[i][j] != '.' and graph[i][j] != '#':
            result[int(graph[i][j])] += 1
            queues[int(graph[i][j])].append((i, j))

while True:
    flag = False
    for i in range(1, p + 1):
        for _ in range(s[i]):
            if not queues[i]:
                continue

            for _ in range(len(queues[i])):
                y, x = queues[i].popleft()

                for j in range(4):
                    ny = y + dy[j]
                    nx = x + dx[j]
                    if ny < 0 or ny >= n or nx < 0 or nx >= m:
                        continue
                    if graph[ny][nx] == '.':
                        queues[i].append((ny, nx))
                        graph[ny][nx] = str(i)
                        result[i] += 1
                        flag = True
    if not flag:
        break

print(*result[1:])