from sys import stdin
from collections import deque
input = stdin.readline

def find():
    while q:
        y, x = q.popleft()
        if y == l1_y and x == l1_x:
            return True
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= r or nx < 0 or nx >= c:
                continue
            if visited_find[ny][nx]:
                continue
            if graph[ny][nx] == '.':
                q.append((ny, nx))
            else:
                next_q.append((ny, nx))
            visited_find[ny][nx] = True
    return False

def melt():
    while wq:
        y, x = wq.popleft()
        if graph[y][x] == 'X':
            graph[y][x] = '.'
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= r or nx < 0 or nx >= c:
                continue
            if visited_melt[ny][nx]:
                continue
            if graph[ny][nx] == 'X':
                next_wq.append((ny, nx))
            else:
                wq.append((ny, nx))
            visited_melt[ny][nx] = True

r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

q, next_q = deque(), deque()
wq, next_wq = deque(), deque()

visited_find = [[False] * c for _ in range(r)]
visited_melt = [[False] * c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if graph[i][j] == '.':
            wq.append((i, j))
            visited_melt[i][j] = True
        elif graph[i][j] == 'L':
            q.append((i, j))
            wq.append((i, j))
            graph[i][j] = '.'

l1_y, l1_x = q.popleft()
l2_y, l2_x = q[0]
visited_find[l2_y][l2_x] = True

time = 0
while True:
    melt()
    if find():
        print(time)
        break
    wq, next_wq = next_wq, deque()
    q, next_q = next_q, deque()
    time += 1