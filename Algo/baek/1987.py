from sys import stdin
input = stdin.readline

def sol(y, x, depth, flag):
    global answer
    if flag:
        answer = max(answer, depth)
        return

    flag = True
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= r or nx < 0 or nx >= c:
            continue
        if alp[ord(graph[ny][nx]) - 65]:
            continue
        alp[ord(graph[ny][nx]) - 65] += 1
        flag = False

        sol(ny, nx, depth + 1, flag)

        alp[ord(graph[ny][nx]) - 65] -= 1

    if flag:
        sol(y, x, depth, True)


r, c = map(int, input().split())
graph = [input().strip() for _ in range(r)]
alp = [0] * 26

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

alp[ord(graph[0][0]) - 65] += 1

answer = 0
sol(0, 0, 1, False)

print(answer)