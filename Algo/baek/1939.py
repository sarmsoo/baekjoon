from sys import stdin
from collections import deque
input = stdin.readline

def bfs(mid):
    q = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True
    while q:
        curr = q.popleft()
        if curr == end:
            return True

        for next, next_limit in graph[curr]:
            if visited[next] or next_limit < mid:
                continue
            visited[next] = True
            q.append(next)
    return False


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
start, end = map(int, input().split())

left, right = 1, 1000000000
answer = 0
while left <= right:
    mid = (left + right) // 2
    if bfs(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)