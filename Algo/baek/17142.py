from sys import stdin
from collections import deque
input = stdin.readline

def bfs(tmp):
    q = deque(tmp)
    visited = [[-1] * n for _ in range(n)]
    for y, x in q:
        visited[y][x] = 0
    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            # 방문 or 벽
            if visited[ny][nx] != -1 or graph[ny][nx] == 1:
                continue
            q.append((ny, nx))
            visited[ny][nx] = visited[y][x] + 1

    # 바이러스 확산 후
    time = 0
    for i in range(n):
        for j in range(n):
            # 바이러스가 퍼지지 않은 빈 공간 존재
            if visited[i][j] == -1 and graph[i][j] == 0:
                return 1e12
            # 바이러스가 퍼진 빈 공간에서 max값
            if visited[i][j] != -1 and graph[i][j] == 0:
                time = max(time, visited[i][j])
    return time

def sol(depth, start):
    global answer
    if depth == m:
        answer = min(answer, bfs(tmp))
        return

    for i in range(start, len(arr)):
        tmp.append(arr[i])

        sol(depth + 1, i + 1)

        tmp.pop()


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
arr = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            arr.append((i, j))

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

tmp = []
answer = 1e12
sol(0, 0)

print(answer if answer != 1e12 else -1)