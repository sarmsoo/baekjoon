'''
백트랙킹으로 조합 구현할 때, start에 i + 1을 넣어줘야 하는 걸 자꾸 까먹는데 기억하자.

꽃이 생길 때의 상황을 착각해서 시간을 되게 오래 먹음.
예를 들어, 꽃이 생기기 위해서는 visited의 [1][1]에 빨간색이 이미 있고
같은 시간에 초록색이 [1][1] 방문하면 생기는데,
여기서 나는 착각을 해서 빨간색이 [2][1], [1][2]...으로 이미 퍼졌다고(q에 들어갔다고)생각을 해서
[1][1]이 꽃이 되었을 때 퍼진 것들을 q에서 제거 해줘야 한다고 생각했다.
근데 안퍼졌던거임 ㅋㅋㄹㅇ
'''
from sys import stdin
from collections import deque
input = stdin.readline

def bfs() -> int:
    q = deque(tmp)
    visited = [[0] * m for _ in range(n)]
    for i, j, color in q:
        if color == 'R':
            visited[i][j] = 1
        elif color == 'G':
            visited[i][j] = -1
    result = 0
    time = 2
    while q:
        for _ in range(len(q)):
            y, x, color = q.popleft()
            if visited[y][x] == 'F':
                continue
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or ny >= n or nx < 0 or nx >= m:
                    continue
                if graph[ny][nx] == 0 or visited[ny][nx] == 'F':
                    continue

                if visited[ny][nx]:
                    if color == 'R' and not visited[ny][nx] + time:
                        visited[ny][nx] = 'F'
                        result += 1
                    elif color == 'G' and not visited[ny][nx] - time:
                        visited[ny][nx] = 'F'
                        result += 1

                elif not visited[ny][nx]:
                    if color == 'R':
                        visited[ny][nx] = time
                        q.append((ny, nx, 'R'))
                    elif color == 'G':
                        visited[ny][nx] = -time
                        q.append((ny, nx, 'G'))
        time += 1
    return result

def sol(start: int, red: int, green: int) -> None:
    global answer
    if red > r or green > g:
        return
    if red == r and green == g:
        answer = max(answer, bfs())
        return

    for i in range(start, len(arr)):
        y, x = arr[i]
        for color in ['R', 'G']:
            tmp.append((y, x, color))

            sol(i + 1, red + (color == 'R'), green + (color == 'G'))

            tmp.pop()

n, m, r, g = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

arr = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            arr.append((i, j))

tmp = []
answer = 0
sol(0, 0, 0)
print(answer)