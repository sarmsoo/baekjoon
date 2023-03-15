from collections import deque
from sys import stdin

input = stdin.readline

m, n, hh = map(int, input().split())
graph = []
for _ in range(hh):
    graph.append(list(list(map(int, input().split())) for _ in range(n)))

dy = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    visited = [[[False] * m for _ in range(n)] for _ in range(hh)]
    q = deque()
    for h in range(hh):
        for i in range(n):
            for j in range(m):
                if graph[h][i][j] == 1:
                    q.append((i, j, h))
                    visited[h][i][j] = True
    counts = -1
    while q:
        for _ in range(len(q)):
            y, x, z = q.popleft()
            for i in range(6):
                ny = y + dy[i]
                nx = x + dx[i]
                nz = z + dz[i]
                if ny < 0 or ny >= n or nx < 0 or nx >= m or nz < 0 or nz >= hh:
                    continue
                if visited[nz][ny][nx]:
                    continue
                if graph[nz][ny][nx] == 0:
                    visited[nz][ny][nx] = True
                    q.append((ny, nx, nz))
                    graph[nz][ny][nx] = 1
        counts += 1

    for h in range(hh):
        for i in range(n):
            for j in range(m):
                if graph[h][i][j] == 0:
                    return -1

    return counts

print(bfs())