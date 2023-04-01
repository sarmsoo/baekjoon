from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(i, j):
    q = deque([(i, j)])
    visited[i][j] = True
    cnt = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if visited[ny][nx] or graph[ny][nx] == 0:
                continue
            q.append((ny, nx))
            visited[ny][nx] = True
            cnt += 1
    return cnt

answer1 = 0
answer2 = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            answer1 += 1
            answer2 = max(answer2, bfs(i, j))

print(answer1)
print(answer2)