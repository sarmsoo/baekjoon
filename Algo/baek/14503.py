from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

answer = 0
cy, cx = r, c
while True:
    flag = False
    if graph[cy][cx] == 0:
        graph[cy][cx] = 2
        answer += 1

    for i in range(4):
        ny = cy + dy[i]
        nx = cx + dx[i]
        if graph[ny][nx] == 0:
            flag = True
            break

    if flag:
        while True:
            d = (d - 1) % 4
            ny = cy + dy[d]
            nx = cx + dx[d]
            if graph[ny][nx] == 0:
                cy = ny
                cx = nx
                break
    else:
        ny = cy + dy[(d - 2) % 4]
        nx = cx + dx[(d - 2) % 4]
        if graph[ny][nx] != 1:
            cy = ny
            cx = nx
        else:
            print(answer)
            break