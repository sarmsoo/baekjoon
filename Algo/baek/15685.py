from sys import stdin
input = stdin.readline

def dragon_curve(y, x, directions, cnt, g):
    if cnt > g:
        return

    tmp = []
    for i in range(len(directions) - 1, -1, -1):
        nd = (directions[i] + 1) % 4
        y += dy[nd]
        x += dx[nd]
        graph[y][x] = 1

        tmp.append(nd)

    directions += tmp
    dragon_curve(y, x, directions, cnt + 1, g)

n = int(input())
graph = [[0] * 101 for _ in range(101)]
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
for _ in range(n):
    x, y, d, g = map(int, input().split())
    # 0세대 드래곤
    graph[y][x] = 1
    y += dy[d]
    x += dx[d]
    graph[y][x] = 1
    # n세대, n > 0
    directions = [d]
    dragon_curve(y, x, directions, 1, g)

answer = 0
for i in range(100):
    flag = False
    for j in range(100):
        if graph[i][j] == 1 and graph[i + 1][j] == 1 and graph[i][j + 1] == 1 and graph[i + 1][j + 1] == 1:
            answer += 1

print(answer)