from sys import stdin
from collections import deque
input = stdin.readline

def bfs():
    global answer

    visited = [[False] * (m + 2) for _ in range(n + 2)]
    q = deque([(0, 0)])
    visited[0][0] = True
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n + 2 or nx < 0 or nx >= m + 2:
                continue
            if visited[ny][nx] or graph[ny][nx] == '*':
                continue
            # 문
            if 'A' <= graph[ny][nx] <= 'Z':
                if graph[ny][nx].lower() not in keys:
                    continue
            # 열쇠
            if 'a' <= graph[ny][nx] <= 'z' and graph[ny][nx] not in keys:
                keys[graph[ny][nx]] = True
                visited = [[False] * (m + 2) for _ in range(n + 2)]
            # 문서
            if graph[ny][nx] == '$' and (ny, nx) not in visited_doc:
                answer += 1
                visited_doc.append((ny, nx))
            q.append((ny, nx))
            visited[ny][nx] = True


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = ['.' + input() + '.' for _ in range(n)]
    graph = ['.' * (m + 2)] + graph + ['.' * (m + 2)]

    visited_doc = []

    keys = {}
    for i in input():
        if i.isalpha():
            keys[i] = True

    answer = 0
    bfs()
    print(answer)