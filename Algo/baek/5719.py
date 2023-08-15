from sys import stdin, maxsize
from heapq import heappush, heappop
from collections import deque
input = stdin.readline
INF = maxsize

def dijkstra():
    pq = []
    dist = [INF] * n
    heappush(pq, (0, s))
    dist[s] = 0
    while pq:
        curr_cost, curr = heappop(pq)
        if dist[curr] < curr_cost:
            continue
        if curr == d:
            return dist
        for next, next_cost in graph[curr]:
            if checked[curr][next]:
                continue
            if dist[next] > dist[curr] + next_cost:
                dist[next] = dist[curr] + next_cost
                heappush(pq, (dist[next], next))
    return dist

def bfs():
    q = deque([d])
    while q:
        curr = q.popleft()
        if curr == s:
            continue
        for next, next_cost in graph_inverse[curr]:
            if not dist[next] + next_cost == dist[curr]:
                continue
            # 체크 안해주니깐 메모리초과랑 시간초과 나오는데
            # 왜그런지 생각해보자
            if checked[next][curr]:
                continue
            q.append(next)
            checked[next][curr] = True


while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    s, d = map(int, input().split())

    graph = [[] for _ in range(n)]
    graph_inverse = [[] for _ in range(n)]
    checked = [[False] * n for _ in range(n)]
    for _ in range(m):
        u, v, p = map(int, input().split())
        graph[u].append((v, p))
        graph_inverse[v].append((u, p))

    dist = dijkstra()

    if dist[d] == -1:
        print(-1)
        continue

    bfs()
    dist = dijkstra()
    print(dist[d] if dist[d] != INF else -1)