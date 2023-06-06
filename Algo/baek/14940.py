from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            graph[i][j] = -1
        elif graph[i][j] == 2:
            q.append((i, j))
            graph[i][j] = 0
            visited[i][j] = True

time = 1
while q:
    for _ in range(len(q)):
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if visited[ny][nx] or graph[ny][nx] == 0:
                continue
            graph[ny][nx] = time
            q.append((ny, nx))
            visited[ny][nx] = True

    time += 1

for i in graph:
    print(*i)