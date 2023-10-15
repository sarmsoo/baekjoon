from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)
input = stdin.readline

def dfs(curr):
    visited[curr] = True
    for next in graph[curr]:
        if visited[next]:
            continue
        answer[next] = curr
        dfs(next)

n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
answer = [0] * (n + 1)

dfs(1)

for i in range(2, n + 1):
    print(answer[i])