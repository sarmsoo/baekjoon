from sys import stdin
input = stdin.readline

def dfs(r, c):
    color = graph[r][c]
    stack =[(r, c, -1, -1)]
    while stack:
        y, x, prev_y, prev_x = stack.pop()
        if visited[y][x]:
            continue

        visited[y][x] = True
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            # 이전 노드와 같으면
            if ny == prev_y and nx == prev_x:
                continue
            if graph[ny][nx] != color:
                continue

            if visited[ny][nx]:
                return True
            else:
                stack.append((ny, nx, y, x))

    return False


n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue
        if dfs(i, j):
            print("Yes")
            exit(0)
print("No")