from sys import stdin
input = stdin.readline

n = int(input())
graph = [list(input().strip()) for _ in range(n)]


def find_max_candy():
    max_ = 1
    for i in range(n):
        for j in range(n):
            flag1, flag2 = True, True
            if i + 1 >= n:
                flag1 = False
            if flag1:
                if graph[i][j] == graph[i + 1][j]:
                    temp = 1
                    ny = i
                    while True:
                        ny += 1
                        if ny >= n:
                            break
                        if graph[i][j] != graph[ny][j]:
                            break
                        if graph[i][j] == graph[ny][j]:
                            temp += 1
                    max_ = max(max_, temp)

            if j + 1 >= n:
                flag2 = False
            if flag2:
                if graph[i][j] == graph[i][j + 1]:
                    temp = 1
                    nx = j
                    while True:
                        nx += 1
                        if nx >= n:
                            break
                        if graph[i][j] != graph[i][nx]:
                            break
                        if graph[i][j] == graph[i][nx]:
                            temp += 1
                    max_ = max(max_, temp)
    return max_


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
answer = 0
for i in range(n):
    for j in range(n):
        for k in range(4):
            y = i + dy[k]
            x = j + dx[k]
            if y < 0 or y >= n or x < 0 or x >= n:
                continue
            if graph[y][x] == graph[i][j]:
                continue
            graph[i][j], graph[y][x] = graph[y][x], graph[i][j]
            answer = max(answer, find_max_candy())
            graph[i][j], graph[y][x] = graph[y][x], graph[i][j]
            if answer == n:
                print(n)
                exit(0)
print(answer)