from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
k = int(input())
graph = [[0] * n for _ in range(n)]
for _ in range(k):
    y, x = map(int, input().split())
    graph[y - 1][x - 1] = 2 # 2 == 사과


l = int(input())
instr = deque()
for _ in range(l):
    x, c = input().strip().split()
    instr.append((int(x), c))

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

snake = deque([(0, 0)])
graph[0][0] = 1
direction = 0
time = 0
while True:
    time += 1

    if instr:
        if time > instr[0][0]:
            c = instr.popleft()[1]
            if c == 'D':
                direction = (direction + 1) % 4
            elif c == 'L':
                direction = (direction - 1) % 4

    y, x = snake[0]
    ny = y + dy[direction]
    nx = x + dx[direction]
    if ny < 0 or ny >= n or nx < 0 or nx >= n:
        break
    if graph[ny][nx] == 1:
        break
    if graph[ny][nx] == 0:
        tail_y, tail_x = snake.pop()
        graph[tail_y][tail_x] = 0
    graph[ny][nx] = 1
    snake.appendleft((ny, nx))

print(time)