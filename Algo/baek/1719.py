from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

def dijkstra(start):
    pq = []
    heappush(pq, (0, start))
    dist = [INF] * (n + 1)
    dist[start] = 0
    prev = [0] * (n + 1)
    result = ['-'] * n
    while pq:
        d, curr = heappop(pq)
        if dist[curr] < d:
            continue

        for next, nd in graph[curr]:
            if dist[next] > dist[curr] + nd:
                dist[next] = dist[curr] + nd
                heappush(pq, (dist[next], next))
                prev[next] = curr

    for i in range(1, n + 1):
        if i == start:
            continue
        tmp = i
        while prev[tmp] != start:
            tmp = prev[tmp]
        result[i - 1] = tmp

    return result


INF = 1e10
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

answer = []
for i in range(1, n + 1):
    answer.append(dijkstra(i))

for row in answer:
    print(*row)