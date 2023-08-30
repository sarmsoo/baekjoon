from sys import stdin
input = stdin.readline

def dfs(start):
    stack = [start] 
    visited[start] = 0
    while stack:
        curr = stack.pop()
        for next, d in graph[curr]:
            if visited[next] != -1:
                continue
            stack.append(next)
            visited[next] = visited[curr] + d


v = int(input())
graph = [[] for _ in range(v + 1)]
for _ in range(v):
    line = list(map(int, input().split()))
    for i in range(1, len(line) - 2, 2):
        graph[line[0]].append((line[i], line[i + 1]))

visited = [-1] * (v + 1)
dfs(1)

start = visited.index(max(visited))

visited = [-1] * (v + 1)
dfs(start)

print(max(visited))