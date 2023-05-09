from sys import stdin
from collections import deque
input = stdin.readline

n, m, k = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
# 0: 방문x
# 1:방문o 머무르기x
# 2:방문o 머무르기o
# visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]

visited = [[-1] * m for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

# 내가 짠 거, 7552ms
'''
def bfs():
    q = deque([(0, 0, k)])
    visited[0][0][k] = 2
    answer = 1
    day = True
    while q:
        for _ in range(len(q)):
            y, x, chance = q.popleft()
            if y == n - 1 and x == m - 1:
                return answer

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or ny >= n or nx < 0 or nx >= m:
                    continue
                # 벽 만났을 때
                if graph[ny][nx] == '1':
                    if day:
                        if visited[ny][nx][chance] == 0 and chance > 0:
                            visited[ny][nx][chance] = 1
                            visited[ny][nx][chance - 1] = 1 # 두번 방문 체크해야함
                            q.append((ny, nx, chance - 1))
                    elif not day and visited[y][x][chance] != 2:
                        q.append((y, x, chance))
                        visited[y][x][chance] = 2
                # 벽x
                elif graph[ny][nx] == '0':
                    if visited[ny][nx][chance] == 0:
                        q.append((ny, nx, chance))
                        visited[ny][nx][chance] = 1
        answer += 1
        day = not day
    return -1

print(bfs())
'''

# 다른 사람, 2844ms
def bfs():
    q = deque([(0, 0, k)])
    visited[0][0] = k
    answer = 1
    day = True
    while q:
        for _ in range(len(q)):
            y, x, chance = q.popleft()
            if y == n - 1 and x == m - 1:
                return answer

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or ny >= n or nx < 0 or nx >= m:
                    continue
                if visited[ny][nx] >= chance:
                    continue
                if graph[ny][nx] == '0':
                    q.append((ny, nx, chance))
                    visited[ny][nx] = chance

                elif chance > 0:
                    if day:
                        q.append((ny, nx, chance - 1))
                        visited[ny][nx] = chance
                    else:
                        q.append((y, x, chance))
        answer += 1
        day = not day
    return -1

print(bfs())



