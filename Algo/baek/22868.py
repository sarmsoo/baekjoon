from sys import stdin
from collections import deque
input = stdin.readline

def bfs(start, end):
    q = deque([start])
    visited[start] = True
    time = 1
    while q:
        for _ in range(len(q)):
            curr = q.popleft()

            for next in graph[curr]:
                if visited[next]:
                    continue
                prev[next] = curr

                if next == end:
                    return time

                q.append(next)
                visited[next] = True
        time += 1


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    graph[i].sort()

s, e = map(int, input().split())

prev = [0] * (n + 1)
visited = [False] * (n + 1)
answer = bfs(s, e)

visited = [False] * (n + 1)
curr = e
while curr != s:
    visited[curr] = True
    curr = prev[curr]

answer += bfs(e, s)

print(answer)