from sys import stdin
from collections import deque
input = stdin.readline

def topology_sort():
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = build_time[i]
    while q:
        curr = q.popleft()
        if curr == w:
            return

        for i in graph[curr]:
            indegree[i] -= 1
            dp[i] = max(dp[curr] + build_time[i], dp[i])
            if indegree[i] == 0:
                q.append(i)


for _ in range(int(input())):
    n, k = map(int, input().split())
    build_time = [0] + list(map(int, input().split()))

    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1

    w = int(input())

    dp = [0] * (n + 1)
    topology_sort()
    print(dp[w])