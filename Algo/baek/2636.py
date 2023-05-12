from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs():
    q = deque()
    visited = [[False] * m for _ in range(n)]
    tmp_q = deque([(0, 0)])
    visited[0][0] = True
    while tmp_q:
        y, x = tmp_q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if visited[ny][nx]:
                continue
            if graph[ny][nx] == 1:
                q.append((ny, nx))
                visited[ny][nx] = True
            else:
                tmp_q.append((ny, nx))
                visited[ny][nx] = True

    return q

time = 0
prev_cheese = 0
while True:
    q = bfs()
    if not q:
        break
    else:
        prev_cheese = len(q)
        time += 1
        while q:
            y, x = q.popleft()
            graph[y][x] = 0

print(time)
print(prev_cheese)