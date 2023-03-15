import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    # 출발 시작점도 세줘야함
    counts = 2
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == 0:
                    continue
                if visited[nx][ny]:
                    continue
                if nx == n - 1 and ny == m - 1:
                    return(counts)
                q.append((nx, ny))
                visited[nx][ny] = True
        counts += 1

print(bfs(0, 0))