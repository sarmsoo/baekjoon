from sys import stdin
from heapq import heappush, heappop
input = stdin.readline
INF = 1e10

def dijkstra(start):
    pq = []
    dist[start] = 0
    heappush(pq, (0, start))
    while pq:
        d, curr = heappop(pq)
        if dist[curr] < d:
            continue
        if curr == end:
            return

        for next, nd in graph[curr]:
            if dist[next] > dist[curr] + nd:
                dist[next] = dist[curr] + nd
                heappush(pq, (dist[next], next))
                prev[next] = curr


n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

dist = [INF] * (n + 1)
prev = [0] * (n + 1)
dijkstra(start)

path = [end]
now = end
while now != start:
    path.append(prev[now])
    now = prev[now]

print(dist[end])
print(len(path))
print(*reversed(path))