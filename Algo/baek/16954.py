from sys import stdin
from collections import deque
input = stdin.readline

def bfs():
    q = deque([(7, 0)])
    visited = [[-1] * 8 for _ in range(8)]
    time = 0
    while q:
        for _ in range(len(q)):
            y, x = q.popleft()
            if graph[y][x] == '#':
                continue
            if y == 0 and x == 7:
                return 1

            for i in range(9):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or ny >= 8 or nx < 0 or nx >= 8:
                    continue
                if visited[ny][nx] >= time or graph[ny][nx] == '#':
                    continue
                visited[ny][nx] = time
                q.append((ny, nx))

        for i in range(7, -1, -1):
            for j in range(8):
                if graph[i][j] == '#':
                    if i == 7:
                        graph[i][j] = '.'
                    else:
                        graph[i][j] = '.'
                        graph[i + 1][j] = '#'

        time += 1
    return 0


graph = [list(input().strip()) for _ in range(8)]

dy = [1, -1, 0, 0, 1, 1, -1, -1, 0]
dx = [0, 0, 1, -1, 1, -1, 1, -1, 0]

print(bfs())