from sys import stdin
from collections import deque
input = stdin.readline

k = int(input())
m, n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dy = [1, -1, 0, 0, 2, 2, -2, -2, 1, 1, -1, -1]
dx = [0, 0, 1, -1, 1, -1, 1, -1, 2, -2, 2, -2]

def bfs():
    q = deque([(0, 0, 2)])
    visited[0][0] = 2
    answer = 0
    while q:
        for _ in range(len(q)):
            y, x, t = q.popleft()
            if y == n - 1 and x == m - 1:
                return answer

            if t < k + 2:
                for i in range(4, 12):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if ny < 0 or ny >= n or nx < 0 or nx >= m:
                        continue
                    if (visited[ny][nx] == 0 or visited[ny][nx] > t + 1) and graph[ny][nx] == 0:
                        q.append((ny, nx, t + 1))
                        visited[ny][nx] = t + 1

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or ny >= n or nx < 0 or nx >= m:
                    continue
                if (visited[ny][nx] == 0 or visited[ny][nx] > t) and graph[ny][nx] == 0:
                    q.append((ny, nx, t))
                    visited[ny][nx] = t

        answer += 1
    return -1

print(bfs())