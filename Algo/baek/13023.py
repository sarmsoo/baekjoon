from sys import stdin
input = stdin.readline

def sol(curr, depth):
    if depth == 5:
        print(1)
        exit(0)

    for next in graph[curr]:
        if visited[next]:
            continue
        visited[next] = True

        sol(next, depth + 1)

        visited[next] = False


n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * n

for curr in range(n):
    visited[curr] = True
    sol(curr, 1)
    visited[curr] = False

print(0)