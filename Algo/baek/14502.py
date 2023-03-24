from collections import deque
import copy
import sys
input = sys.stdin.readline

d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def bfs():
    queue = deque()
    test_map = copy.deepcopy(lab_map)
    for i in range(n):
        for k in range(m):
            if test_map[i][k] == 2:
                queue.append((i, k))

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            dr = r+d[i][0]
            dc = c+d[i][1]

            if (0 <= dr < n) and (0 <= dc < m):
                if test_map[dr][dc] == 0:
                    test_map[dr][dc] = 2
                    queue.append((dr, dc))

    global result
    count = 0
    for i in range(n):
        for k in range(m):
            if test_map[i][k] == 0:
                count += 1

    result = max(result, count)


def make_wall(count):
    if count == 3:
        bfs()
        return
    for i in range(n):
        for k in range(m):
            if lab_map[i][k] == 0:
                lab_map[i][k] = 1
                make_wall(count+1)
                lab_map[i][k] = 0


n, m = map(int,input().split())
lab_map = [list(map(int,input().split())) for _ in range(n)]

result = 0
make_wall(0)

print(result)

# 순수 그 자체 코드

'''
from sys import stdin
from collections import deque
from copy import deepcopy
input = stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
graph_copy = deepcopy(graph)
visited = [[False] * m for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs():
    q = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                q.append((i, j))
                visited[i][j] = True
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if graph[ny][nx] != 0 or visited[ny][nx]:
                continue
            graph[ny][nx] = 2
            q.append((ny, nx))
            visited[ny][nx] = True

answer = 0
tmp = 0
for i1 in range(n):
    for j1 in range(m):
        if graph[i1][j1] == 0:
            graph[i1][j1] = 1

            for i2 in range(n):
                for j2 in range(m):
                    if graph[i2][j2] == 0:
                        graph[i2][j2] = 1

                        for i3 in range(n):
                            for j3 in range(m):
                                if graph[i3][j3] == 0:
                                    graph[i3][j3] = 1
                                    bfs()
                                    for y in range(n):
                                        for x in range(m):
                                            if graph[y][x] == 0:
                                                tmp += 1
                                    answer = max(answer, tmp)
                                    tmp = 0
                                    graph = deepcopy(graph_copy)
                                    graph[i1][j1] = 1
                                    graph[i2][j2] = 1
                                    visited = [[False] * m for _ in range(n)]
                        graph[i2][j2] = 0
            graph[i1][j1] = 0
print(answer)
'''