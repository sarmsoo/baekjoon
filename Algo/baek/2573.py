from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def dfs(y, x):
    stack = [(y, x)]
    while stack:
        cy, cx = stack.pop()
        if not visited[cy][cx]:
            visited[cy][cx] = True
            for i in range(4):
                ny = cy + dy[i]
                nx = cx + dx[i]
                if ny < 0 or ny >= n or nx < 0 or nx >= m:
                    continue
                if graph[ny][nx] == 0:
                    continue
                stack.append((ny, nx))

# 빙하 녹이기
def melt():
    q = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                q.append((i, j))
    result = []
    while q:
        cy, cx = q.popleft()
        cnt = 0
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if graph[ny][nx] == 0:
                cnt += 1
        # 일괄적으로 빙하를 녹이기 위한 과정1
        if cnt > 0:
            result.append((cy, cx, cnt))
    # 일괄적으로 빙하를 녹이기 위한 과정2
    for i in range(len(result)):
        y, x, cnt = result[i]
        graph[y][x] = graph[y][x] - cnt if graph[y][x] > cnt else 0

answer = 0
while True:
    visited = [[False] * m for _ in range(n)]
    tmp = 0
    answer += 1
    melt()
    # 빙하 분리됐는지 체크
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and not visited[i][j]:
                dfs(i, j)
                tmp += 1
    # 빙하가 분리 되었으면
    if tmp >= 2:
        print(answer)
        break
    # 분리 되지 않았으면
    flag = False
    # 빙하가 다 녹는 경우 고려
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                flag = True
                break
    if not flag:
        print(0)
        break