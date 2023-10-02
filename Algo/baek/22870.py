from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

def dijkstra(start):
    pq = []
    heappush(pq, (0, start))
    dist = [INF] * (n + 1)
    dist[start] = 0
    while pq:
        d, curr = heappop(pq)
        if dist[curr] < d:
            continue

        for next, nd in graph[curr]:
            if visited[next]:
                continue
            if dist[next] > dist[curr] + nd:
                dist[next] = dist[curr] + nd
                heappush(pq, (dist[next], next))
    return dist

INF = 1e10
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

# 양방향 그래프
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 사전순을 위한 정렬
for i in range(n + 1):
    graph[i].sort()

s, e = map(int, input().split())

visited = [False] * (n + 1)
dist_s = dijkstra(s)
dist_e = dijkstra(e)

# 방문 노드 체크
curr = s
while curr != e:
    for next, nd in graph[curr]:
        if dist_s[curr] + nd + dist_e[next] == dist_s[e]:
            visited[next] = True
            curr = next
            break

dist_e = dijkstra(e)
print(dist_s[e] + dist_e[s])