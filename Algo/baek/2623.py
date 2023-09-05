from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for _ in range(m):
    tmp = list(map(int, input().split()))
    for i in range(1, tmp[0]):
        graph[tmp[i]].append(tmp[i + 1])
        indegree[tmp[i + 1]] += 1

def topology_sort():
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    result = []
    while q:
        curr = q.popleft()
        result.append(curr)
        for next in graph[curr]:
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)
    return result

result = topology_sort()
if len(result) == n:
    for i in result:
        print(i)
else:
    print(0)