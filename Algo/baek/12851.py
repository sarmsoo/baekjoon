from collections import deque
n, k = map(int, input().split())
visited = [[0, 0] for _ in range(100001)]

def bfs():
    q = deque([n])
    visited[n][0] = 1
    time = 1
    flag = False
    while q:
        for _ in range(len(q)):
            x = q.popleft()

            if x == k:
                flag = True
                continue

            for nx in [2 * x, x + 1, x - 1]:
                if nx < 0 or nx > 100000:
                    continue
                if visited[nx][0] != 0:
                    if visited[nx][1] == time:
                        visited[nx][0] += visited[x][0]
                    elif visited[nx][1] < time:
                        continue

                else:
                    q.append(nx)
                    visited[nx][1] = time
                    visited[nx][0] += visited[x][0]

        if flag:
            return time - 1

        time += 1

print(bfs())
print(visited[k][0])