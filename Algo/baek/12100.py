from sys import stdin
from copy import deepcopy
input = stdin.readline

def move(dir, graph):
    if dir == 0:
        for j in range(n):
            top = 0
            for i in range(1, n):
                if graph[i][j] == 0:
                    continue
                tmp = graph[i][j]
                graph[i][j] = 0
                if graph[top][j] == 0:
                    graph[top][j] = tmp
                elif graph[top][j] == tmp:
                    graph[top][j] = 2 * tmp
                    top += 1
                else:
                    top += 1
                    graph[top][j] = tmp

    elif dir == 1:
        for j in range(n):
            top = n - 1
            for i in range(n - 2, -1, -1):
                if graph[i][j] == 0:
                    continue
                tmp = graph[i][j]
                graph[i][j] = 0
                if graph[top][j] == 0:
                    graph[top][j] = tmp
                elif graph[top][j] == tmp:
                    graph[top][j] = 2 * tmp
                    top -= 1
                else:
                    top -= 1
                    graph[top][j] = tmp

    elif dir == 2:
        for i in range(n):
            top = 0
            for j in range(1, n):
                if graph[i][j] == 0:
                    continue
                tmp = graph[i][j]
                graph[i][j] = 0
                if graph[i][top] == 0:
                    graph[i][top] = tmp
                elif graph[i][top] == tmp:
                    graph[i][top] = 2 * tmp
                    top += 1
                else:
                    top += 1
                    graph[i][top] = tmp

    elif dir == 3:
        for i in range(n):
            top = n - 1
            for j in range(n - 2, -1, -1):
                if graph[i][j] == 0:
                    continue
                tmp = graph[i][j]
                graph[i][j] = 0
                if graph[i][top] == 0:
                    graph[i][top] = tmp
                elif graph[i][top] == tmp:
                    graph[i][top] = 2 * tmp
                    top -= 1
                else:
                    top -= 1
                    graph[i][top] = tmp
    return graph

def sol(depth, graph):
    global answer
    if depth == 5:
        for i in range(n):
            for j in range(n):
                answer = max(answer, graph[i][j])
        return

    for i in range(4):
        tmp_graph = move(i, deepcopy(graph))
        sol(depth + 1, tmp_graph)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

answer = 0
sol(0, board)
print(answer)