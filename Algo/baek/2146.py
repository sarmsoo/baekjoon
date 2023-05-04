from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs1(y, x):
    global cnt
    q = deque([(y, x)])
    graph[y][x] = cnt
    visited[y][x] = True
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if graph[ny][nx] == 0 or visited[ny][nx]:
                continue

            graph[ny][nx] = cnt
            q.append((ny, nx))
            visited[ny][nx] = True

def bfs2(k):
    check = [[-1] * n for _ in range(n)]
    q = deque()

    for y in range(n):
        for x in range(n):
            if graph[y][x] == k:
                q.append((y, x))
                check[y][x] = 0
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            if graph[ny][nx] > 0 and graph[ny][nx] != k:
                return check[cy][cx]

            if graph[ny][nx] == 0 and check[ny][nx] == -1:
                check[ny][nx] = check[cy][cx] + 1
                q.append((ny, nx))

visited = [[False] * n for _ in range(n)]
cnt = 2
for y in range(n):
    for x in range(n):
        if graph[y][x] == 1 and not visited[y][x]:
            bfs1(y, x)
            cnt += 1

answer = 10 ** 5
for k in range(2, cnt):
    answer = min(answer, bfs2(k))

print(answer)