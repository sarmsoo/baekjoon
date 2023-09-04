from sys import stdin
from collections import deque
input = stdin.readline

def topology_sort():
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    result = []
    while q:
        curr = q.popleft()
        result.append(curr)

        for i in graph[curr]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    return result


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

print(*topology_sort())