from sys import stdin
input = stdin.readline

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[a] = b
    else:
        parent[b] = a

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

edges.sort(key=lambda x: x[2])

mst = []
for a, b, c in edges:
    if find(a) != find(b):
        union(a, b)
        mst.append(c)

print(sum(mst[:-1]))