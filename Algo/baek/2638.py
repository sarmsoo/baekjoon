from sys import stdin
from collections import deque
input = stdin.readline

def bfs():
    q = deque([(0, 0)])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if visited[ny][nx]:
                continue

            if graph[ny][nx] >= 1:
                graph[ny][nx] += 1
            else:
                q.append((ny, nx))
                visited[ny][nx] = True


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

time = 0
while True:
    bfs()
    flag = False
    for i in range(n):
        for j in range(m):
            if graph[i][j] >= 3:
                graph[i][j] = 0
                flag = True
            elif graph[i][j] == 2:
                graph[i][j] = 1
    if flag:
        time += 1
    else:
        break

print(time)