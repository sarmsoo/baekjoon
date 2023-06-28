from sys import stdin
input = stdin.readline

def is_exist(y, x, num):
    for j in range(9):
        if graph[y][j] == num:
            return True

    for i in range(9):
        if graph[i][x] == num:
            return True

    square_y = (y // 3) * 3
    square_x = (x // 3) * 3
    for i in range(square_y, square_y + 3):
        for j in range(square_x, square_x + 3):
            if graph[i][j] == num:
                return True
    return False

def sol(depth):
    if depth == len(arr):
        for row in graph:
            print(*row)
        exit(0)

    y, x = arr[depth]
    for num in range(1, 10):
        if not is_exist(y, x, num):
            graph[y][x] = num

            sol(depth + 1)

            graph[y][x] = 0

graph = [list(map(int, input().split())) for _ in range(9)]
arr = []
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            arr.append((i, j))
sol(0)