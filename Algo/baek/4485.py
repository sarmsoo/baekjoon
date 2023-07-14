from sys import stdin, maxsize
from heapq import heappush, heappop
input = stdin.readline

def dijkstra():
    pq = []
    dist[0][0] = graph[0][0]
    heappush(pq, (graph[0][0], 0, 0))
    while pq:
        d, y, x = heappop(pq)
        if dist[y][x] < d:
            continue

        if y == n - 1 and x == n - 1:
            return

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if dist[ny][nx] > dist[y][x] + graph[ny][nx]:
                dist[ny][nx] = dist[y][x] + graph[ny][nx]
                heappush(pq, (dist[ny][nx], ny, nx))


INF = maxsize
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

i = 1
while True:
    n = int(input())
    if n == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(n)]
    dist = [[INF] * n for _ in range(n)]

    dijkstra()
    print(f"Problem {i}: {dist[n - 1][n - 1]}")
    i += 1