import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# graph안 list 정렬
for i in range(1, n + 1):
    graph[i].sort()

def dfs(s):
    stack = [s]
    visited = []
    result = []
    while stack:
        curr = stack.pop()
        if curr not in visited:
            visited.append(curr)
            result.append(curr)
            for adj in graph[curr][::-1]:
                if adj not in visited:
                    stack.append(adj)
    return result

def bfs(s):
    q = deque([s])
    visited = [s]
    result = []
    while q:
        curr = q.popleft()
        result.append(curr)
        for adj in graph[curr]:
            if adj not in visited:
                visited.append(adj)
                q.append(adj)
    return result

print(*dfs(v))
print(*bfs(v))