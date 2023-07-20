from sys import stdin
from collections import deque
input = stdin.readline

def bfs(r, c):
    visited = [[False] * m for _ in range(n)]
    q = deque([((r, c))])
    visited[r][c] = True
    result = 0
    while q:
        y, x = q.popleft()
        if (y + x) % 2 == 0 and graph[y][x] == 'W':
            result += 1
        elif (y + x) % 2 == 1 and graph[y][x] == 'B':
            result += 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < r or ny >= r + 8 or nx < c or nx >= c + 8:
                continue
            if visited[ny][nx]:
                continue
            q.append((ny, nx))
            visited[ny][nx] = True
    return min(result, 64 - result)


n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

answer = n * m
for i in range(n - 7):
    for j in range(m - 7):
        answer = min(answer, bfs(i, j))

print(answer)