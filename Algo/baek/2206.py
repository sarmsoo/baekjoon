from sys import stdin
from collections import deque
input = stdin.readline

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
def bfs():
    visited = [[False] * m for _ in range(n)]
    q = deque([(0, 0, 0)])
    visited[0][0] = True
    times = 2
    while q:
        for _ in range(len(q)):
            y, x, z = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                # 끝 지점 도착
                if ny == n - 1 and nx == m - 1:
                    return times
                if ny < 0 or ny >= n or nx < 0 or nx >= m or visited[ny][nx]:
                    continue
                if graph[ny][nx] == '1' and z == 1:
                    continue
                # 벽 한 번도 안깨고 벽 만날 경우
                if graph[ny][nx] == '1' and z == 0:
                    q.append((ny, nx, 1))
                    visited[ny][nx] = True
                    continue

                q.append((ny, nx, z))
                visited[ny][nx] = True
        times += 1
    return -1

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
print(bfs())