from sys import stdin
input = stdin.readline

r, c, t = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(r)]

def spread(arr):
    tmp_a = [[0] * c for _ in range(r)]
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    while arr:
        y, x = arr.pop()
        tmp = 0
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if ny < 0 or ny >= r or nx < 0 or nx >= c:
                continue
            if a[ny][nx] == -1:
                continue
            tmp_a[ny][nx] += a[y][x] // 5
            tmp += a[y][x] // 5
        a[y][x] -= tmp

    for i in range(r):
        for j in range(c):
            a[i][j] += tmp_a[i][j]

def up():
    dy = [0, -1, 0, 1]
    dx = [1, 0, -1, 0]
    y, x = my - 1, mx + 1
    prev = 0
    dir = 0
    while True:
        if y == my - 1 and x == mx:
            return
        ny = y + dy[dir]
        nx = x + dx[dir]
        if ny < 0 or ny >= r or nx < 0 or nx >= c:
            dir += 1
            continue
        a[y][x], prev = prev, a[y][x]
        y, x = ny, nx

def down():
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    y, x = my, mx + 1
    prev = 0
    dir = 0
    while True:
        if y == my and x == mx:
            return
        ny = y + dy[dir]
        nx = x + dx[dir]
        if ny < 0 or ny >= r or nx < 0 or nx >= c:
            dir += 1
            continue
        a[y][x], prev = prev, a[y][x]
        y, x = ny, nx

for _ in range(t):
    arr = []
    my, mx = 0, 0
    for i in range(r):
        for j in range(c):
            if a[i][j] > 0:
                arr.append((i, j))
            elif a[i][j] == -1:
                my = i
                mx = j
    spread(arr)
    up()
    down()

answer = 0
for i in range(r):
    for j in range(c):
        if a[i][j] > 0:
            answer += a[i][j]
print(answer)