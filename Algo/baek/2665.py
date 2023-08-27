from sys import stdin
from collections import deque
input = stdin.readline

def bfs():
    global answer
    q = deque([(0, 0, 0)])
    visited = [[1e10] * n for _ in range(n)]
    visited[0][0] = 0
    while q:
        y, x, cnt = q.popleft()
        if y == n - 1 and x == n - 1:
            answer = min(answer, cnt)
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if cnt >= visited[ny][nx]:
                continue
            if graph[ny][nx] == 0:
                visited[ny][nx] = cnt + 1
                q.append((ny, nx, cnt + 1))
            else:
                visited[ny][nx] = cnt
                q.append((ny, nx, cnt))


n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

answer = 1e10
bfs()

print(answer)