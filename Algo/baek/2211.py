from sys import stdin, maxsize
from heapq import heappush, heappop
input = stdin.readline

def dijkstra():
    pq = []
    heappush(pq, (0, 1))
    dist[1] = 0
    while pq:
        d, curr = heappop(pq)
        if dist[curr] < d:
            continue

        for next, nd in graph[curr]:
            if dist[next] > dist[curr] + nd:
                dist[next] = dist[curr] + nd
                prev[next] = curr
                heappush(pq, (dist[next], next))


INF = maxsize
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dist = [INF] * (n + 1)
prev = [0] * (n + 1)

dijkstra()
result = []
for i in range(1, n + 1):
    if prev[i] != 0:
        result.append((i, prev[i]))

print(len(result))
for e in result:
    print(*e)