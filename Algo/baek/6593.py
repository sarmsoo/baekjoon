import sys
from collections import deque
input = sys.stdin.readline

dy = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs(i, j, k):
    q = deque([(i, j, k)])
    visited[i][j][k] = True
    counts = 1
    while q:
        for _ in range(len(q)):
            z, y, x = q.popleft()
            for index in range(6):
                ny = y + dy[index]
                nx = x + dx[index]
                nz = z + dz[index]
                if ny < 0 or ny >= r or nx < 0 or nx >= c or nz < 0 or nz >= l:
                    continue
                if graph[nz][ny][nx] == '#' or visited[nz][ny][nx]:
                    continue
                if graph[nz][ny][nx] == 'E':
                    return f'Escaped in {counts} minute(s).'
                q.append((nz, ny, nx))
                visited[nz][ny][nx] = True
        counts += 1
    return 'Trapped!'

while True:
    l, r, c = map(int, input().split())
    # stop 조건
    if l == 0 and r == 0 and c == 0:
        break
    # graph
    graph = [[[] for _ in range(r)] for _ in range(l)]
    visited = [[[False] * c for _ in range(r)] for _ in range(l)]
    for i in range(l):
        graph[i] = [list(map(str, input().strip())) for _ in range(r)]
        input()

    # 'S' index 찾기
    flag = False
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if graph[i][j][k] == 'S':
                    print(bfs(i, j, k))
                    flag = True
                    break
            if flag:
                break
        if flag:
            break