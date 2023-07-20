from sys import stdin, maxsize
from heapq import heappush, heappop
input = stdin.readline

def dijkstra_go(start, end):
    dist = [INF] * (n + 1)
    pq = []
    heappush(pq, (0, start))
    dist[start] = 0
    while pq:
        d, curr = heappop(pq)
        if dist[curr] < d:
            continue
        if curr == end:
            return dist[end]

        for next, nd in graph[curr]:
            if dist[next] > dist[curr] + nd:
                dist[next] = dist[curr] + nd
                heappush(pq, (dist[next], next))

def dijkstra_come(start):
    dist = [INF] * (n + 1)
    pq = []
    heappush(pq, (0, start))
    dist[start] = 0
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
n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dist_go = [0] * (n + 1)
for i in range(1, n + 1):
    dist_go[i] = dijkstra_go(i, x)
dist_come = dijkstra_come(x)

answer = 0
for i in range(1, n + 1):
    answer = max(answer, dist_go[i] + dist_come[i])

print(answer)