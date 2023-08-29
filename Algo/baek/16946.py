from sys import stdin
from collections import deque
input = stdin.readline

def bfs(r, c):
    q = deque([(r, c)])
    visited[r][c] = True
    cnt = 0
    adj = set()
    while q:
        y, x = q.popleft()
        cnt += 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if visited[ny][nx]:
                continue
            if graph[ny][nx]:
                adj.add((ny, nx))
                continue
            q.append((ny, nx))
            visited[ny][nx] = True

    for y, x in adj:
        graph[y][x] += cnt
    return


n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and not visited[i][j]:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        graph[i][j] %= 10

for row in graph:
    print(''.join(list(map(str, row))))