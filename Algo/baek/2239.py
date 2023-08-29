from sys import stdin
input = stdin.readline

def is_valid(num, y, x):
    start_r = y // 3 * 3
    start_c = x // 3 * 3
    for i in range(start_r, start_r + 3):
        for j in range(start_c, start_c + 3):
            if graph[i][j] == num:
                return False

    for j in range(9):
        if graph[y][j] == num:
            return False

    for i in range(9):
        if graph[i][x] == num:
            return False

    return True

def sol(depth):
    if depth == n:
        for row in graph:
            print(''.join(list(map(str, row))))
        exit(0)

    y, x = arr[depth]
    for num in range(1, 10):
        if not is_valid(num, y, x):
            continue
        graph[y][x] = num

        sol(depth + 1)

        graph[y][x] = 0


graph = [list(map(int, input().strip())) for _ in range(9)]

arr = []
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            arr.append((i, j))
n = len(arr)

sol(0)