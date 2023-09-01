from sys import stdin
from heapq import heappush, heappop, heapify
input = stdin.readline

# MST by Prim

def prim(start):
    visited = [False] * (n + 1)
    visited[start] = True
    pq = graph[start]
    heapify(pq)
    answer = 0
    while pq:
        weight, u = heappop(pq)
        if visited[u]:
            continue

        visited[u] = True
        answer += weight

        for edge in graph[u]:
            heappush(pq, edge)

    return answer


n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

print(prim(1))