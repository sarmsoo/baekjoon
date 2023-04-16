from collections import deque

n, k = map(int, input().split())
visited = [-1] * 100001

def bfs():
    q = deque([n])
    visited[n] = 0
    time = 0
    while q:
        x = q.popleft()
        if x == k:
            return visited[x]
        if 0 <= x - 1 < 100001 and visited[x - 1] == -1:
            q.append(x - 1)
            visited[x - 1] = visited[x] + 1
        if 0 <= 2 * x < 100001 and visited[2 * x] == -1:
            q.appendleft(2 * x)
            visited[2 * x] = visited[x]
        if 0 <= x + 1 < 100001 and visited[x + 1] == -1:
            q.append(x + 1)
            visited[x + 1] = visited[x] + 1

print(bfs())