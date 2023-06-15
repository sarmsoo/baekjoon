from sys import stdin
from collections import deque
input = stdin.readline

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(i, j):
    q = deque([(i, j)])
    visited[i][j] = True
    cnt = 1
    sum = graph[i][j]
    tmp = [(i, j)]
    flag = False
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if visited[ny][nx]:
                continue
            if l <= abs(graph[ny][nx] - graph[y][x]) <= r:
                sum += graph[ny][nx]
                cnt += 1
                q.append((ny, nx))
                tmp.append((ny, nx))
                visited[ny][nx] = True
                flag = True

    v = sum // cnt
    for y, x in tmp:
        graph[y][x] = v

    return flag

answer = 0
while True:
    flag = False
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue

            flag = max(bfs(i, j), flag)

    if flag:
        visited = [[False] * n for _ in range(n)]
        answer += 1
    if not flag:
        print(answer)
        break