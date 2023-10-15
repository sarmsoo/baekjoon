from sys import stdin
input = stdin.readline

def dfs(start):
    stack = [start]
    visited[start] = 0
    while stack:
        curr = stack.pop()

        for next, weight in graph[curr]:
            if visited[next] != -1:
                continue
            stack.append(next)
            visited[next] = visited[curr] + weight


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

visited = [-1] * (n + 1)
dfs(1)

start = visited.index(max(visited))

visited = [-1] * (n + 1)
dfs(start)

print(max(visited))