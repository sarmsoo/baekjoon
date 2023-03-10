from sys import stdin
input = stdin.readline

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

white = 0
blue = 0


def sol(n, y, x):
    global white, blue
    for i in range(y, y + n):
        for j in range(x, x + n):
            if graph[i][j] != graph[y][x]:
                sol(n // 2, y, x)
                sol(n // 2, y + n // 2, x)
                sol(n // 2, y, x + n // 2)
                sol(n // 2, y + n // 2, x + n // 2)
                return
    if graph[y][x] == 1:
        blue += 1
    else:
        white += 1
    return


sol(n, 0, 0)
print(white)
print(blue)




