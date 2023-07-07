from sys import stdin
from collections import deque
input = stdin.readline

def bfs(virus):
    q = deque(virus)
    visited = [[-1] * n for _ in range(n)]
    for i, j in virus:
        visited[i][j] = 0
    time = 1
    while q:
        for _ in range(len(q)):
            y, x = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or ny >= n or nx < 0 or nx >= n:
                    continue
                if visited[ny][nx] != -1 or graph[ny][nx] == 1:
                    continue
                q.append((ny, nx))
                visited[ny][nx] = time
        time += 1

    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1 and graph[i][j] != 1:
                return 2500
    return time - 2

def sol(depth, start):
    global answer
    if depth == m:
        answer = min(answer, bfs(virus))
        return

    for i in range(start, len(arr)):
        y, x = arr[i]
        virus.append((y, x))

        sol(depth + 1, i + 1)

        virus.pop()

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

arr = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            arr.append((i, j))

answer = 2500
virus = []
sol(0, 0)
print(answer if answer != 2500 else -1)