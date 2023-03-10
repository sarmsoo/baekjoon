from collections import deque
from sys import stdin
input = stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
temp = 0
size = 2
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            start = (i, j)
            graph[i][j] = 0


def bfs():
    global temp
    i, j = start
    q = deque([(i, j)])
    visited[i][j] = True
    times = 0
    while q:
        ry, rx = n, n
        flag = False
        for _ in range(len(q)):
            y, x = q.popleft()
            if graph[y][x] != 0 and graph[y][x] < size:
                if y < ry:
                    ry, rx = y, x
                elif y == ry and x < rx:
                    ry, rx = y, x
                flag = True
                continue

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or ny >= n or nx < 0 or nx >= n:
                    continue
                if visited[ny][nx] or graph[ny][nx] > size:
                    continue
                q.append((ny, nx))
                visited[ny][nx] = True

        if flag:
            temp += 1
            graph[ry][rx] = 0
            return [(ry, rx), times]

        times += 1
    return ["end", times]

result = 0
while True:
    visited = [[False] * n for _ in range(n)]
    search = bfs()
    if search[0] == "end":
        print(result)
        break
    else:
        if temp == size:
            temp = 0
            size += 1
        start = search[0]
        result += search[1]