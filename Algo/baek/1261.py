from sys import stdin, maxsize
from heapq import heappush, heappop
input = stdin.readline

# dijkstra
def dijkstra():
    pq = []
    dist[0][0] = 0
    heappush(pq, (0, 0, 0))
    while pq:
        d, y, x = heappop(pq)
        if dist[y][x] < d:
            continue
        if y == n - 1 and x == m - 1:
            return

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if dist[ny][nx] > dist[y][x] + graph[ny][nx]:
                dist[ny][nx] = dist[y][x] + graph[ny][nx]
                heappush(pq, (dist[ny][nx], ny, nx))


INF = maxsize
m, n = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

dist = [[INF] * m for _ in range(n)]

dijkstra()
print(dist[n - 1][m - 1])

# bfs
from collections import deque

dist = [[-1] * m for _ in range(n)]

def bfs():
    q = deque([(0, 0)])
    dist[0][0] = 0
    while q:
        y, x = q.popleft()
        if y == n - 1 and x == m - 1:
            return

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if dist[ny][nx] != -1:
                continue
            if graph[ny][nx] == 1:
                dist[ny][nx] = dist[y][x] + 1
                q.append((ny, nx))
            else:
                dist[ny][nx] = dist[y][x]
                q.appendleft((ny, nx))

bfs()
print(dist[n - 1][m - 1])

