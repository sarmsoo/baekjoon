from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)
input = stdin.readline

def dfs(curr):
    visited[curr] = True
    dp[curr][0] = 0
    dp[curr][1] = 1

    for next in graph[curr]:
        if visited[next]:
            continue
        dfs(next)
        dp[curr][1] += min(dp[next][0], dp[next][1])
        dp[curr][0] += dp[next][1]


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [[0, 0] for _ in range(n + 1)]
visited = [False] * (n + 1)

dfs(1)
print(min(dp[1][0], dp[1][1]))