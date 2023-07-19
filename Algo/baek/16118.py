from sys import stdin, maxsize
from heapq import heappush, heappop
input = stdin.readline

def dijkstra_fox():
    dist = [INF] * (n + 1)
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
                heappush(pq, (dist[next], next))
    return dist

# dist 2차원으로 해야하나?
def dijkstra_wolf():
    # dist[i][1]: i에서 다음으로 2배 빠르게 갈 수 있을 때
    dist = [[INF] * 2 for _ in range(n + 1)]
    pq = []
    heappush(pq, (0, 1, 1))
    dist[1][1] = 0
    while pq:
        d, curr, is_runnable = heappop(pq)
        if dist[curr][is_runnable] < d:
            continue

        for next, nd in graph[curr]:
            if is_runnable:
                if dist[next][0] > dist[curr][1] + nd / 2:
                    dist[next][0] = dist[curr][1] + nd / 2
                    heappush(pq, (dist[next][0], next, False))
            else:
                if dist[next][1] > dist[curr][0] + 2 * nd:
                    dist[next][1] = dist[curr][0] + 2 * nd
                    heappush(pq, (dist[next][1], next, True))
    return dist


INF = maxsize
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))

dist_fox = dijkstra_fox()
dist_wolf = dijkstra_wolf()
answer = 0
for i in range(1, n + 1):
    if dist_fox[i] < min(dist_wolf[i][0], dist_wolf[i][1]):
        answer += 1

print(answer)