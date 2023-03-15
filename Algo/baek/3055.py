from sys import stdin
from collections import deque
input = stdin.readline

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
def bfs():
    q = deque()
    visited = [[False] * c for _ in range(r)]
    water = deque()
    # 초기 시작점, 물 찾기
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'S':
                q.append((i, j))
                visited[i][j] = True
            if graph[i][j] == '*':
                water.append((i, j))
    times = 1
    while q:
        # 물 이동
        for _ in range(len(water)):
            w_y, w_x = water.popleft()
            for i in range(4):
                w_ny = w_y + dy[i]
                w_nx = w_x + dx[i]
                if w_nx < 0 or w_nx >= c or w_ny < 0 or w_ny >= r or graph[w_ny][w_nx] == '*':
                    continue
                if graph[w_ny][w_nx] == '.' or graph[w_ny][w_nx] == 'S':
                    graph[w_ny][w_nx] = '*'
                    water.append((w_ny, w_nx))

        for _ in range(len(q)):
            y, x = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if nx < 0 or nx >= c or ny < 0 or ny >= r or visited[ny][nx]:
                    continue
                # 비버집 도착
                if graph[ny][nx] == 'D':
                    return times
                if graph[ny][nx] == '.':
                    visited[ny][nx] = True
                    q.append((ny, nx))
        times += 1
    return 'KAKTUS'

r, c = map(int, input().split())
graph = [list(map(str, input().strip())) for _ in range(r)]

print(bfs())