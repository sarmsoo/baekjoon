from sys import stdin
input = stdin.readline

# list(zip(*sticker[::-1])) 이거 한 줄이면 끝남.
def rotate(r, c, sticker):
    tmp = [[0] * r for _ in range(c)]
    for i in range(c):
        for j in range(1, r + 1):
            tmp[i][j - 1] = sticker[-j][i]
    return tmp

def is_attachable(sticker, y, x, r, c):
    for i in range(y, y + r):
        for j in range(x, x + c):
            if sticker[i - y][j - x] == 1 and graph[i][j] == 1:
                return False
    return True

n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]

def attach(sticker, y, x, r, c):
    for i in range(y, y + r):
        for j in range(x, x + c):
            if graph[i][j] == 1:
                continue
            graph[i][j] = sticker[i - y][j - x]

for _ in range(k):
    r, c = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(r)]

    for _ in range(4):
        flag = False
        for i in range(n - r + 1):
            for j in range(m - c + 1):
                if is_attachable(sticker, i, j, r, c):
                    attach(sticker, i, j, r, c)
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
        else:
            sticker = rotate(r, c, sticker)
            r, c = c, r

answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            answer += 1
print(answer)