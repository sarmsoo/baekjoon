from sys import stdin
from collections import deque
input = stdin.readline

def bfs(r, c, num):
    q = deque([(r, c)])
    visited[r][c] = True
    graph[r][c] = num
    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if visited[ny][nx] or graph[ny][nx] == 0:
                continue
            graph[ny][nx] = num
            q.append((ny, nx))
            visited[ny][nx] = True


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

num = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 or visited[i][j]:
            continue
        num += 1
        bfs(i, j, num)

table = dict()
table[0] = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            table[graph[i][j]] = table.get(graph[i][j], 0) + 1

answer = 0
for y in range(n):
    for x in range(m):
        if graph[y][x] == 0:
            adj = set()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or ny >= n or nx < 0 or nx >= m:
                    continue
                adj.add(graph[ny][nx])

            tmp = 1
            for val in adj:
                tmp += table[val]

            answer = max(answer, tmp)

print(answer)