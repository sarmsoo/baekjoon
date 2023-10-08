from sys import stdin
input = stdin.readline

# Kruskal
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m, k = map(int, input().split())
plant = list(map(int, input().split()))
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

edges.sort(key=lambda x: x[2])
parent = [i for i in range(n + 1)]

for p in plant:
    parent[p] = parent[0]

answer = 0
for u, v, w in edges:
    if find(u) != find(v):
        union(u, v)
        answer += w

print(answer)

from sys import stdin
from heapq import heappush, heappop, heapify
input = stdin.readline

# Prim
def prim():
    pq = []
    visited = [False] * (n + 1)
    for p in plant:
        for node, weight in graph[p]:
            heappush(pq, (weight, node))
        visited[p] = True
    answer = 0
    while pq:
        weight, curr = heappop(pq)
        if visited[curr]:
            continue
        answer += weight
        visited[curr] = True

        for next, next_weight in graph[curr]:
            heappush(pq, (next_weight, next))

    return answer


n, m, k = map(int, input().split())
plant = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

print(prim())