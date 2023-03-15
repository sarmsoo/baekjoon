from sys import stdin
from collections import deque
input = stdin.readline

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs():
    visited = [[False] * m for _ in range(n)]
    q = deque()
    times = -1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                q.append((i, j))
                visited[i][j] = True
    while q:
        for _ in range(len(q)):
            y, x = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or ny >= n or nx < 0 or nx >= m:
                    continue
                if graph[ny][nx] == 0:
                    graph[ny][nx] = 2
                    q.append((ny, nx))
                    visited[ny][nx] = True
        times += 1
    return times


m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

answer = bfs()
flag = False
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            answer = -1
            break
    if flag:
        break
print(answer)