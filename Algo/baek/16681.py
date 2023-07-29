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
            # 높아지는 정점으로만
            if not height[next] > height[curr]:
                continue
            if dist[next] > dist[curr] + nd:
                dist[next] = dist[curr] + nd
                heappush(pq, (dist[next], next))
    return dist


INF = maxsize
n, m, d, e = map(int, input().split())
height = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dist_go = dijkstra(1)
dist_come = dijkstra(n)

answer = -INF
for i in range(2, n):
    if dist_go[i] == INF or dist_come[i] == INF:
        continue
    tmp = height[i] * e - (dist_go[i] + dist_come[i]) * d
    answer = max(answer, tmp)

print(answer if answer != -INF else "Impossible")

'''
그래프 입력 받을 때 낮은 곳에서 높은 곳으로 가는 간선만 받아서 평범한 dijkstra로 풀어도됨. 
for i in range(m):
    a, b, c = map(int, input().split())
    if height[a] == height[b] :
        continue
    if height[a] > height[b] :
        a, b = b, a
    graph_go[a].append((b, c))
    graph_come[b].append((a, c))
'''