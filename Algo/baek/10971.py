from sys import stdin
from sys import maxsize
input = stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 0
answer = maxsize

def sol(depth, prev, start):
    global result, answer
    if depth == n - 1:
        if graph[prev][start]:
            answer = min(answer, result + graph[prev][start])
        return

    for i in range(n):
        if visited[i] or graph[prev][i] == 0 or i == start:
            continue
        visited[i] = True
        result += graph[prev][i]

        sol(depth + 1, i, start)

        visited[i] = False
        result -= graph[prev][i]

for prev in range(n):
    visited = [False] * n
    sol(0, prev, prev)

print(answer)