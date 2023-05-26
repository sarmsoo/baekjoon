from sys import stdin
input = stdin.readline

def roll(y, x, order):
    # 동쪽, 3: 아랫면, 1: 동쪽, 4: 윗면, 6: 서쪽 / 2: 남쪽, 5: 북쪽
    if order == 1:
        dice[6], dice[3], dice[1], dice[4] = dice[3], dice[1], dice[4], dice[6]

    # 서쪽, 3: 윗면, 1: 서쪽, 4: 아랫면, 6: 동쪽 / 2: 남쪽, 5: 북쪽
    elif order == 2:
        dice[1], dice[4], dice[6], dice[3] = dice[3], dice[1], dice[4], dice[6]

    # 북쪽, 6: 남쪽, 2: 윗면, 1: 북쪽, 5: 아랫면 / 4: 서쪽, 3: 동쪽
    elif order == 3:
        dice[2], dice[1], dice[5], dice[6] = dice[6], dice[2], dice[1], dice[5]

    # 남쪽, 5: 윗면, 1: 남쪽, 2: 아랫면, 6: 북쪽 / 4: 서쪽, 3: 동쪽
    elif order == 4:
        dice[1], dice[2], dice[6], dice[5] = dice[5], dice[1], dice[2], dice[6]

    if graph[y][x] == 0:
        graph[y][x] = dice[6]
    else:
        dice[6] = graph[y][x]
        graph[y][x] = 0
    print(dice[1])
    return

n, m, y, x, k = map(int, input().split())

dy = [0, 0, 0, -1, 1]
dx = [0, 1, -1, 0, 0]

graph = [list(map(int, input().split())) for _ in range(n)]
dice = [0] * 7 # 윗면, 남쪽, 동쪽, 서쪽, 북쪽, 아랫면 (index 1부터)
orders = list(map(int, input().split()))

for order in orders:
    ny = y + dy[order]
    nx = x + dx[order]
    if ny < 0 or ny >= n or nx < 0 or nx >= m:
        continue
    y = ny
    x = nx
    roll(y, x, order)