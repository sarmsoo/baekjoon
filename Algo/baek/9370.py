from sys import stdin
from heapq import heappush, heappop
input = stdin.readline
INF = 1e10

def dijkstra(start):
    pq = []
    dist = [INF] * (n + 1)
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

for _ in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    dest = []
    for _ in range(t):
        x = int(input())
        dest.append(x)

    dist_s = dijkstra(s)
    mid = 0
    if dist_s[g] > dist_s[h]:
        mid = g
    else:
        mid = h

    dist_mid = dijkstra(mid)

    answer = []
    for x in dest:
        if dist_s[x] == dist_s[mid] + dist_mid[x]:
            answer.append(x)

    answer.sort()
    print(*answer)