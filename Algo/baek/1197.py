from sys import stdin
input = stdin.readline

# Kruskal MST

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

edges.sort(key=lambda x: x[2])

parent = [i for i in range(v + 1)]

answer = 0
for a, b, cost in edges:
    if find(a) != find(b):
        union(a, b)
        answer += cost

print(answer)