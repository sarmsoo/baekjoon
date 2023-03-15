import sys

input = sys.stdin.readline

n = int(input())
visited = [False] * n
graph = [list(map(int, input().split())) for _ in range(n)]


def dfs(v):
    for j in range(n):
        if not visited[j] and graph[v][j] == 1:
            visited[j] = True
            dfs(j)


for i in range(n):
    dfs(i)
    for j in range(n):
        if visited[j]:
            print(1, end='')
        else:
            print(0, end='')
    print()
    visited = [False] * n
