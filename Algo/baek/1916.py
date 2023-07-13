from sys import stdin, maxsize
from heapq import heappush, heappop
input = stdin.readline

n = int(input())
m = int(input())
INF = maxsize

graph = [[] for _ in range(n + 1)]
dist = [INF] * (n + 1)

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, end = map(int, input().split())

def dijkstra():
    pq = []
    dist[start] = 0
    heappush(pq, (0, start))
    while pq:
        d, curr = heappop(pq)
        if dist[curr] < d:
            continue
        # end 방문 했으면 return
        if curr == end:
            return

        for next, nd in graph[curr]:
            if dist[next] > dist[curr] + nd:
                dist[next] = dist[curr] + nd
                heappush(pq, (dist[next], next))

dijkstra()
print(dist[end])