from sys import stdin
from collections import deque
input = stdin.readline

n, k = map(int, input().split())
visited = [False] * 100001
check = [-1] * 100001

def bfs():
    q = deque()
    q.append(n)
    visited[n] = True
    time = 0
    while q:
        for _ in range(len(q)):
            x = q.popleft()
            if x == k:
                print(time)
                data = []
                tmp = x
                while True:
                    if check[tmp] != -1:
                        data.append(tmp)
                        tmp = check[tmp]
                    else:
                        data.append(tmp)
                        break
                data.reverse()
                print(*data)
                return

            for i in [x + 1, x - 1, 2 * x]:
                nx = i
                if nx < 0 or nx > 100000:
                    continue
                if visited[nx]:
                    continue

                check[nx] = x
                q.append(nx)
                visited[nx] = True
        time += 1

bfs()