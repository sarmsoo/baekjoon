from sys import stdin
input = stdin.readline

def find(x):
    if parent[x][0] != x:
        return find(parent[x][0])
    return x

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if parent[a][1] < parent[b][1]:
        parent[a][0] = b
        parent[b][1] = parent[a][1] + parent[b][1]
    else:
        parent[b][0] = a
        parent[a][1] = parent[a][1] + parent[b][1]


for _ in range(int(input())):
    f = int(input())
    parent = dict()
    for _ in range(f):
        a, b = input().split()
        if a not in parent:
            parent[a] = [a, 1]
        if b not in parent:
            parent[b] = [b, 1]
        union(a, b)
        print(parent[find(a)][1])