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


while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break

    parent = [i for i in range(m)]
    edges = []
    answer = 0
    for _ in range(n):
        x, y, z = map(int, input().split())
        answer += z
        edges.append((x, y, z))

    edges.sort(key=lambda x: x[2])

    for a, b, cost in edges:
        if find(a) != find(b):
            answer -= cost
            union(a, b)

    print(answer)

#Prim
from heapq import heappush, heappop, heapify

def prim(start):
    visited = [False] * m
    visited[start] = True
    pq = graph[start]
    heapify(pq)
    result = 0
    while pq:
        cost, curr = heappop(pq)
        if visited[curr]:
            continue

        visited[curr] = True
        result += cost

        for edge in graph[curr]:
            heappush(pq, edge)

    return result


while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    graph = [[] for _ in range(m)]
    answer = 0
    for _ in range(n):
        x, y, z = map(int, input().split())
        answer += z
        graph[x].append((z, y))
        graph[y].append((z, x))

    print(answer - prim(0))