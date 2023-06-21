from sys import stdin
from collections import deque
input = stdin.readline

def clockwise(graph):
    return list(zip(*graph[::-1]))

def bfs(cube):
    global answer
    visited = [[[False] * 5 for _ in range(5)] for _ in range(5)]
    q = deque([(0, 0, 0)])
    visited[0][0][0] = True
    cnt = 0
    while q:
        for _ in range(len(q)):
            y, x, z = q.popleft()
            if y == 4 and x == 4 and z == 4:
                answer = min(answer, cnt)
                return

            for i in range(6):
                ny = y + dy[i]
                nx = x + dx[i]
                nz = z + dz[i]
                if ny < 0 or ny >= 5 or nx < 0 or nx >= 5 or nz < 0 or nz >= 5:
                    continue
                if visited[ny][nx][nz] or cube[ny][nx][nz] == 0:
                    continue
                q.append((ny, nx, nz))
                visited[ny][nx][nz] = True
        cnt += 1

def sol(depth):
    if depth == 5:
        if cube[0][0][0] and cube[4][4][4]:
            bfs(cube)
        if answer == 12:
            print(12)
            exit(0)
        return

    for i in range(5):
        if checked[i]:
            continue
        for _ in range(4):
            graphs[i] = clockwise(graphs[i])
            cube.append(graphs[i])
            checked[i] = True

            sol(depth + 1)

            cube.pop()
            checked[i] = False

graphs = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
cube = []
dy = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
answer = 100
checked = [False] * 5

sol(0)
print(answer if answer < 100 else -1)