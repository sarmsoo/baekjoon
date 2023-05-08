from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
graph = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
visited = [[False] * (n + 1) for _ in range(n + 1)] # 방문했는지 체크
lighted = [[False] * (n + 1) for _ in range(n + 1)] # 불이 켜진지 체크

for _ in range(m):
    x, y, a, b = map(int, input().split())
    graph[y][x].append((b, a))

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs():
    q = deque([(1, 1)])
    visited[1][1] = True
    lighted[1][1] = True
    answer = 1
    while q:
        y, x = q.popleft()
        if len(graph[y][x]):
            for _ in range(len(graph[y][x])):
                b, a = graph[y][x].pop()
                # 이미 켜진 곳은 할 필요가 없음
                if lighted[b][a]:
                    continue
                lighted[b][a] = True
                answer += 1
                # 불이 켜진 곳이 방문 가능 한 곳 인지, 방문 가능하면 큐에 추가
                for i in range(4):
                    nb = b + dy[i]
                    na = a + dx[i]
                    if nb < 1 or nb > n or na < 1 or na > n:
                        continue
                    if visited[nb][na]:
                        q.append((b, a))
                        visited[b][a] = True
                        break
        # 이동한 곳 주변에 방문 가능한 곳이 있는지
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 1 or ny > n or nx < 1 or nx > n:
                continue
            if lighted[ny][nx] and not visited[ny][nx]:
                q.append((ny, nx))
                visited[ny][nx] = True
    return answer

print(bfs())