from sys import stdin
from copy import deepcopy
input = stdin.readline

def cctv_1(y: int, x: int, id: int, mod: int, back: bool) -> None:
    while True:
        y += dy[mod]
        x += dx[mod]
        if y < 0 or y >= n or x < 0 or x >= m:
            return
        if graph[y][x] == 6:
            return
        if visited[y][x]:
            continue
        if not back and graph[y][x] >= 0:
            graph[y][x] += id + 6
        elif back and graph[y][x] > 0:
            graph[y][x] -= id + 6

def cctv_2(y: int, x: int, id: int, mod: int, back: bool) -> None:
    cctv_1(y, x, id, mod, back)
    cctv_1(y, x, id, (mod + 2) % 4, back)

def cctv_3(y: int, x: int, id: int, mod: int, back: bool) -> None:
    cctv_1(y, x, id, mod, back)
    cctv_1(y, x, id,(mod + 1) % 4, back)

def cctv_4(y: int, x: int, id: int, mod: int, back: bool) -> None:
    cctv_1(y, x, id, mod, back)
    cctv_1(y, x, id, (mod + 1) % 4, back)
    cctv_1(y, x, id, (mod + 3) % 4, back)

def cctv_5(y: int, x: int) -> None:
    for i in range(4):
        cctv_1(y, x, 5, i, False)

def cctv_manage(y: int, x: int, id: int, mod: int, back: bool) -> None:
    if id == 1:
        cctv_1(y, x, id, mod, back)
        return
    if id == 2:
        cctv_2(y, x, id, mod, back)
        return
    if id == 3:
        cctv_3(y, x, id, mod, back)
        return
    if id == 4:
        cctv_4(y, x, id, mod, back)
        return

def sol(start: int, cnt: int):
    global answer
    if cnt == len(cctvs):
        tmp = 0
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    tmp += 1
        answer = min(answer, tmp)
        return

    for i in range(start, len(cctvs)):
        y, x, id = cctvs[i]
        for mod in range(4):
            cctv_manage(y, x, id, mod, False)

            sol(i + 1, cnt + 1)

            cctv_manage(y, x, id, mod, True)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

cctvs = []
cctv5s = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 5:
            visited[i][j] = True
            cctv5s.append((i, j))
            continue

        if 1 <= graph[i][j] <= 4:
            cctvs.append((i, j, graph[i][j]))
            visited[i][j] = True

for y, x in cctv5s:
    cctv_5(y, x)

answer = n * m
sol(0, 0)
print(answer)