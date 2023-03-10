from collections import deque

n, k = map(int, input().split())
dx = [1, -1, 2]

visited = [False] * 200002
q = deque([n])
visited[n] = False
counts = 0
while q:
    for _ in range(len(q)):
        x = q.popleft()
        if x == k:
            print(counts)
            exit(0)
        for i in range(3):
            if i == 2:
                nx = 2 * x
            else:
                nx = x + dx[i]
            if nx < 0 or nx > 200001:
                continue
            if visited[nx]:
                continue
            q.append(nx)
            visited[nx] = True
    counts += 1

print(counts)