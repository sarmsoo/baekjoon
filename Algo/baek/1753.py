from sys import stdin, maxsize
from heapq import heappush, heappop
input = stdin.readline

def dijkstra(start):
    q = []
    heappush(q, (0, start))
    dist[start] = 0
    while q:
        d, curr = heappop(q)
        if dist[curr] < d: # 방문 체크
            continue

        for nd, next in graph[curr]:
            if dist[next] > dist[curr] + nd:
                dist[next] = dist[curr] + nd
                heappush(q, (dist[next], next))

INF = maxsize
v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v + 1)]
dist = [INF] * (v + 1)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

dijkstra(k)
for i in range(1, v + 1):
    print(dist[i] if dist[i] != INF else "INF")