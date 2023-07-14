from sys import stdin, maxsize
from heapq import heappush, heappop
input = stdin.readline

def dijkstra(start):
    pq = []
    dist = [INF] * (n + 1)
    dist[start] = 0
    heappush(pq, (0, start))
    while pq:
        d, curr = heappop(pq)
        if dist[curr] < d:
            continue

        for next, nd in graph[curr]:
            if dist[next] > dist[curr] + nd:
                dist[next] = dist[curr] + nd
                heappush(pq, (dist[next], next))
    return dist

INF = maxsize
n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 무방향 그래프
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

dist_1 = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

answer = min(dist_1[v1] + dist_v1[v2] + dist_v2[n],
             dist_1[v2] + dist_v2[v1] + dist_v1[n])
print(answer if answer < maxsize else -1)