from sys import stdin
from collections import deque
input = stdin.readline

r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
fired = [[False] * c for _ in range(r)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs():
    q = deque()
    fire = deque()

    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'J':
                q.append((i, j))
                visited[i][j] = True
            if graph[i][j] == 'F':
                fire.append((i, j))
                fired[i][j] = True

    time = 0
    while q:
        # 불 번짐
        for _ in range(len(fire)):
            fy, fx = fire.popleft()

            for i in range(4):
                nfy = fy + dy[i]
                nfx = fx + dx[i]

                if nfy < 0 or nfy >= r or nfx < 0 or nfx >= c:
                    continue
                if fired[nfy][nfx] or graph[nfy][nfx] == '#':
                    continue
                graph[nfy][nfx] = 'F'
                fire.append((nfy, nfx))
                fired[nfy][nfx] = True

        # 사람 이동
        for _ in range(len(q)):
            y, x = q.popleft()
            if y < 0 or y >= r or x < 0 or x >= c:
                return time

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or ny >= r or nx < 0 or nx >= c:
                    q.append((ny, nx))
                    break
                if visited[ny][nx]:
                    continue
                if graph[ny][nx] == '#' or graph[ny][nx] == 'F':
                    continue
                q.append((ny, nx))
                visited[ny][nx] = True

        time += 1
    return "IMPOSSIBLE"

print(bfs())