# bfs
'''
from sys import stdin
from collections import deque
input = stdin.readline

def bfs(start, end):
    q = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True
    while q:
        curr = q.popleft()
        if curr == end:
            return True

        for next in range(1, n + 1):
            if graph[curr - 1][next - 1] == 0:
                continue
            if visited[next]:
                continue
            q.append(next)
            visited[next] = True

    return False


n = int(input())
m = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
travel = list(map(int, input().split()))

for i in range(m - 1):
    if not bfs(travel[i], travel[i + 1]):
        print("NO")
        exit(0)
print("YES")
'''
# union find
from sys import stdin
input = stdin.readline

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


n = int(input())
m = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
travel = list(map(int, input().split()))

parent = [i for i in range(n + 1)]
for i in range(n):
    for j in range(i + 1, n):
        if graph[i][j]:
            union(i + 1, j + 1)

root = find(travel[0])
for i in range(1, m):
    if find(travel[i]) != root:
        print("NO")
        exit(0)
print("YES")