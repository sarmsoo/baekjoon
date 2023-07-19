from sys import stdin, maxsize
from heapq import heappush, heappop
input = stdin.readline

def dijkstra():
    pq = []
    heappush(pq, (0, node[1], 1))
    dist[1][node[1]] = 0
    while pq:
        d, cost, curr = heappop(pq)
        if curr == n:
            return d
        if dist[curr][cost] < d:
            continue

        for next, nd in graph[curr]:
            if dist[next][cost] > d + cost * nd:
                dist[next][cost] = d + cost * nd
                heappush(pq, (dist[next][cost], min(cost, node[next]), next))


INF = maxsize
n, m = map(int, input().split())
node = [0] + list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dist = [[INF] * (max(node) + 1) for _ in range(n + 1)]

print(dijkstra())