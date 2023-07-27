from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

ry, rx, by, bx = 0, 0, 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            ry, rx = i, j
        elif graph[i][j] == 'B':
            by, bx = i, j

q = deque([(ry, rx, by, bx, 1)])
visited = [(ry, rx, by, bx)]

def move(y, x, i, j):
    count = 0
    while graph[y + i][x + j] != '#' and graph[y][x] != 'O':
        y += i
        x += j
        count += 1
    return y, x, count

def bfs():
    while q:
        ry, rx, by, bx, cnt = q.popleft()
        for i in range(4):
            nry, nrx, rcnt = move(ry, rx, dy[i], dx[i])
            nby, nbx, bcnt = move(by, bx, dy[i], dx[i])
            if graph[nby][nbx] == 'O':
                continue
            if graph[nry][nrx] == 'O':
                return cnt
            if nry == nby and nrx == nbx:
                if rcnt > bcnt:
                    nry -= dy[i]
                    nrx -= dx[i]
                else:
                    nby -= dy[i]
                    nbx -= dx[i]
            if (nry, nrx, nby, nbx) not in visited:
                visited.append((nry, nrx, nby, nbx))
                q.append((nry, nrx, nby, nbx, cnt + 1))
    return -1

print(bfs())