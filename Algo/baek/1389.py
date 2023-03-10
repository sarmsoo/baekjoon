from collections import deque
from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start: int, end: int) -> int:
    visited = [False] * (n + 1)
    visited[start] = True
    q = deque([start])
    times = 0
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            if curr == end:
                return times

            for next in graph[curr]:
                if visited[next]:
                    continue
                q.append(next)
        times += 1


result = []
for i in range(1, n + 1):
    temp = 0
    for j in range(1, n + 1):
        if i == j:
            continue
        temp += bfs(i, j)
    result.append((temp, i))

result.sort()

print(result[0][1])