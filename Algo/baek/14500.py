from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
max_value = 0


def dfs(y, x, sum_, cnt):
    global max_value

    if cnt == 4:
        max_value = max(max_value, sum_)
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= n or nx < 0 or nx >= m:
            continue
        if visited[ny][nx]:
            continue

        visited[ny][nx] = True
        dfs(ny, nx, sum_ + graph[ny][nx], cnt + 1)
        visited[ny][nx] = False


def exce(y, x):
    global max_value
    for p in range(4):
        tmp = graph[y][x]
        for q in range(3):
            t = (p + q) % 4
            ny = y + dy[t]
            nx = x + dx[t]

            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                break
            tmp += graph[ny][nx]
        max_value = max(max_value, tmp)


for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, graph[i][j], 1)
        visited[i][j] = False

        exce(i, j)

print(max_value)