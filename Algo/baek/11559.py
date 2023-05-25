from sys import stdin
input = stdin.readline

def dfs(i, j, color):
    stack = [(i, j)]
    visited = [[False] * 6 for _ in range(12)]
    result = []
    while stack:
        y, x = stack.pop()
        if visited[y][x]:
            continue
        visited[y][x] = True
        result.append((y, x))
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= 12 or nx < 0 or nx >= 6:
                continue
            if graph[ny][nx] != color:
                continue
            stack.append((ny, nx))

    return result


graph = [list(input().strip()) for _ in range(12)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

answer = 0
while True:
    flag = False
    for i in range(12):
        for j in range(6):
            if graph[i][j] == '.':
                continue

            result = dfs(i, j, graph[i][j])
            if len(result) < 4:
                continue

            flag = True
            for y, x in result:
                graph[y][x] = '.'

    if not flag:
        break

    answer += 1

    for j in range(6):
        tmp = []
        for i in range(11, -1, -1):
            if graph[i][j] == '.':
                continue
            tmp.append(graph[i][j])

        tmp = tmp + ['.'] * (12 - len(tmp))
        for i in range(12):
            graph[i][j] = tmp[11 - i]

print(answer)