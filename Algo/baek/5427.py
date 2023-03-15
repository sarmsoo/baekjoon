from sys import stdin
from collections import deque
input = stdin.readline

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs():
    # 처음 불, 시작점 찾기
    fire = deque()
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '*':
                fire.append((i, j))
            if graph[i][j] == '@':
                q = deque([(i, j)])
                visited[i][j] = True
    times = 1
    while q:
        # 불 번짐
        for _ in range(len(fire)):
            f_y, f_x = fire.popleft()
            for i in range(4):
                f_ny = f_y + dy[i]
                f_nx = f_x + dx[i]
                if f_ny < 0 or f_ny >= h or f_nx < 0 or f_nx >= w:
                    continue
                if graph[f_ny][f_nx] == '#' or graph[f_ny][f_nx] == '*':
                    continue
                fire.append((f_ny, f_nx))
                graph[f_ny][f_nx] = '*'
        # 이동
        for _ in range(len(q)):
            y, x = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                # 탈출 조건
                if ny < 0 or ny >= h or nx < 0 or nx >= w:
                    return times
                if visited[ny][nx] or graph[ny][nx] != '.':
                    continue
                q.append((ny, nx))
                visited[ny][nx] = True
        times += 1
    return 'IMPOSSIBLE'

t = int(input().rstrip())
for _ in range(t):
    w, h = map(int, input().split())
    graph = [list(map(str, input().strip())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    print(bfs())
