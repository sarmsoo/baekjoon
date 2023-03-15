import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input().rstrip())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]


def dfs(i, j, t):
    if i < 0 or i >= n or j < 0 or j >= n or visited[i][j]:
        return
    if graph[i][j] <= t:
        return
    visited[i][j] = True

    dfs(i + 1, j, t)
    dfs(i - 1, j, t)
    dfs(i, j + 1, t)
    dfs(i, j - 1, t)

t = 0
count = 1
result = []
while count:
    count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > t and not visited[i][j]:
                dfs(i, j, t)
                count += 1
    result.append(count)
    visited = [[False] * n for _ in range(n)]
    t += 1

print(max(result))
