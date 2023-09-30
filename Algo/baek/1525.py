from collections import deque

def bfs():
    q = deque([graph])
    visited = dict()
    visited[graph] = 0
    while q:
        curr = q.popleft()
        cnt = visited[curr]
        if curr == answer:
            return cnt

        idx = curr.index('0')
        y = idx // 3
        x = idx % 3
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= 3 or nx < 0 or nx >= 3:
                continue

            nidx = ny * 3 + nx
            next = list(curr)
            next[idx], next[nidx] = next[nidx], next[idx]
            next = ''.join(next)

            if visited.get(next, 0) == 0:
                visited[next] = cnt + 1
                q.append(next)
    return -1


graph = ""
answer = "123456780"

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for _ in range(3):
    row = input().strip().replace(' ', '')
    graph += row

print(bfs())