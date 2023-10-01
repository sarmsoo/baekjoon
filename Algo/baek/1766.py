from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

def topology_sort():
    pq = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            heappush(pq, i)
    result = []
    while pq:
        curr = heappop(pq)
        result.append(curr)

        for next in graph[curr]:
            indegree[next] -= 1
            if indegree[next] == 0:
                heappush(pq, next)
    return result


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

print(*topology_sort())